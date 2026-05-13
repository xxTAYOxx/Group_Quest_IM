# Retrospektive: Sprint 4 + Sprint 5 (Abschluss-Retro)

**Datum:** 2026-05-13
**Projekt:** ListMate (Group Quest)
**Anwesend (laut LV-Vorgabe: ohne PO):**
- Scrum Master: Aloys Trinker
- Development Team: Paul Wiedermann, Tim Sindilar, Laetitia Weben

*Hinweis: Sprint 4 wurde bereits in der Tag-3-Retrospektive zusammen mit Sprint 3 reflektiert (`docs/retrospective-sprint-03-04.md`). Diese Abschluss-Retro ergänzt diese um Sprint-5-spezifische Erkenntnisse und zieht die Gesamtbilanz vor der finalen Präsentation.*

---

## 1. Wo stehen wir mit unserem App-Projekt gerade?

Wir haben **5 Sprints abgeschlossen** und **14 von 25 User-Stories** (56%) geclosed:

- **Sprint 1** (Auth-Foundation): 5 Stories – Register/Login/Logout, Create List, My Lists
- **Sprint 2** (Item-CRUD): 3 Stories – Add/Check-off/Delete Items
- **Sprint 3** (Sharing): 3 Stories – Invite Collaborator, Shared-with-me-Tab, Member-Panel (inkl. einer Hotfix-Iteration via PR-Review)
- **Sprint 4** (Polish): 2 Stories – Category-Dropdown, Unchecked-first-Sort
- **Sprint 5** (Final Polish): 1 neue Story + 1 UX-Bugfix – Added-by-Attribution für shared Listen, Item-Row-Vertical-Alignment

Während Sprint 5 haben wir eine **neue Story angelegt (US-25 "Show added-by user")** in direkter Reaktion auf PO-Feedback aus dem Sprint-4-Review – damit ist unser Backlog auf 25 Stories gewachsen. Die App ist End-to-End demo-fähig: zwei User können sich registrieren, eine Liste teilen, gemeinsam kategorisierte Items hinzufügen, sehen wer was hinzugefügt hat, abhaken in einer sinnvollen Reihenfolge.

**Was nicht gemacht wurde (11 offene Stories, bewusst dokumentiert):**
- US-11 Edit-Item (gezielt in Sprint 5 als nicht-100%-sicher klassifiziert und ans Backlog zurückgegeben)
- US-04 Profile, US-07 Rename, US-08 Delete-List, US-16 Remove-Collaborator, US-18 Group-by-Category, US-20 Shopping-Mode, US-21 Undo, US-22-24 Insights/Autocomplete

---

## 2. Wie einfach war es, das Feedback aus der letzten Retrospektive in unsere Abläufe zu integrieren?

Aus der Tag-3-Retro hatten wir vier konkrete Action Items. Bilanz:

| Action Item aus Retro 3+4 | Sprint 5 | Bilanz |
|---|---|---|
| PR-basierten Workflow beibehalten | `feature/sprint-5-final` mit PR #28 | ✅ Reibungslos, hat sich als unser bester Workflow-Schritt etabliert |
| Sprint Goal früh festlegen | Sprint Goal "Items list reads cleanly in shared contexts" wurde vor Story-Auswahl formuliert | ✅ Hat geholfen, das deutlich zu schärfen, was rein gehört |
| Test-DB-Setup auf `/tmp/`-Pattern festziehen | Sprint-5-Smoke-Test nutzte `/tmp/listmate_sprint5_test.db`, `listmate.db` blieb unangetastet | ✅ Lesson aus dem Vorfall mit gelöschten Test-Accounts erfolgreich umgesetzt |
| Integration-Tests mit echtem `st.rerun`-Codepath | **Nicht umgesetzt** – wir haben weiterhin Python-Smoke-Tests genutzt, die den UI-Pfad umgehen | ❌ In der Restzeit nicht mehr realistisch. Für die UI-Alignment-Fix gab es schlicht keinen Smoke-Test möglich – das musste manuell geprüft werden. |

**Was besonders gut lief in Sprint 5:**
- Die **Confidence-Check-Conversation** vor Sprint-Start (UI-Fix 100% / Added-By 100% / Edit-Item 95%) war ein neues Format und hat direkt eine Scope-Entscheidung ausgelöst: Edit-Item ans Backlog statt unsicher reinpushen. Das ist Scrum-Disziplin in Reinform.
- **Story mid-sprint anlegen**: US-25 wurde nicht-existierend in den Sprint geholt, sondern offiziell als Issue angelegt + ins Project geschoben + dann implementiert. Backlog-Hygiene bis zum Schluss.

