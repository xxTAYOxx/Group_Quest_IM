# Sprint 5 — Planning (Final Sprint, Tag 4)

**Project:** ListMate
**Date:** 2026-05-13 (vorgezogen auf Tag-3-Abend wegen Restzeit)
**Sprint Duration:** ~15 min effective coding
**Team Capacity:** 3 Developers
**Branch:** `feature/sprint-5-final`

---

## Sprint Goal

> **"Items list reads cleanly in shared contexts: vertical alignment is correct and every item shows its author so collaborators can attribute changes."**

This is a **quality-and-trust sprint** rather than a feature-expansion sprint. The PO and the team explicitly decided to favor *bug-free polish* over additional features, motivated by the "100% bug-free" constraint set at the start of Sprint 5. Edit-Item (US-11) was considered but deferred to the backlog — the team chose to ship two very safe stories instead of three uncertain ones.

---

## Selected Stories

| # | Story | Issue | Size | Priority | Why it fits the Sprint Goal |
|---|---|---|---|---|---|
| 1 | UX-Fix: Item-row vertical alignment | (tech-debt, no separate issue) | XS | — | Bug found by PO during Sprint 4 review — checkbox, text and trash icon were on different heights. Fix via `vertical_alignment="center"` on `st.columns` (Streamlit ≥ 1.36, we have 1.50). |
| 2 | US-25 Show added-by user | [#27](https://github.com/xxTAYOxx/Group_Quest_IM/issues/27) | XS | P1 | New story created in response to PO feedback from Sprint 4: in shared lists, attribution was missing. Pure read-path change (JOIN + display), no write-path risk. |

**Deliberately NOT in Sprint 5** (with rationale, for the Sprint-4+5 retrospective):
- **US-11 Edit item** — moved to backlog. Edit-flow has subtle Streamlit-state-management edge cases (form-key collisions per row, conditional rendering, cancel semantics). The team's "100% bug-free" constraint made the risk/reward unfavorable for a final-sprint feature.
- US-04 Profile, US-07 Rename, US-08 Delete-list, US-16 Remove collaborator, US-18 Group-by-category view, US-20–24 Insights & Polish — backlog, will not be implemented in this project iteration.

---

## Definition of Done

- [ ] Item rows render with checkbox, label, delete-button on **the same vertical baseline** — verified visually
- [ ] Items query joins `users` on `items.added_by`
- [ ] Items added by *other* members display `· added by <username>` after the existing markdown — items added by **the current viewer** stay clean (avoid noise like "added by yourself")
- [ ] Smoke test: 2 users on a shared list, each sees their own items clean, the other's items annotated
- [ ] PR opened, PO approves, squash-merge to `main`, issue #27 closes automatically, project-board item moves to Done

---

## Out of Scope (final state of the project after Sprint 5)

After this sprint, **14 of 25 user stories** are closed (US-25 was added during this sprint). The remaining 11 stories are documented in the backlog and would be the priority candidates for a hypothetical Sprint 6. They are listed in the final-presentation document so the audience understands what the team chose **not** to do and why.

---

## Roles

| Role | Person | Sprint 5 duties |
|---|---|---|
| Product Owner | Karl Schmidt | Reviews PR diff, approves |
| Scrum Master | Aloys Trinker | Facilitates Sprint Planning + final Sprint Review + Sprint-4+5 retrospective |
| Developer | Paul Wiedermann | UI-alignment fix |
| Developer | Tim Sindilar | US-25 query + display |
| Developer | Laetitia Weben | Smoke test + PR-description |
