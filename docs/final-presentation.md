# Finale Präsentation — ListMate (Speaker Notes)

**Team:** Karl Schmidt (PO) · Aloys Trinker (SM) · Paul Wiedermann · Tim Sindilar · Laetitia Weben
**Repo:** https://github.com/xxTAYOxx/Group_Quest_IM
**Project Board:** https://github.com/users/xxTAYOxx/projects/1
**Time Budget:** max. 10 min pro Gruppe

Die Reihenfolge folgt den 4 LV-Pflichtpunkten aus der Aufgabenstellung. Jede Sektion hat einen *Speaker-Notes-Block* (was sagen) und einen *Slide-Content-Block* (was zeigen).

---

## Punkt 1: Wie schaut eure finale App aus

### Slide-Content
- App-Name: **ListMate** — kollaborative Einkaufsliste in Streamlit + SQLite
- Screenshots (vor Demo aufnehmen):
  1. Login/Register-Tab
  2. My-Lists-Page mit zwei Tabs (My Lists + Shared with me)
  3. List-Detail mit Add-Item-Form (Category-Dropdown sichtbar)
  4. List-Detail mit Items teils abgehakt (Unchecked-first-Sort sichtbar)
  5. Sidebar Member-Panel + Invite-Form (als Owner)
- Falls Live-Demo: Backup-Screenshots trotzdem dabei haben

### Speaker Notes (≈ 3 min)
> "ListMate ist eine kollaborative Einkaufslisten-App, gebaut in Python mit Streamlit als Frontend und SQLite als Backend — keine externen Services, vollständig im Streamlit-Cloud-Deployment-Modell.
>
> **Demo-Pfad:** Ich registriere zwei Test-Accounts. Mit dem ersten Account erstelle ich eine Liste *Groceries Tuesday*. Ich lade den zweiten Account ein. Mit dem zweiten logge ich mich ein und sehe die Liste sofort im *Shared with me*-Tab. Wir fügen gemeinsam Items hinzu — mit Kategorie-Dropdown — und haken einige ab. Die App sortiert automatisch: abgehakte Items rutschen ans Ende, ungehakte bleiben oben.
>
> Insgesamt sind **13 von 24 User-Stories** abgeschlossen — der vollständige End-to-End-Flow inkl. Sharing funktioniert. Den GitHub-Project-Board-Screenshot zeigen wir am Ende — saubere Sprint-Spalten, alle 4 durchgeführten Sprints sauber dokumentiert."

---

## Punkt 2: Die 3 wichtigsten Lessons Learned

### Slide-Content (eine Slide pro Lesson)

#### Lesson 1: **PR-basierte Sprint Reviews fangen Bugs, die direkter `git push` versteckt.**
- Konkretes Beispiel: PR #25 (Sprint 3, *Invite Collaborator*)
- Symptom in der Demo: Owner lädt User ein → keine Rückmeldung sichtbar → Eingeladener sieht die Liste nicht
- Root Cause: `st.rerun()` innerhalb `with sqlite3.connection`-Block → Streamlit's RerunException rollt die Transaktion zurück, kein sichtbarer Fehler
- Ohne PR-Diff-Review hätten wir das erst in der Final-Demo gesehen
- Vollständig dokumentiert in `docs/sprint-03-review.md` mit Reproduktions-Test

#### Lesson 2: **T-Shirt-Sizing + klare Sprint-Goals = realistische Velocity.**
- Wir haben in **allen 4 Sprints** alle committeden Stories geschafft, kein Carry-over
- Planning Poker hat Capacity realistisch eingeschätzt
- Strict "Out of Scope"-Listen pro Sprint haben Scope-Creep verhindert
- Mini-Sprint 4 (nur 2 Stories) war eine **bewusste Time-Box-Entscheidung** — Disziplin statt "noch eine Story dazu"

#### Lesson 3: **Streamlit + SQLite hat versteckte Anti-Pattern.**
- Concrete: `st.rerun()` darf niemals in einem `with conn:`-Block stehen
- Reine Python-Smoke-Tests fangen das nicht — der RerunException-Codepath kommt nur durch echte Streamlit-Interaktion
- → Realistische Integration-Tests sind nötig, nicht nur Unit-Tests
- Speichern wir als persistente Memory-Notiz für Folgeprojekte

