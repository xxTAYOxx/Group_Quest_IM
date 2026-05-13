# Sprint 2 — Planning

**Project:** ListMate
**Date:** 2026-05-13
**Sprint Duration:** ~60 min effective coding
**Team Capacity:** 3 Developers

---

## Sprint Goal

> **"A logged-in user can add items to a shopping list, tick them off while shopping, and remove items they no longer need."**

This builds directly on Sprint 1: lists now have *content*. After this sprint, the core single-user shopping flow works end-to-end.

---

## Selected Stories

| # | Story | Issue | Size | Priority | Rationale |
|---|---|---|---|---|---|
| 1 | US-09 Add item | [#9](https://github.com/xxTAYOxx/Group_Quest_IM/issues/9) | M | P0 | Without items, lists are empty shells |
| 2 | US-10 Mark as bought | [#10](https://github.com/xxTAYOxx/Group_Quest_IM/issues/10) | S | P0 | The "shopping" verb in "shopping list" |
| 3 | US-12 Delete item | [#12](https://github.com/xxTAYOxx/Group_Quest_IM/issues/12) | XS | P1 | Trivial completion of basic CRUD |

**Total commitment:** 1× M + 1× S + 1× XS — comfortable for 3 devs.

---

## Definition of Done

- [ ] User can open a list from "My Lists" and see a per-list detail page
- [ ] User can add an item (name + optional quantity + optional category) — persists to DB
- [ ] User can tick the checkbox next to an item — strikethrough + `items.checked_at` set
- [ ] User can untick a previously-bought item — strikethrough removed
- [ ] User can delete an item — row removed from `items` table
- [ ] `lists.last_updated` is bumped whenever an item is added/changed
- [ ] Smoke test: full flow runs locally without errors
- [ ] Commit pushed to `main`; PO can demo end-to-end

---

## Out of Scope for Sprint 2

- Category dropdown / predefined categories → Sprint 4 (US-17)
- Edit item (US-11) → Sprint 3
- Sharing / collaborators / shared-with-me tab → Sprint 3 (US-13/14)
- Categories grouping view → Sprint 4 (US-18)
- Shopping Mode toggle → Sprint 4 (US-20)

---

## Roles

| Role | Person | Sprint 2 duties |
|---|---|---|
| Product Owner | Karl Schmidt | Reviews demo, signs off |
| Scrum Master | Aloys Trinker | Facilitates planning + review |
| Developer | Paul Wiedermann | US-09 (add item form + DB insert) |
| Developer | Tim Sindilar | US-10 (check-off + DB update) + schema migration |
| Developer | Laetitia Weben | US-12 (delete item) + list-detail page layout |
