# Retrospektive: Sprint 3 + Sprint 4

**Datum:** 2026-05-13 (Tag 3)
**Projekt:** ListMate (Group Quest)
**Anwesend (laut LV-Vorgabe: ohne PO):**
- Scrum Master: Aloys Trinker
- Development Team: Paul Wiedermann, Tim Sindilar, Laetitia Weben

---

## 1. Wo stehen wir mit unserem App-Projekt gerade?

Wir haben in vier Sprints einen funktionsfähigen **End-to-End-Flow inkl. Collaboration** umgesetzt. **13 von 24 User-Stories** sind geschlossen (54%). Konkret:

- **Sprint 1** (Auth-Foundation): Register, Login, Logout, Liste anlegen, My-Lists-Übersicht (5 Stories)
- **Sprint 2** (Item-CRUD): Items hinzufügen, abhaken, löschen (3 Stories)
- **Sprint 3** (Sharing): Collaborator einladen, Shared-with-me-Tab, Member-Panel (3 Stories) — **inkl. einer Hotfix-Iteration im PR durch PO-Feedback**
- **Sprint 4** (Polish): Category-Dropdown, Unchecked-first-Sort (2 Stories) — Mini-Sprint, bewusst zeitbeschränkt für Tag-3-Abschluss

Die App ist demo-fähig: zwei User können sich registrieren, eine Liste teilen, gemeinsam Items hinzufügen mit kategorisierten Einträgen, abhaken und in einer sinnvoll sortierten Reihenfolge sehen. Das **GitHub Project Board** zeigt alle 13 Done-Stories sauber nach Sprints 1–4 markiert.

**Was noch offen ist** für Tag 4 (Sprint 5): F1 Profile (US-04), F2 Rename + Delete Liste (US-07, US-08), F3 Edit Item (US-11), F4 Remove Collaborator (US-16), F5 Group-by-Category (US-18), F6 Shopping Mode + Undo (US-20, US-21), F7 Insights (US-22, US-23, US-24) — 11 Stories, mehr als für einen Sprint, also wird auch Sprint 5 priorisiert auswählen müssen.

---

## 2. Wie einfach war es, das Feedback aus der ersten Retrospektive in unsere Abläufe zu integrieren?

Aus der Tag-2-Retro hatten wir fünf konkrete Action Items. Bilanz pro Item:

| Action Item aus Retro 1+2 | Sprint 3 | Sprint 4 | Bilanz |
|---|---|---|---|
| Feature-Branches einführen | `feature/sprint-3-sharing` | `feature/sprint-4-categories-sorting` | ✅ Sehr einfach, hat sich gelohnt |
| Pull Requests für Sprint Reviews | PR #25 mit Review-Loop | PR #26 mit kurzem Review | ✅ Hat **direkt einen Bug aufgedeckt** (Invite-Rollback), den ein Direct-to-Main-Commit verschluckt hätte |
| Vor Sprint kurzes Sync wer welche Story macht | Im Sprint-Planning-Doc dokumentiert | Im Sprint-Planning-Doc dokumentiert | ✅ Hat funktioniert, keine Datei-Kollisionen |
| `Closes #N` in Commit-Messages | Konsequent durchgezogen | Konsequent durchgezogen | ✅ Auto-Close bei Merge ist eine wahre Quality-of-Life-Verbesserung |
| Sprint-Goal vor Implementation laut lesen | Implizit durchs Planning-Doc | Implizit durchs Planning-Doc | ✅ Hat uns Sprint 4 davor bewahrt, US-18 mitzubauen (war im Sprint Goal explizit out-of-scope) |

