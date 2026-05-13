# Sprint 1 — Planning

**Project:** ListMate
**Date:** 2026-05-13
**Sprint Duration:** ~70 min effective coding
**Team Capacity:** 3 Developers × ~70 min

---

## Sprint Goal

> **"A new user can register, log in, and create their first shopping list."**

This is the minimum viable end-to-end slice that proves the foundation works: authentication is wired up, the SQLite database is initialized, and the core "list" entity exists. Without this, nothing else in the backlog can be built.

---

## Selected Stories

| # | Story | Issue | Size | Priority | Rationale |
|---|---|---|---|---|---|
| 1 | US-01 Register | [#1](https://github.com/xxTAYOxx/Group_Quest_IM/issues/1) | M | P0 | Foundation — without auth, nothing else can be user-scoped |
| 2 | US-02 Login | [#2](https://github.com/xxTAYOxx/Group_Quest_IM/issues/2) | S | P0 | Direct follow-up to registration |
| 3 | US-03 Logout | [#3](https://github.com/xxTAYOxx/Group_Quest_IM/issues/3) | XS | P0 | Trivial closure of auth flow |
| 4 | US-05 Create List | [#5](https://github.com/xxTAYOxx/Group_Quest_IM/issues/5) | M | P0 | Second half of the Sprint Goal |
| 5 | US-06 My Lists | [#6](https://github.com/xxTAYOxx/Group_Quest_IM/issues/6) | S | P0 | Pulled in due to 3-dev capacity — makes Sprint Goal demo-able |

**Total commitment:** 2× M + 2× S + 1× XS ≈ realistic for 3 devs × 70 min.

---

## Definition of Done (Sprint 1)

A user reviewing the result with the Product Owner should be able to:

- [ ] Run the app locally with `streamlit run app.py`
- [ ] See an empty SQLite file (`listmate.db`) get auto-created on first start
- [ ] Register a new user via the UI — password is hashed in DB (verify with `sqlite3 listmate.db "SELECT * FROM users"`)
- [ ] Log out, then log back in with the same credentials
- [ ] After login, create a shopping list with a name (e.g. "Groceries Tuesday") — see it persisted in `lists` table
- [ ] Log out — list is no longer visible without logging in
- [ ] Read the README and follow setup instructions from scratch on a clean machine

Code-quality requirements:
- [ ] All Sprint-1 changes pushed to `main` (or merged via PR)
- [ ] No hard-coded secrets in code
- [ ] `requirements.txt` lists all runtime dependencies

---

## Out of Scope for Sprint 1

These stories explicitly belong to later sprints — do **not** build them now even if there's time:

- US-04 Profile page → Sprint 5
- US-06 My Lists page (browsing multiple lists) → Sprint 2
- US-09 Add item to list → Sprint 2
- US-13 / US-14 Sharing → Sprint 3
- All P1/P2 features → later sprints

If time remains: pull the next P0 story (US-06 My Lists) into the sprint with team consent.

---

## Technical Notes for Sprint 1 Implementation

- File layout to set up:
  - `app.py` — Streamlit entry point with login gate + page router
  - `db.py` — SQLite connection, schema-init on first run
  - `auth.py` — `hash_password`, `verify_password`, `current_user`
  - `schema.sql` — DDL for `users`, `lists` (other tables can wait)
- Use `bcrypt` for hashing (already in `requirements.txt`)
- Session state: `st.session_state.user` = `{"id": int, "username": str}` or `None`
- DB path: `listmate.db` in repo root, auto-created on first run, ignored by git

---

## Roles in this Sprint

| Role | Person | Sprint 1 duties |
|---|---|---|
| Product Owner | Karl Schmidt | Defines acceptance, reviews demo, signs off |
| Scrum Master | Aloys Trinker | Facilitates planning + review, removes blockers |
| Developer | Paul Wiedermann | Implements US-01, US-02, US-03 (auth flow) |
| Developer | Tim Sindilar | Implements US-05 (create list) + DB schema + project structure |
| Developer | Laetitia Weben | Implements US-06 (My Lists page) + UI polish for Sprint 1 |

---

## Sprint Review Checklist

At end of sprint, the PO does:

- [ ] Live walkthrough of all 4 stories in the running app
- [ ] Move accepted stories to `Done` column in the GitHub Project
- [ ] For any rejected story: move back to Backlog with a comment explaining what is missing

---

## Notes for the Project Report

For the Tag-2 retrospective and project report, capture:

- Did we hit the Sprint Goal? Yes/No, why?
- T-Shirt size estimates vs. actual effort — were any way off?
- Pair work vs. solo work distribution between the two devs
- Blockers encountered, and how they were resolved (or not)