### Speaker Notes (≈ 3 min, ~1 min pro Lesson)
> "Drei Lessons. Erstens: PR-basierte Reviews sind ihr Gewicht in Gold wert. Wir haben in Sprint 3 mit Feature-Branches angefangen — der allererste PR hat einen Bug aufgedeckt, den wir mit Direct-to-Main-Commits sicher übersehen hätten. Konkret war es ein Streamlit-SQLite-Anti-Pattern: `st.rerun()` in einem Datenbank-Context-Manager rollt die Transaktion zurück.
>
> Zweitens: T-Shirt-Sizing funktioniert. Wir haben in jedem unserer 4 Sprints exakt das geschafft, was wir uns vorgenommen haben. Null Carry-over. Das war kein Zufall, das war Planning Poker am Tag 1 plus die Disziplin, die Out-of-Scope-Liste ernst zu nehmen.
>
> Drittens: das technische Lesson Learned, das wir oben schon angerissen haben — Streamlit + SQLite haben Fallen, die nur in echten Use-Pfaden auftauchen. Reine Python-Smoke-Tests reichen nicht. Integration-Tests, die den echten UI-Codepath durchspielen, sind nötig."

---

## Punkt 3: Was würdet ihr beim nächsten Projekt anders machen

### Slide-Content
1. **PR-Workflow von Sprint 1 an, nicht erst ab Sprint 3** — das Branching-Megatutorial der LV kam erst Tag 3, aber wir hätten von Anfang an Branches nutzen können. Vermutlich hätten wir auch in Sprint 1 oder 2 Bugs gefunden, die wir sonst durchgeschleift haben.
2. **Integration-Tests statt nur Python-Smoke** — der Sprint-3-Bug war nicht in unseren Smoke-Tests sichtbar, weil sie den `st.rerun`-Codepath umgangen haben. Beim nächsten Mal: mindestens ein E2E-Test pro Story mit echter Streamlit-Interaktion (z. B. via `streamlit-testing`-Library).
3. **Schema-Migrationen versionieren** — wir haben `CREATE TABLE IF NOT EXISTS` für alle Schema-Änderungen genutzt. Das ist OK für ein 4-Tage-Projekt, aber bei mehr Sprints oder echten Production-DBs muss man Migrations-Dateien (`0001_initial.sql`, `0002_add_collaborators.sql`, ...) versionieren — sonst weiß man irgendwann nicht mehr, welches Schema in welchem Sprint dazukam.
4. **Test-Daten und Production-DB sauber trennen** — wir hatten einen Vorfall, wo ein Smoke-Test die `listmate.db` (mit echten Test-Accounts des PO) gelöscht hat. Beim nächsten Projekt: Test-DB immer in `/tmp/` oder via Environment-Variable, niemals dieselbe Datei wie die Dev-DB.

### Speaker Notes (≈ 1.5 min)
> "Vier Dinge anders. Branching-Workflow von Anfang an. Integration-Tests die den echten UI-Pfad durchspielen, nicht nur Python-Funktionen. Schema-Migrationen versionieren. Und — kleines Trauma — Test-Daten strikt getrennt von der Dev-DB halten. Dazu kommt noch eine generelle Erkenntnis: kürzere, fokussiertere Sprints (wie unser Mini-Sprint 4) waren angenehmer und produktiver als die ambitionierteren 4-Story-Sprints."

---

## Punkt 4: Wie könnt ihr eure Lessons-Learned beim Data-Science-Hackathon im 3. Semester nutzen

