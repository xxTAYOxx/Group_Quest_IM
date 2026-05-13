# ListMate — Collaborative Shopping List App

A small Streamlit + SQLite app developed as part of the Software Engineering "Group Quest" course project.

ListMate lets a user create shopping lists, add items, mark them off while shopping, and share lists with other users.

---

## Team

| Role | Person |
|---|---|
| Product Owner | Karl Schmidt |
| Scrum Master | Aloys Trinker |
| Developer | Paul Wiedermann |
| Developer | Tim Sindilar |

**Stack Authority:** entire team.

---

## Tech Stack

- **Frontend:** Streamlit
- **Backend / DB:** SQLite (single `listmate.db` file)
- **Language:** Python 3.10+
- **Deployment:** Streamlit Community Cloud
- **Project Management:** GitHub Issues + Milestones + GitHub Project v2

---

## Project Structure (target, populated during Sprints)

```
app.py               # Streamlit entry point
db.py                # SQLite connection + schema init
auth.py              # Registration, login, session helpers
pages/               # Streamlit multipage app
schema.sql           # DDL for users, lists, list_collaborators, items
requirements.txt
docs/
  sprint-01-planning.md
  ...
```

---

## How to Run (target — implemented in Sprint 1)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

---

## Scrum Setup

- **5 Sprints** across 3 hands-on days
- **Backlog:** 7 Features (Milestones), 24 User Stories (Issues)
- **Sizing:** T-Shirt sizes (XS / S / M / L / XL), simulated Planning Poker
- **Priorities:** P0 (must) / P1 (should) / P2 (could)

See [docs/sprint-01-planning.md](docs/sprint-01-planning.md) for the active sprint plan.

---

## License

MIT — see [LICENSE](LICENSE).