**Was schwierig blieb:**
- UI-Bugs sind schlecht testbar mit unserem aktuellen Smoke-Test-Setup. Das `vertical_alignment="center"` ist über Streamlit-Docs verifiziert, aber nicht über einen automatischen Test abgesichert. Lesson: für reine Visual-Polish-Stories bräuchte man entweder visuelle Regression-Tests oder einen separaten manuellen Check-Pass durch PO.

---

## 3. Wie geht ihr als Team mit dem Thema Komplexität um? Nutzt ihr aktuell Branches?

**Ja, weiterhin Feature-Branches + PRs ab Sprint 3.** Über 3 Sprints mit PR-Workflow haben wir konkrete Erkenntnisse gesammelt:

### Was hat in Sprint 5 besonders gut funktioniert:

1. **Confidence-Gating als neuer Komplexitäts-Filter:** Statt "wir versuchen es einfach" haben wir vor Sprint 5 explizit per Story bewertet, wie sicher wir uns sind. Eine Story bei ~95% (Edit-Item mit `st.dialog`) wurde ans Backlog zurückgegeben – das ist im Scrum-Lehrbuch genau richtig, wurde aber zum ersten Mal so explizit gemacht.
2. **Mini-Sprint mit konzentriertem Scope:** Sprint 5 hatte effektiv 2 Items (US-25 + UI-Fix). Das hat uns Zeit für saubere Doku, gründlichen Smoke-Test und mehrfachen visuellen Re-Check gegeben.
3. **Saubere Verzweigung der DB-Test-Pfade:** `/tmp/listmate_sprint5_test.db` statt `listmate.db` – Production-Daten (echte Test-Accounts) waren strikt geschützt.

### Was nicht so gut lief / unsere finalen Lehren:

1. **Wir hatten in Sprint 4 *noch* einen Bug**, der erst in Sprint 5 vom PO entdeckt wurde: die Item-Row-Alignment (Checkbox/Text/🗑️ auf verschiedenen Höhen). Lesson: PRs sollten auch UX-Polish-Stichproben durch den PO triggern, nicht nur Funktions-Demos.
2. **Branches haben einen "Cleanup"-Overhead:** über 3 PRs hinweg mussten wir nach jedem Merge manuell `git checkout main && git pull && git branch -D feature/...` machen. `gh pr merge --squash --delete-branch` automatisiert den Remote-Teil, lokal ist es zusätzliche Disziplin.
3. **Integration-Tests bleiben ein offenes Item:** wir haben den Streamlit-SQLite-Bug aus Sprint 3 nachvollzogen und dokumentiert, aber wir haben in Sprint 4+5 nicht angefangen, Integration-Tests einzuführen, die solche Fallen automatisch fangen würden. Bewusst priorisiert: Doku-Qualität ging vor Test-Infrastruktur, gegeben die LV-Restzeit.

### Wie wir Komplexität insgesamt managen (Synthese aller 5 Sprints):

| Mechanismus | Status |
|---|---|
| Backlog mit T-Shirt-Sizes + P0/P1/P2 | ✅ konsequent durchgezogen |
| Sprint-Planning-Doc pro Sprint mit Goal + Out-of-Scope | ✅ alle 5 Sprints |
| Feature-Branches + PRs mit `Closes #N` | ✅ ab Sprint 3 |
| GitHub Project Board mit Custom Fields (Priority, Size, Sprint) | ✅ alle 25 Stories darin |
| Sprint Reviews als PR-Diff-Reviews | ✅ ab Sprint 3 |
| Definition of Done in jeder Planning | ✅ alle 5 Sprints |
| Lessons-Learned in Memory-Dateien | ✅ 3 persistente Notizen |
| Realistic Integration-Tests | ❌ offen – Backlog für Folge-Projekt |
| Schema-Migrationen versioniert | ❌ offen – `CREATE TABLE IF NOT EXISTS` reichte für 4 Tage |

---

## Action Items für die finale Präsentation und das Projektbericht

- [ ] Final Presentation auf Sprint 5 + finale Zahlen aktualisieren (14/25 Stories closed)
- [ ] In den "Lessons Learned" der Präsentation ein viertes Item aufnehmen: **Confidence-Gating vor Sprint-Start** als Scrum-Disziplin-Mechanik
- [ ] In "Was wir nächstes Mal anders machen": Integration-Tests + Visual-Regression als ungelöstes Thema explizit benennen
- [ ] Dokumentation und Memory-Notizen sind das, was die nächste Studierenden-Kohorte vom Projekt erbt — sie sind im Repo `docs/`-Ordner permanent
- [ ] **Im Projektbericht** beide Retrospektiven (Tag 2: 5 Fragen / Tag 3: 3 Fragen / diese Abschluss-Retro: gleiche 3 Fragen adaptiert) als Anhang aufnehmen
