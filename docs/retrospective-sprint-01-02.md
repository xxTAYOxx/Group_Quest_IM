# Retrospektive: Sprint 1 + Sprint 2

**Datum:** 2026-05-13
**Projekt:** ListMate (Group Quest)
**Anwesend (laut LV-Vorgabe: ohne PO):**
- Scrum Master: Aloys Trinker
- Development Team: Paul Wiedermann, Tim Sindilar, Laetitia Weben

---

## 1. Wo stehen wir mit unserem App-Projekt gerade?

Wir haben in zwei Sprints einen vollständig funktionsfähigen Single-User-Kern von **ListMate** gebaut:

- Registrierung mit Email + Username + Passwort (bcrypt-Hashing)
- Login / Logout über `st.session_state`
- "My Lists"-Übersicht mit Erstellung neuer Shopping-Listen
- List-Detail-Page mit Add-Item-Form, Check-Box-Ticken und Item-Löschen

**Backlog-Stand:** 8 von 24 User-Stories abgeschlossen (33%). Im GitHub-Project-Board sind alle erledigten Stories sauber als Sprint 1 bzw. Sprint 2 markiert und in der `Done`-Spalte. Die App läuft lokal unter `streamlit run app.py`, der Demo-Flow für den Sprint Review funktioniert end-to-end.

**Konkrete geschlossene Issues:**
- Sprint 1 (Auth + List-Foundation): US-01, US-02, US-03, US-05, US-06
- Sprint 2 (Item-CRUD): US-09, US-10, US-12

---

## 2. Wie hat uns SCRUM dabei unterstützt, den aktuellen Zwischenstand zu erreichen?

- **T-Shirt-Sizing** (Planning Poker in Tag 1) hat unsere Sprint-Kapazität realistisch eingeschätzt - wir haben in beiden Sprints alle committeden Stories tatsächlich geschafft, nichts blieb über.
- **Klar definierte Sprint-Ziele** ("User registriert + erstellt erste Liste" / "User verwaltet Items einer Liste") haben verhindert, dass wir uns in Polish- oder Nice-to-have-Arbeit verlieren.
- **Priorisierung P0/P1/P2** hat dafür gesorgt, dass wir die Kern-User-Journey (Register → Liste → Items) vor Komfort-Features wie Profile oder Insights bauen.
- **GitHub Issues mit Acceptance Criteria** haben uns bei jeder Story einen klaren "Fertig"-Begriff gegeben. Im Sprint Review ist die PO-Freigabe damit nahezu objektiv.
- **Die Definition of Done pro Sprint** im Sprint-Planning-Doc hat uns davor bewahrt, eine Story "fast fertig" liegen zu lassen.

---

## 3. Wo hat uns SCRUM behindert?

- **Ceremonien-Overhead bei kurzen Sprints:** Planning (5 min) + Review (5 min) sind bei einem 60-min-Sprint relativ teuer im Verhältnis zur reinen Coding-Zeit. Bei längeren Sprints (1-2 Wochen) würde sich der Aufwand besser amortisieren.
- **Lineare Story-Bearbeitung trotz 3 Devs:** Wir haben in beiden Sprints faktisch sequentiell entwickelt statt parallel, weil wir alle auf `main` committed haben und uns nicht in die Quere kommen wollten. Branches hätten parallele Arbeit ermöglicht (kommt in Tag 3).
- **"Out of Scope"-Striktheit:** Manche kleinen Verbesserungen (z. B. `lists.last_updated` automatisch updaten beim Item-Add) sind beim Implementieren naheliegend, aber gehören streng gesehen erst in einen späteren Sprint. Wir haben pragmatisch entschieden, solche minimalen Cleanups sofort mitzunehmen - das war nicht ganz Sprint-Goal-rein.

---

## 4. Welche SCRUM-Tools setzten wir aktuell ein und funktionieren diese für uns als Gruppe?

| Tool | Verwendung | Funktioniert für uns? |
|---|---|---|
| **GitHub Repository** | Zentrale Codebasis, jeder Sprint ein klarer Commit-Block | ✅ Ja, sehr gut |
| **GitHub Milestones (F1-F7)** | Feature-Gruppierung für unsere 7 Features | ✅ Ja, gibt sofort den Feature-Überblick |
| **GitHub Issues (US-01 bis US-24)** | User Stories mit Acceptance Criteria | ✅ Essentiell - ohne hätten wir die DoD nicht im Griff |
| **GitHub Project v2** | Backlog-Board mit Custom Fields (Priority, T-Shirt Size, Sprint) | ✅ Sehr gute Sichtbarkeit, Filter pro Sprint funktioniert |
| **Sprint-Planning-Markdowns** (`docs/sprint-0X-planning.md`) | Sprint-Goal + Selected Stories + DoD an einer Stelle | ✅ Ja, ideal für den Projektbericht |
| **`Closes #N` in Commits** | Auto-Closing von Issues beim Push | ✅ Funktioniert tadellos |

**Was uns aktuell fehlt (kommt in Sprint 3):**
- Feature-Branches und Pull Requests - bisher alles direkt auf `main`. Tag 3 startet mit dem Branching-Megatutorial, ab Sprint 3 nutzen wir Branches.

---

## 5. Was ändern wir im nächsten Sprint, um effizienter arbeiten zu können?

| Änderung | Was wir uns davon erwarten |
|---|---|
| **Feature-Branches einführen** (`feature/sprint-3-sharing`) | Parallele Story-Bearbeitung möglich, jeder Dev kann unabhängig committen |
| **Pull Requests für Sprint-Reviews** | PO kann das Sprint-Ergebnis am Diff reviewen statt nur im Live-Browser |
| **Vor jedem Sprint kurzes Sync wer welche Story macht** | Vermeidet, dass zwei Devs an derselben Datei parallel arbeiten |
| **`Closes #N` weiterhin in jeder Commit-Message** | Automatisches Issue-Closing beim Merge, weniger manuelle Pflege |
| **Sprint-Goal vor jeder Implementation laut vorlesen** | Stellt sicher, dass wir wirklich nur Goal-relevante Stories anpacken |

---

## Action Items für Sprint 3

- [ ] Feature-Branch `feature/sprint-3-sharing` von `main` abzweigen, bevor wir mit Sprint-3-Implementierung starten
- [ ] PR-Workflow: Branch → Commit → Push → Pull Request → Review → Merge
- [ ] Sprint-Goal "Two or more users can collaborate on a shared shopping list" als Header in den Sprint-Planning-Doc
- [ ] Sprint-Review auch im Project-Board: Stories nach PO-Approval auf `Done` ziehen
