# Sprint 3 — Planning

**Project:** ListMate
**Date:** 2026-05-13 (Tag 3 nach LV-Plan, nach Branching-Megatutorial)
**Sprint Duration:** ~60 min effective coding
**Team Capacity:** 3 Developers
**Branch:** `feature/sprint-3-sharing` — first sprint using a feature branch + Pull Request (per Sprint 1+2 retrospective action item).

---

## Sprint Goal

> **"Two or more users can collaborate on the same shopping list — owners can invite other users, and invited users can see and edit shared lists alongside the owner."**

This sprint turns ListMate from a single-user app into a real collaborative tool, which is the whole point of the product idea.

---

## Selected Stories

| # | Story | Issue | Size | Priority | Why it fits the Sprint Goal |
|---|---|---|---|---|---|
| 1 | US-13 Invite collaborator | [#13](https://github.com/xxTAYOxx/Group_Quest_IM/issues/13) | M | P0 | Without invite, no sharing — entry point for the whole feature |
| 2 | US-14 "Shared with me" tab | [#14](https://github.com/xxTAYOxx/Group_Quest_IM/issues/14) | S | P0 | Invited users need to *find* the lists they were invited to |
| 3 | US-15 Collaborator panel | [#15](https://github.com/xxTAYOxx/Group_Quest_IM/issues/15) | S | P1 | Members need transparency about who else has access |

**Total commitment:** 1× M + 2× S — comfortable for 3 devs.

**Deliberate exclusion** to keep the Goal sharp:
- US-11 (Edit item) — useful but unrelated to sharing → Sprint 4 or 5
- US-16 (Remove collaborator) — P2, can wait → backlog

---

## Definition of Done

- [ ] New table `list_collaborators (list_id, user_id, invited_by, invited_at)` migrated and indexed
- [ ] On list-detail page (only as owner): an Invite form accepting an existing username
- [ ] Invite form validates: username exists / not already collaborator / not the owner themselves — clear inline errors
- [ ] On "My Lists" page: two tabs — *My Lists* (owned) and *Shared with me* (where I'm a collaborator)
- [ ] Each shared list shows owner's username on the card
- [ ] Collaborators can open a shared list and add / check / delete items, just like owners
- [ ] Member panel in the sidebar of every list-detail page lists owner + all collaborators
- [ ] Smoke test: 2 simulated users, owner invites collaborator, collaborator sees + edits the list
- [ ] PR opened against `main` with the Sprint Goal as title, PO approves the PR diff, merge to `main`

---

## Out of Scope for Sprint 3

- US-11 Edit item — Sprint 4 or 5
- US-16 Remove collaborator — backlog (P2)
- US-17 Category dropdown / US-18 grouped view / US-19 unchecked-first sort — Sprint 4
- US-20 Shopping Mode toggle / US-21 Undo — Sprint 4
- US-22-24 Insights / autocomplete — Sprint 5 (Stretch)

---

## Roles

| Role | Person | Sprint 3 duties |
|---|---|---|
| Product Owner | Karl Schmidt | Reviews the PR diff in the Sprint Review, approves or rejects |
| Scrum Master | Aloys Trinker | Facilitates planning + review + retrospective, removes blockers |
| Developer | Paul Wiedermann | US-13 (invite form + validation + DB insert) |
| Developer | Tim Sindilar | US-14 (Shared-with-me tab + access control extension in list-detail) |
| Developer | Laetitia Weben | US-15 (Member panel in sidebar) + schema migration |

---

## Branching Workflow (introduced this sprint)

1. `git checkout -b feature/sprint-3-sharing` from `main`
2. Each commit explicitly references the story it solves (e.g. `feat: invite collaborator (US-13)`)
3. When all 3 stories pass smoke-test, push branch and open a PR titled "Sprint 3 — Sharing & Collaboration"
4. PR description references `Closes #13`, `Closes #14`, `Closes #15`
5. PO reviews the PR diff (Sprint Review)
6. On approval: squash-merge to `main`, issues auto-close, items move to Done in the Project board