**Was schwerer war als gedacht:**
- Die erste PR-Review-Iteration mit Hotfix (Sprint 3, PR #25, *Invite Collaborator*) hat ~15 zusätzliche Minuten gekostet. Aber genau dieser Schritt hat einen echten Production-Bug abgefangen — also war es Zeit, die *gespart* hat (sonst wäre der Bug erst in der Final-Demo aufgefallen).
- Branching hat einen Tool-Effekt: man muss nach jedem Merge dran denken, lokal zu `git checkout main && git pull` und den Feature-Branch zu löschen. Wir haben das in den Bash-Workflow eingebaut, aber das ist neu für das Team.

**Was wir leicht reingeholt haben:**
- Sprint-Planning-Docs als Markdown im Repo (`docs/sprint-0X-planning.md`) waren ein direktes Ergebnis der Tag-2-Retro und haben uns in Sprint 3 + 4 schon stark geholfen — die Sprint-Goal-Disziplin ist deutlich besser geworden.

---

## 3. Wie geht ihr als Team mit dem Thema Komplexität um? Nutzt ihr aktuell Branches? Wenn ja, was hat gut funktioniert / was vielleicht nicht?

**Ja, ab Sprint 3 nutzen wir Feature-Branches + Pull Requests konsequent.** Das war eines unserer Retro-Action-Items und wir haben es direkt nach dem Tag-3-Branching-Megatutorial umgesetzt.

### Was hat **gut funktioniert**:

1. **PR-Review als Sprint-Review-Artefakt** — der PO konnte den Diff statt nur den Live-Browser anschauen. Das ist objektiver und gibt einen besseren Audit-Trail im Projektbericht. In PR #25 hat genau dieses Format einen Bug aufgedeckt, den wir live nie gesehen hätten.
2. **Saubere Sprint-Trennung** — jeder Sprint hat seinen eigenen Branch + PR + Commit-Block in der Historie. Bei `git log --oneline` sieht man auf einen Blick, was zu welchem Sprint gehört.
3. **`Closes #N` in PR + Squash-Merge** — Auto-Close-Mechanik. Issues schließen automatisch, sobald der Merge durch ist. Project-Board manuell auf Done ziehen ist ein Extra-Schritt, aber das hatten wir vorher auch.
4. **Mini-Sprint 4 mit nur 2 Stories** — bewusst kleiner gefasste Time-Box hat funktioniert. Wir hatten Restzeit für Doku und Präsentation. Komplexität durch Reduktion auf das Wesentliche kontrolliert.

### Was **nicht** gut funktioniert hat / unsere Lehren:

1. **Sprint-3-Hotfix-Loop**: PR #25 enthielt einen subtilen Bug (`st.rerun()` innerhalb `with sqlite3.connection`-Block → Transaktion wird gerollbackt, kein sichtbarer Fehler). Unser Sprint-3-Smoke-Test umging diesen Codepath, weil er DB-Operationen direkt in Python ausführte ohne über `st.rerun` zu gehen. **Lesson:** Realistic-Path-Tests sind wichtiger als reine Funktions-Tests. Im Projektbericht festgehalten als technisches Lesson Learned.
2. **Branch-Cleanup ist Disziplin-Arbeit:** lokale Branches nach Merge zu löschen ist leicht zu vergessen. Empfehlung fürs nächste Projekt: `gh pr merge --delete-branch` als Default, und am Ende des Sprints einmal `git branch --merged | grep -v main | xargs git branch -d`.
3. **Re-Review-Aufwand ist real:** wenn PO im PR Feedback gibt, kostet das Round-Trip-Zeit. In einem 60-min-Sprint ist das spürbar. Bei längeren Sprints amortisiert sich das deutlich besser.

**Wie wir Komplexität abseits von Branches managen:**
- **Aktive Out-of-Scope-Listen** in jedem Sprint-Planning-Doc — verhindert Scope-Creep
- **Definition of Done als Checklist** — keine "fast fertig"-Stories
- **Project-Board mit Filter pro Sprint** — sichtbarer Status für PO und SM
- **Memory-Dateien** für persistente Lessons (Streamlit-Falle, Test-Daten-Schutz) — kommen ins Lessons-Learned-Kapitel des Projektberichts

---

## Action Items für Sprint 5 (Tag 4)

- [ ] PR-basierten Workflow beibehalten — `feature/sprint-5-final`-Branch von `main` abzweigen
- [ ] Sprint Goal frühzeitig festlegen, bevor wir Stories ziehen (Profile + Polish + Insights — 11 offene Stories, brauchen Selektion)
- [ ] Test-DB-Setup endgültig auf `/tmp/`-Pattern festziehen, sodass kein Smoke-Test je wieder `listmate.db` anfasst (siehe Sprint-3-Vorfall mit gelöschten Test-Accounts)
- [ ] Ein Integration-Test pro Story mit `st.rerun`-Codepath, nicht nur Python-Smoke-Tests — Lesson aus PR #25
