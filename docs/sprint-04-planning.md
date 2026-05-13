# Sprint 4 — Planning

**Project:** ListMate
**Date:** 2026-05-13 (Tag 3, zweiter Sprint)
**Sprint Duration:** ~12 min effective coding (Mini-Sprint, bewusste Zeit-Box wegen knappem Restbudget)
**Team Capacity:** 3 Developers
**Branch:** `feature/sprint-4-categories-sorting`

---

## Sprint Goal

> **"Items can be classified by category and unchecked items always appear first, so shopping is faster and more organized."**

This is a focused UX polish sprint. The team explicitly scoped down to two small stories because the LV time-box for Tag 3 is nearly over and the team prioritized documentation quality for the project report.

---

## Selected Stories

| # | Story | Issue | Size | Priority | Why it fits the Sprint Goal |
|---|---|---|---|---|---|
| 1 | US-17 Category dropdown | [#17](https://github.com/xxTAYOxx/Group_Quest_IM/issues/17) | S | P1 | Item-organization core: classify with a fixed set instead of free-text |
| 2 | US-19 Unchecked items first | [#19](https://github.com/xxTAYOxx/Group_Quest_IM/issues/19) | S | P1 | Shopping-flow improvement: focus stays on what is still to buy |

**Total commitment:** 2× S — deliberately tight.

**Deliberate exclusion from the Sprint Goal:**
- US-18 (Group-by-category view) — would expand the visual change too much for the time-box → backlog for Sprint 5 or beyond
- US-20 (Shopping-Mode toggle) — same reason
- US-21 (Undo) — P2, optional

---

## Definition of Done

- [ ] *Add item* form uses an `st.selectbox` with the predefined category list (Dairy, Produce, Bakery, Meat, Drinks, Household, Other) — no more free-text category typing
- [ ] Default selection: "Other"
- [ ] Category column on `items` table stores one of the predefined values (no schema migration needed; the column already exists with default 'Other')
- [ ] Items list on the list-detail page is sorted so that **unchecked items appear above checked items**, preserving their original `position` within each group
- [ ] Smoke test: adding items with different categories writes the right value; sorting puts checked items at the bottom
- [ ] PR opened, PO approves the diff, squash-merge to `main`, issues #17 + #19 close automatically, project-board items move to Done

---

## Out of Scope for Sprint 4

- US-18 Grouped-by-category view → Sprint 5 (Stretch)
- US-20 Shopping Mode toggle / US-21 Undo → Sprint 5 (Stretch)
- US-04 Profile · US-07 Rename · US-08 Delete list → Sprint 5
- US-11 Edit item · US-16 Remove collaborator → Backlog
- US-22-24 Insights/Autocomplete → Backlog or Stretch

---

## Roles

| Role | Person | Sprint 4 duties |
|---|---|---|
| Product Owner | Karl Schmidt | Reviews PR diff, approves |
| Scrum Master | Aloys Trinker | Facilitates planning + review + Sprint-3+4 retrospective afterwards |
| Developer | Paul Wiedermann | US-17 (selectbox + form-state) |
| Developer | Tim Sindilar | US-19 (ORDER BY in items query) |
| Developer | Laetitia Weben | Smoke test + PR description |