### Slide-Content
- **Backlog-Disziplin auch für ML-Aufgaben:** User Stories nicht nur für Features, sondern für Daten-Aufgaben (`As an analyst, I want to ... so that ...`) — schärft die Frage *"warum macht das Modell das?"*
- **T-Shirt-Sizing für ML-Experimente:** Hyperparameter-Tuning XL, Baseline-Modell M, Feature-Engineering S — gleiche Logik, andere Domain
- **Branching pro Experiment:** `feature/baseline-logreg`, `feature/xgboost-tuning`, `feature/cnn-arch-v2` — ermöglicht parallel laufende Experimente ohne Konflikte, mit klaren PRs für Modell-Vergleich
- **Project Board mit Status-Spalten:** *To Try* / *Running* / *Validated* — Sichtbarkeit für ganzes Team, kein "wer trainiert gerade was?"
- **Sprint-Goals fokussieren:** "Heute kein Hyperparameter-Tuning, heute nur Feature-Selection" — verhindert das klassische ML-Hackathon-Antipattern, gleichzeitig 5 Dinge zu probieren
- **Streamlit für Demo-Layer:** wir können den Stack direkt wiederverwenden — Streamlit-App als Dashboard für die Hackathon-Final-Präsentation, SQLite für Result-Tracking
- **Lessons-Learned-Doku pro Tag:** kurze tägliche Retros analog zu unserer Tag-2 + Tag-3-Retro — kostet 5 Minuten, spart Stunden in der Final-Doku

### Speaker Notes (≈ 2 min)
> "Der Data-Science-Hackathon im 3. Semester ist die direkte Bewährungsprobe für alles, was wir hier gelernt haben. Konkret:
>
> Scrum-Disziplin überträgt sich 1:1. ML-Experimente sind User Stories. Hyperparameter-Tuning kriegt eine T-Shirt-Size. Jedes Modell oder Experiment ist ein eigener Branch — das gibt uns parallele Pfade ohne Konflikt, und am Ende sehen wir im PR-Diff genau, was sich verändert hat.
>
> Das Streamlit-Frontend können wir **direkt wiederverwenden** — Hackathon-Demos brauchen eine UI, und wir haben gerade gelernt, wie man eine baut. SQLite als leichtgewichtiges Tracking-Backend funktioniert für Run-Logs genauso gut wie für Shopping-Listen.
>
> Und das vielleicht Wichtigste: **kurze Retros pro Tag** — wir haben heute zwei Retros geschrieben und werden sie ins Projektbericht-Kapitel übernehmen. Das Format funktioniert. Das nehmen wir 1:1 mit in den Hackathon."

---

## Backup: kurze App-Statistik für etwaige Fragen aus dem Plenum

| Metrik | Wert |
|---|---|
| Sprints durchgeführt | **5** (Tag 1: Planung · Tag 2: Sprint 1+2 · Tag 3: Sprint 3+4+5) |
| User Stories closed | **14 / 25** (56%) — eine zusätzliche Story (US-25) wurde während Sprint 5 angelegt + abgeschlossen |
| Features (Milestones) berührt | 5 von 7 (F1, F2, F3, F4, F5) |
| Pull Requests gemerged | **3** (PR #25 Sprint 3 · PR #26 Sprint 4 · PR #28 Sprint 5) |
| Bugs im PR-Review gefangen | **2** (Sprint 3: RerunException-Rollback bei Invite · Sprint 5: Item-Row-Alignment war von PO im Sprint-4-Review entdeckt) |
| Retrospektiven dokumentiert | **3** (Tag 2: 5 LV-Fragen · Tag 3: 3 LV-Fragen · Abschluss: 3 LV-Fragen adaptiert — alle auf Deutsch fürs Projektbericht) |
| Lines of Code (App-Files) | ~650 (app.py + db.py + auth.py + 2 pages + schema.sql) |
| Backlog-Stories offen | **11** (bewusst dokumentiert, kein Carry-over-Versagen): US-04 · US-07 · US-08 · US-11 · US-16 · US-18 · US-20 · US-21 · US-22 · US-23 · US-24 |

### Erweitertes Lessons-Learned-Set (Bonus 4: Confidence-Gating)

Falls im Plenum Zeit ist, kurz nennen:

> **Confidence-Gating vor Sprint-Start:** Vor Sprint 5 hat das Team explizit pro Story den Implementierungs-Confidence-Level bewertet (UI-Fix 100% / Added-By 100% / Edit-Item ~95%). Die einzige Story unter 100% (Edit-Item) wurde aktiv ans Backlog zurückgegeben statt sie hoffnungs-getrieben mitzuziehen. Das ist Scrum-Risiko-Management auf Story-Ebene und hat uns davor bewahrt, einen subtilen Bug in den finalen Sprint einzuschleppen.
