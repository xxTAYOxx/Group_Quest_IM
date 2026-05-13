# Sprint 3 — Review (LV-Ceremony)

**Date:** 2026-05-13
**Sprint:** 3 (Sharing & Collaboration)
**Branch under review:** `feature/sprint-3-sharing`
**Pull Request:** [#25 — Sprint 3 — Sharing & Collaboration](https://github.com/xxTAYOxx/Group_Quest_IM/pull/25)
**Attendees (per LV-Vorgabe):** PO Karl Schmidt · SM Aloys Trinker · Devs Paul Wiedermann, Tim Sindilar, Laetitia Weben

---

## 1. What the Development Team demoed

Per LV: *"Beim Sprint Review zeigen die Developer, was sie geleistet haben und erklären die umgesetzten User-Stories am fertigen Produkt."*

Live walkthrough on `http://localhost:8502` with the feature branch checked out:

1. **US-13 Invite collaborator** — Owner ("Tayo") opens list "Groceries Tuesday", expands the new *Invite collaborator* form, enters another username, clicks *Send invitation*.
2. **US-14 Shared with me tab** — Second user logs in, opens *My Lists*, switches to the new *Shared with me* tab.
3. **US-15 Collaborator panel** — In any list detail, the sidebar *Members* section shows owner + all collaborators.

---

## 2. PO Review Outcome

| Story | PO Decision | Reason |
|---|---|---|
| US-13 Invite collaborator | ❌ **Rejected (request changes)** | Tayo invited Karlo (verified correct spelling). Form cleared, no visible feedback. Karlo's *Shared with me* tab remained empty — invitation not persisted. |
| US-14 Shared with me tab | ⏸ Held | Logically depends on US-13. Cannot accept until US-13 works. |
| US-15 Collaborator panel | ✅ Approved | Member panel renders correctly for the owner-only state. |

Per LV-Vorgabe: *"Wenn er das tut, wird die User-Story auf done gesetzt. Ansonsten muss sie wieder zurück in den Product-Backlog um neu eingeplant zu werden."*

Since the PR is still in flight (not merged), we treat this as **"Request Changes" on the open Pull Request** rather than a hard reject-to-backlog. This is consistent with the Tag-1+2 retrospective decision to introduce a feature-branch + PR workflow at Tag 3.

---

## 3. Bug Analysis

### Symptom

- Owner submits *Invite collaborator* form
- Form clears (`clear_on_submit=True`) — no success or error message visible
- Sidebar *Members* panel still shows only the owner (no new collaborator)
- Invited user's *Shared with me* tab is empty
- No exception in the Streamlit terminal log

### Root Cause (verified by reproduction test)

In the original Sprint-3 implementation of [pages/02_List_Detail.py](../pages/02_List_Detail.py), `st.rerun()` was called **inside** the `with get_conn() as conn:` context manager:

```python
with get_conn() as conn:
    ...
    conn.execute("INSERT INTO list_collaborators ...")
    st.success(f"Invited '{uname}' to this list.")
    st.rerun()    # ← inside the with-block
```

`st.rerun()` is implemented in Streamlit as a `RerunException` that propagates up the call stack to restart the script. Python's `sqlite3.Connection` context manager treats **any exception** out of the `with`-block as a transaction failure and **rolls back uncommitted writes**.

Net effect: the `INSERT` happened, but was rolled back the same millisecond. No row reached disk. No exception was visible because Streamlit swallowed the `RerunException` at the top level.

### Reproduction (programmatic)

```bash
.venv/bin/python -c "
from db import init_db, get_conn
init_db()
# ... register Tayo + Karlo ...
class FakeRerun(Exception): pass
try:
    with get_conn() as conn:
        karlo_id = conn.execute('SELECT id FROM users WHERE username=?', ('Karlo',)).fetchone()['id']
        conn.execute('INSERT INTO list_collaborators ...', (...))
        raise FakeRerun('simulating st.rerun')
except FakeRerun:
    pass
# Check: 0 rows in list_collaborators → confirms rollback
"
```

Result: **0 rows persisted** when rerun-pattern is inside the `with`-block. Confirms the root cause.

---

## 4. Fix applied (same branch, request-changes loop)

Two coordinated changes in [pages/02_List_Detail.py](../pages/02_List_Detail.py):

### Fix 1 — Move `st.rerun()` out of `with get_conn()`
The submit handler now writes a one-shot message into `st.session_state["invite_feedback"]` from inside the `with`-block, exits the `with` cleanly (commit succeeds), and calls `st.rerun()` **after** that.

### Fix 2 — Persistent feedback message via `session_state`
A short renderer at the top of the page reads `st.session_state.pop("invite_feedback", ...)` and shows it as `st.success` or `st.error`. This survives unrelated reruns from other widgets (checkbox toggles, delete buttons).

### Fix 3 — Case-insensitive username lookup (defensive)
The user-lookup SQL changed from `WHERE username = ?` to `WHERE LOWER(username) = LOWER(?)`, and the *can't invite yourself* check compares `.lower()` on both sides. Not the root cause of the reported bug, but a robustness improvement: usernames are case-insensitive in every real product the team knows (GitHub, Slack, email). The success message uses the **stored** canonical username, not the user's input.

---

## 5. Verification (programmatic)

Run after the fix:

```text
=== Reproduce original bug: rerun inside with-block ===
Rows after rerun-inside-with: 0
  → Old behavior: ROLLED BACK (bug confirmed)

=== Verify fixed pattern: rerun OUTSIDE with-block ===
Rows after rerun-outside-with: 1
  → Fixed behavior: COMMITTED (fix works)
Feedback message: ('success', "Invited 'Karlo' to this list.")
Karlo shared-with-me: [('Groceries Tuesday', 'Tayo')]
PASS
```

Plus a manual re-test in the browser app on the updated PR:
- Tayo invites Karlo (correctly spelled) → green *"Invited 'Karlo' to this list."* persists above the invite form
- Tayo invites "karlo" (lowercase) → same green message, with the canonical "Karlo" capitalization in the text
- Karlo logs in → *Shared with me (1)* — list visible — opens it — adds an item

---

## 6. Lessons Learned (input for Sprint-3+4 retrospective)

- **Streamlit + sqlite3 idiom:** never call `st.rerun()` (or any other exception-raising flow-control) inside a `with sqlite3.Connection` block. Always exit the `with` cleanly first, then call `st.rerun()` on the next line.
- **Optimistic-UI smoke testing is not enough.** Our Sprint-3 smoke test simulated DB inserts directly in Python — it bypassed the actual Streamlit `st.rerun` codepath that triggered the bug. A more realistic integration test would have caught it.
- **PR-based Sprint Reviews catch things that direct-to-main commits hide:** the bug existed in the same form during Sprint-2 (`add item` form used the same pattern but the rerun was outside the `with`, by accident-not-design). The PR diff in Sprint 3 was small enough that this anti-pattern was reviewable — going forward we keep PRs small.

---

## 7. Status

- ✅ Fix committed on `feature/sprint-3-sharing`, PR #25 auto-updated
- ⏳ Awaiting **PO re-review** on the updated PR diff
- On re-approval → squash-merge → issues #13/#14/#15 close automatically → Project board items → Done
