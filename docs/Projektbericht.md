# Projektbericht: ListMate

**Gruppe Group Quest IM**
**Lehrveranstaltung:** Software Engineering Projekt — Group Quest
**Abgabedatum:** 2026-05-19
**Repository:** https://github.com/xxTAYOxx/Group_Quest_IM
**GitHub Project Board:** https://github.com/users/xxTAYOxx/projects/1

---

## Inhaltsverzeichnis

1. Projektüberblick
2. Projektidee und Tech-Stack
3. Team und Scrum-Rollen
4. Scrum-Setup (Tools, Backlog, Workflow)
5. Sprint-Verlauf
6. Retrospektive Sprint 1 + Sprint 2 (Tag 2)
7. Retrospektive Sprint 3 + Sprint 4 (Tag 3)
8. Die drei wichtigsten Lessons Learned
9. Was wir beim nächsten Projekt anders machen würden
10. Transfer auf den Data-Science-Hackathon (3. Semester)
11. Anhang: GitHub-Statistik und Evidenz

---

## 1. Projektüberblick

Unsere Gruppe hat im Rahmen der Lehrveranstaltung *Software Engineering Projekt — Group Quest* eine kollaborative Einkaufslisten-App entwickelt, die wir **ListMate** genannt haben. Die App lässt zwei oder mehr Personen gemeinsam eine Einkaufsliste pflegen, Items kategorisieren, abhaken und sehen, wer welchen Eintrag hinzugefügt hat.

Wir haben **5 Sprints** über die 4 LV-Tage durchgeführt und dabei **14 von 25 User Stories** abgeschlossen (56% des Backlogs). Alle Sprints wurden mit **null Carry-over** abgeschlossen — wir haben in jedem Sprint exakt das geschafft, was wir uns vorgenommen hatten. Die Arbeit ist über drei Pull Requests sauber im Repository nachvollziehbar dokumentiert.

Im Verlauf des Projekts haben wir die Scrum-Disziplin nicht nur formal angewendet, sondern als echtes Steuerungsinstrument für Team-Arbeit erlebt. Die wichtigsten Erkenntnisse dazu finden sich in den beiden Retrospektiven (Kapitel 6 und 7) sowie im Lessons-Learned-Kapitel.

---

## 2. Projektidee und Tech-Stack

**App-Konzept:** ListMate ist eine kollaborative Einkaufsliste. Nutzer:innen können Listen anlegen, Items mit Kategorien hinzufügen, abhaken, sowie die Listen mit anderen Team-Mitgliedern teilen. Die App ist mobil-freundlich und zeigt im geteilten Kontext, welche Person welchen Eintrag hinzugefügt hat.

**Technische Umsetzung** (gemäß LV-Vorgaben):

| Bereich | Wahl | Begründung |
|---|---|---|
| Sprache | Python 3.10+ | LV-Vorgabe |
| Frontend | Streamlit | LV-Vorgabe — Multipage-App-Struktur |
| Datenbank | SQLite | LV-Vorgabe — lokale Datei `listmate.db` |
| Passwort-Hashing | bcrypt | Sicherheitsstandard |
| Versionskontrolle | Git + GitHub | LV-Vorgabe |
| Projektmanagement | GitHub Issues + Milestones + Project v2 | LV-Vorgabe |
| Deployment | Streamlit Community Cloud | LV-Vorgabe |

Per LV-Constraint *"keine externen Services"* haben wir bewusst keine E-Mail-Benachrichtigungen, keine externen Auth-Provider und keine Cloud-Storage-Anbindung umgesetzt. Sharing erfolgt deshalb **pull-basiert**: ein eingeladener User sieht geteilte Listen im "Shared with me"-Tab.

---

## 3. Team und Scrum-Rollen

| Rolle | Person | Verantwortung |
|---|---|---|
| Product Owner | Karl Schmidt | Backlog-Pflege, Priorisierung, Sprint-Review-Abnahme |
| Scrum Master | Aloys Trinker | Facilitation der Sprint-Plannings, Reviews und Retrospektiven, Hindernisse beseitigen |
| Developer | Paul Wiedermann | Implementierung |
| Developer | Tim Sindilar | Implementierung, Repo-Pflege |
| Developer | Laetitia Weben | Implementierung |

**Stack Authority:** Das gesamte Team gemeinsam — gemäß LV-Vorgabe.

---

## 4. Scrum-Setup

### 4.1 Backlog-Struktur

Wir haben am Tag 1 einen Backlog mit **7 Features (Milestones)** und ursprünglich **24 User Stories (GitHub Issues)** aufgebaut. Im Verlauf von Sprint 5 kam eine weitere Story (US-25) hinzu, die direkt aus einem PO-Feedback im Sprint-4-Review entstand — damit umfasst der finale Backlog **25 User Stories**.

**Die 7 Features:**
- F1 Authentication & Profile
- F2 Shopping List Management
- F3 Item Management
- F4 Collaboration & Sharing
- F5 Categories & Smart Sorting
- F6 Shopping Mode
- F7 History & Insights

Jede User Story wurde:
- im *As-a-/I-want-to-/so-that-*-Format formuliert,
- mit **Acceptance Criteria** als Checkliste versehen,
- nach **T-Shirt-Größe** (XS / S / M / L / XL) geschätzt,
- nach **Priorität** (P0 / P1 / P2) markiert,
- einem **Milestone** und einem **Sprint** zugeordnet.

### 4.2 Eingesetzte Scrum-Tools

| Tool | Verwendung |
|---|---|
| GitHub Repository | Zentrale Codebasis, ein klarer Commit-Block pro Sprint |
| GitHub Milestones | 7 Features mit Fortschrittsanzeige |
| GitHub Issues | 25 User Stories mit Acceptance Criteria und Labels |
| GitHub Project v2 | Backlog-Board mit Custom Fields (Priority, T-Shirt Size, Sprint) und Status-Spalten |
| Sprint-Planning-Markdowns | Pro Sprint ein eigenes Dokument im `docs/`-Ordner mit Sprint Goal, Selected Stories und Definition of Done |
| Pull Requests (ab Sprint 3) | Sprint-Review als Diff-Review durch den Product Owner |
| Retrospektive-Markdowns | Pro Sprint-Block ein eigenes Dokument auf Deutsch |

### 4.3 Workflow pro Sprint

1. **Sprint Planning** (5 min, mit PO + SM + Devs): Sprint Goal festlegen → User Stories aus dem Backlog auswählen, die zum Goal passen → Definition of Done schriftlich fixieren.
2. **Implementation:** Ab Sprint 3 auf einem Feature-Branch (`feature/sprint-N-…`), davor direkt auf `main`.
3. **Sprint Review** (5 min, mit PO + SM + Devs): Devs zeigen das Ergebnis live oder per PR-Diff, PO gibt jede Story frei oder schickt sie zurück in den Backlog.
4. **Sprint Retrospektive** (5 min, mit SM + Devs, ohne PO): LV-spezifische Fragen beantworten, Action Items für den nächsten Sprint festhalten.

---

## 5. Sprint-Verlauf

Die folgende Tabelle gibt die Sprint-Ergebnisse im Überblick. Detaillierte Sprint-Planning-Dokumente und das Sprint-3-Review (mit Bug-Analyse) liegen im `docs/`-Ordner des Repositories.

| Sprint | Tag | Sprint Goal | Closed Stories | Done |
|---|---|---|---|---|
| **1** | 2 | "Ein User kann sich registrieren, einloggen und eine erste Shopping-Liste anlegen." | US-01, US-02, US-03, US-05, US-06 | 5 |
| **2** | 2 | "Ein User kann Items zu einer Liste hinzufügen, abhaken und löschen." | US-09, US-10, US-12 | 3 |
| **3** | 3 | "Zwei oder mehr User können dieselbe Einkaufsliste gemeinsam nutzen." | US-13, US-14, US-15 | 3 |
| **4** | 3 | "Items können kategorisiert werden, ungehakte Items erscheinen oben." | US-17, US-19 | 2 |
| **5** | 3 (vorgezogen) | "Item-Liste liest sich sauber: korrekte Ausrichtung, Attribution wer was hinzugefügt hat." | US-25 (neu) + UI-Fix | 1 |
| **Σ** | | | | **14** |

Ein Highlight des Sprint-Verlaufs ist der **Sprint-3-Review** (Pull Request #25). Der PO entdeckte im PR-Diff-Review einen subtilen Bug, der live in der Demo nicht aufgefallen wäre: `st.rerun()` wurde innerhalb eines `with sqlite3.connection`-Blocks aufgerufen, was die `INSERT`-Transaktion stillschweigend rollbackte. Wir haben den Bug auf demselben Branch gefixt und den PR erneut zum Review vorgelegt, der dann genehmigt und gemerged wurde. Diese Loop war eines der zentralen Lernerlebnisse des Projekts (siehe Kapitel 7 und 8).

---

## 6. Retrospektive Sprint 1 + Sprint 2 (Tag 2)

**Datum:** 2026-05-13 — **Anwesend** (laut LV-Vorgabe: ohne PO): Scrum Master Aloys Trinker sowie das Development Team (Paul Wiedermann, Tim Sindilar, Laetitia Weben).

### 6.1 Wo stehen wir mit unserem App-Projekt gerade?

Wir haben in zwei Sprints einen vollständig funktionsfähigen Single-User-Kern von ListMate gebaut: Registrierung mit Email + Username + bcrypt-Passwort-Hashing, Login und Logout über `st.session_state`, eine "My Lists"-Übersicht mit Erstellung neuer Shopping-Listen, sowie die List-Detail-Seite mit Add-Item-Formular, Checkbox-Ticken und Item-Löschen.

**Backlog-Stand nach Tag 2:** 8 von 24 User-Stories abgeschlossen (33%). Im GitHub-Project-Board sind alle erledigten Stories sauber als Sprint 1 bzw. Sprint 2 markiert und in der `Done`-Spalte. Die App läuft lokal unter `streamlit run app.py`, der Demo-Flow für den Sprint Review funktioniert end-to-end.

### 6.2 Wie hat uns Scrum dabei unterstützt, den aktuellen Zwischenstand zu erreichen?

- **T-Shirt-Sizing** (Planning Poker an Tag 1) hat unsere Sprint-Kapazität realistisch eingeschätzt — wir haben in beiden Sprints alle committeten Stories tatsächlich geschafft, nichts blieb übrig.
- **Klar definierte Sprint-Ziele** ("User registriert und erstellt erste Liste" / "User verwaltet Items einer Liste") haben verhindert, dass wir uns in Polish- oder Nice-to-have-Arbeit verlieren.
- **Priorisierung P0/P1/P2** hat dafür gesorgt, dass wir die Kern-User-Journey (Register → Liste → Items) vor Komfort-Features wie Profile oder Insights gebaut haben.
- **GitHub Issues mit Acceptance Criteria** haben uns bei jeder Story einen klaren "Fertig"-Begriff gegeben. Im Sprint Review wird die PO-Freigabe damit nahezu objektiv.
- **Die Definition of Done pro Sprint** im Sprint-Planning-Dokument hat uns davor bewahrt, eine Story als "fast fertig" liegen zu lassen.

### 6.3 Wo hat uns Scrum behindert?

- **Ceremonien-Overhead bei kurzen Sprints:** Planning (5 min) und Review (5 min) sind bei einem 60-min-Sprint relativ teuer im Verhältnis zur reinen Coding-Zeit. Bei längeren Sprints würde sich der Aufwand besser amortisieren.
- **Lineare Story-Bearbeitung trotz drei Devs:** Wir haben in beiden Sprints faktisch sequentiell entwickelt statt parallel, weil alle direkt auf `main` committeten und sich nicht in die Quere kommen wollten. Branches hätten parallele Arbeit ermöglicht — das wird in Tag 3 nachgeholt.
- **"Out of Scope"-Striktheit:** Manche kleinen Verbesserungen (z. B. `lists.last_updated` automatisch bei Item-Add aktualisieren) waren beim Implementieren naheliegend, gehören streng genommen aber erst in einen späteren Sprint. Wir haben pragmatisch entschieden, solche minimalen Cleanups sofort mitzunehmen — das war nicht ganz Sprint-Goal-rein.

### 6.4 Welche Scrum-Tools setzen wir aktuell ein, und funktionieren sie für uns als Gruppe?

| Tool | Verwendung | Funktioniert für uns? |
|---|---|---|
| **GitHub Repository** | Zentrale Codebasis, ein klarer Commit-Block pro Sprint | ✅ Ja, sehr gut |
| **GitHub Milestones (F1–F7)** | Feature-Gruppierung für unsere 7 Features | ✅ Ja, gibt sofort den Feature-Überblick |
| **GitHub Issues (US-01 bis US-24)** | User Stories mit Acceptance Criteria | ✅ Essenziell — ohne sie hätten wir die DoD nicht im Griff |
| **GitHub Project v2** | Backlog-Board mit Custom Fields (Priority, Size, Sprint) | ✅ Sehr gute Sichtbarkeit, Filter pro Sprint funktioniert |
| **Sprint-Planning-Markdowns** | Sprint-Goal, Selected Stories und DoD an einer Stelle | ✅ Ja, ideal für den Projektbericht |
| **`Closes #N` in Commits** | Automatisches Issue-Closing beim Push | ✅ Funktioniert tadellos |

**Was uns aktuell fehlt** (kommt in Sprint 3): Feature-Branches und Pull Requests — bisher haben wir alles direkt auf `main` committet. Tag 3 startet mit dem Branching-Megatutorial, ab Sprint 3 nutzen wir Branches.

### 6.5 Was ändern wir im nächsten Sprint, um effizienter zu arbeiten?

| Änderung | Erwartung |
|---|---|
| Feature-Branches einführen | Parallele Story-Bearbeitung möglich, unabhängige Commits |
| Pull Requests für Sprint Reviews | PO kann das Ergebnis am Diff reviewen, nicht nur live |
| Vor jedem Sprint kurzes Sync wer welche Story macht | Vermeidet Datei-Kollisionen |
| `Closes #N` in jeder Commit-Message | Automatisches Issue-Closing beim Merge |
| Sprint-Goal vor Implementierung laut vorlesen | Stellt sicher, dass wir nur Goal-relevante Stories anpacken |

---

## 7. Retrospektive Sprint 3 + Sprint 4 (Tag 3)

**Datum:** 2026-05-13 — **Anwesend** (laut LV-Vorgabe: ohne PO): Scrum Master Aloys Trinker sowie das Development Team (Paul Wiedermann, Tim Sindilar, Laetitia Weben).

### 7.1 Wo stehen wir mit unserem App-Projekt gerade?

Wir haben in vier Sprints einen funktionsfähigen End-to-End-Flow inklusive Collaboration umgesetzt. **13 von 24 User Stories** sind nach Sprint 4 geschlossen (54%):

- **Sprint 1** (Auth-Foundation): Register, Login, Logout, Liste anlegen, My-Lists-Übersicht (5 Stories)
- **Sprint 2** (Item-CRUD): Items hinzufügen, abhaken, löschen (3 Stories)
- **Sprint 3** (Sharing): Collaborator einladen, Shared-with-me-Tab, Member-Panel (3 Stories) — inklusive einer Hotfix-Iteration im Pull Request, die durch PO-Feedback entstand
- **Sprint 4** (Polish): Category-Dropdown, Unchecked-first-Sort (2 Stories) — bewusst als Mini-Sprint mit Time-Box für den Tag-3-Abschluss konzipiert

Die App ist demo-fähig: zwei Nutzer:innen können sich registrieren, eine Liste teilen, gemeinsam kategorisierte Items hinzufügen, abhaken und in einer sinnvoll sortierten Reihenfolge sehen. Das GitHub Project Board zeigt alle 13 Done-Stories sauber nach Sprints 1 bis 4 markiert.

### 7.2 Wie einfach war es, das Feedback aus der ersten Retrospektive in unsere Abläufe zu integrieren?

Aus der Tag-2-Retro hatten wir fünf konkrete Action Items. Die Bilanz fällt klar positiv aus:

| Action Item aus Retro 1 | Umsetzung in Sprint 3 + 4 | Bilanz |
|---|---|---|
| Feature-Branches einführen | `feature/sprint-3-sharing` und `feature/sprint-4-categories-sorting` | ✅ Sehr einfach, hat sich gelohnt |
| Pull Requests für Sprint Reviews | PR #25 mit Review-Loop, PR #26 mit kurzem Review | ✅ Hat einen Bug aufgedeckt, den ein Direct-to-Main-Commit verschluckt hätte |
| Vor Sprint kurzes Sync wer welche Story macht | Im Sprint-Planning-Dokument dokumentiert | ✅ Hat funktioniert, keine Datei-Kollisionen |
| `Closes #N` in Commit-Messages | Konsequent durchgezogen | ✅ Auto-Close bei Merge ist eine echte Quality-of-Life-Verbesserung |
| Sprint-Goal vor Implementation laut vorlesen | Implizit durchs Planning-Dokument | ✅ Hat uns in Sprint 4 davor bewahrt, eine out-of-scope Story mitzubauen |

**Was schwerer war als gedacht:** Die erste PR-Review-Iteration mit Hotfix (Sprint 3) hat etwa 15 zusätzliche Minuten gekostet. Aber genau dieser Schritt hat einen echten Bug abgefangen — die Zeit war also gut investiert. Außerdem ist Branch-Cleanup eine neue Disziplin-Anforderung: nach jedem Merge muss man lokal aufräumen, was anfangs leicht vergessen wird.

**Was uns leicht reingegangen ist:** Sprint-Planning-Dokumente als Markdown im Repository (`docs/sprint-0X-planning.md`) waren ein direktes Ergebnis der Tag-2-Retro und haben die Sprint-Goal-Disziplin deutlich gestärkt.

### 7.3 Wie geht ihr als Team mit dem Thema Komplexität um? Nutzt ihr aktuell Branches?

**Ja, ab Sprint 3 nutzen wir konsequent Feature-Branches und Pull Requests.** Das war eines unserer Retro-Action-Items und wir haben es direkt nach dem Tag-3-Branching-Megatutorial umgesetzt.

**Was gut funktioniert hat:**

1. **PR-Review als Sprint-Review-Artefakt:** Der PO konnte den Diff anschauen, nicht nur die Live-App. Das ist objektiver und gibt einen Audit-Trail für den Projektbericht. In PR #25 hat genau dieses Format einen Bug aufgedeckt.
2. **Saubere Sprint-Trennung:** Jeder Sprint hat seinen eigenen Branch und PR. In der Git-Historie sieht man auf einen Blick, was zu welchem Sprint gehört.
3. **`Closes #N` + Squash-Merge:** Auto-Close-Mechanik. Issues schließen automatisch beim Merge, der Pflegeaufwand sinkt.
4. **Mini-Sprint 4 mit nur zwei Stories:** Bewusst kleinere Time-Box hat funktioniert. Wir hatten Restzeit für saubere Dokumentation und Vorbereitung der Retrospektive.

**Was nicht so gut lief — unsere Lehren:**

1. **Sprint-3-Hotfix-Loop:** PR #25 enthielt einen subtilen Bug. Der `st.rerun()`-Aufruf stand innerhalb eines `with sqlite3.connection`-Blocks und hat die Transaktion implizit gerollbackt. Unser Smoke-Test umging diesen Codepath, weil er DB-Operationen direkt in Python ausführte ohne über die Streamlit-Interaktion zu gehen. **Lesson:** realistische Integration-Tests sind wichtiger als reine Unit-Smokes.
2. **Branch-Cleanup ist Disziplin-Arbeit:** lokale Branches nach dem Merge zu löschen wird leicht vergessen. Empfehlung: `gh pr merge --delete-branch` als Default, und am Sprint-Ende ein einmaliges Aufräumen.
3. **Re-Review-Aufwand ist real:** wenn der PO im PR Feedback gibt, kostet das Round-Trip-Zeit. Im 60-min-Sprint spürbar; bei längeren Sprints amortisiert es sich.

**Wie wir Komplexität abseits von Branches managen:**
- Aktive Out-of-Scope-Listen in jedem Sprint-Planning verhindern Scope-Creep.
- Definition of Done als Checkliste — keine "fast fertig"-Stories.
- Project Board mit Filter pro Sprint — sichtbarer Status für PO und SM.
- Persistente Lessons-Learned-Notizen für technische Fallen wie die `st.rerun`-im-`with`-Block-Falle.

---

## 8. Die drei wichtigsten Lessons Learned

Wenn wir auf die fünf Sprints zurückblicken, gibt es drei Erkenntnisse, die für uns als Team am wertvollsten waren — und alle drei haben weniger mit Technik zu tun als mit der Art, wie wir miteinander gearbeitet haben.

### 8.1 T-Shirt-Sizing macht Sprint-Kapazität verhandelbar statt geraten

Am ersten Tag haben wir alle User Stories nach Größen geschätzt — XS, S, M, L, XL. Das hat erst banal gewirkt, war aber eines der wichtigsten Tools im ganzen Projekt. Vor jedem Sprint konnten wir mit einem Blick entscheiden, was realistisch in die verfügbare Zeit passt.

Das Ergebnis: über alle fünf Sprints hatten wir **kein einziges Carry-over**. Wir haben in jedem Sprint exakt das geschafft, was wir uns vorgenommen hatten. Das war kein Zufall — das war die Disziplin, sich nicht zu überfordern, und der Mut, eine Story aus dem Sprint herauszuhalten, wenn die Kapazität es nicht hergibt. Scrum ist erst dann wirksam, wenn man auch "Nein" zu Stories sagen kann, die nicht reinpassen.

### 8.2 Retrospektiven sind das Herz von Scrum, nicht Pflicht-Theater

Wir haben pro Sprint-Block eine Retrospektive geschrieben — drei insgesamt. Und jede einzelne hat unsere Arbeitsweise im nächsten Sprint konkret verändert.

Nach der ersten Retrospektive haben wir Feature-Branches eingeführt. Nach der zweiten haben wir vereinbart, dass Tests niemals die echte Datenbank anfassen dürfen. Nach der dritten haben wir vor jedem Sprint einen kurzen "Confidence-Check" eingeführt, um nur Stories anzunehmen, bei denen wir uns wirklich sicher waren.

Eine Retrospektive ist nur dann wertvoll, wenn aus ihr Action Items entstehen, die im nächsten Sprint wirklich umgesetzt werden. Bei uns war das jedes Mal so. Und genau deshalb haben sich unsere Sprints im Laufe des Projekts sichtbar verbessert.

### 8.3 Feature-Branches und Pull Requests schaffen Vertrauen im Team

Bis Sprint 2 haben wir alles direkt auf den Hauptzweig committet. Das hat funktioniert, aber wir hatten ständig das Gefühl, uns gegenseitig auf die Füße zu treten — niemand wollte derjenige sein, der den Build kaputt macht. Ab Sprint 3 hat jedes Sprint-Ergebnis einen eigenen Branch und einen Pull Request bekommen.

Plötzlich konnten alle parallel arbeiten ohne Angst. Und der Product Owner konnte den Sprint Review nicht nur am Live-Bildschirm sondern auch am Code-Diff machen — was sogar einen Bug aufgedeckt hat, der uns sonst erst in der Final-Demo um die Ohren geflogen wäre. Pull Requests sind nicht nur ein Werkzeug — sie sind ein Vertrauens-Mechanismus, der das Team produktiver und entspannter gemacht hat.

---

## 9. Was wir beim nächsten Projekt anders machen würden

Wir würden nicht alles anders machen — vieles hat funktioniert. Aber drei Dinge nehmen wir uns für das nächste Mal konkret vor.

### 9.1 Den Pull-Request-Workflow von Sprint 1 an nutzen

Das Branching-Megatutorial der LV kam erst am Tag 3, und wir haben uns daran gehalten. Aber rückblickend hätten wir früher starten können. Hätten wir auch in Sprint 1 und 2 schon Pull Requests gemacht, hätten wir wahrscheinlich Probleme früher entdeckt und uns schneller an "kleinere, fokussiertere Commits" gewöhnt. Branches einzuführen ist keine technische Hürde, sondern eine Team-Vereinbarung — und die hätten wir einfach von Anfang an treffen können.

### 9.2 Die Scrum-Rollen mittendrin rotieren lassen

Wir hatten fixe Rollen über das ganze Projekt — ein Product Owner, ein Scrum Master, drei Developer. Das war pragmatisch, aber es heißt auch, dass nur eine Person Sprint Plannings moderiert hat, nur eine die Retrospektiven geleitet hat, nur eine den Backlog gepflegt hat. Beim nächsten Mal würden wir die Rollen mindestens einmal in der Mitte tauschen, damit jeder im Team die Erfahrung macht, was diese Verantwortung wirklich bedeutet. Das ist auch realistischer für die Praxis, wo Rollen in Teams öfter wechseln.

### 9.3 Daily Stand-ups einführen, auch in einem kurzen Projekt

Wir haben uns vor jedem Sprint kurz synchronisiert, aber nicht jeden Tag und nicht innerhalb eines Sprints. Bei einem mehrtägigen Projekt mit Pausen dazwischen wäre ein 5-Minuten-Stand-up zu Tagesbeginn Gold wert gewesen: "Was hat jeder heute vor?", "Wo hängt's?", "Wer braucht Unterstützung?". Diese drei Fragen hätten uns Sync-Reibung erspart und das Team-Gefühl noch verstärkt.

---

## 10. Transfer auf den Data-Science-Hackathon (3. Semester)

Der Hackathon im 3. Semester ist die nächste echte Bewährungsprobe für alles, was wir hier gelernt haben. Unser Plan ist, die Scrum-Disziplin eins zu eins zu übertragen.

### 10.1 Wir behandeln ML-Experimente wie User Stories

Statt einer langen Brainstorming-Liste an "Ideen, die wir ausprobieren könnten" formulieren wir jede Experiment-Idee als Story: *"Als Analyst:in möchte ich ein Baseline-Modell mit Logistic Regression, damit wir eine Referenz-Genauigkeit haben."* Das zwingt uns, vor dem Code-Schreiben zu klären, **warum** wir das Experiment machen und **wie** wir Erfolg messen. Das ist die wichtigste Übertragung aus diesem Projekt.

### 10.2 Wir verteilen Rollen klar — auch in einem Daten-Projekt

Hackathons gehen oft kaputt, weil alle gleichzeitig alles probieren. Wir nehmen mit: jemand übernimmt die Product-Owner-Rolle und priorisiert, welche Modelle gebaut werden. Jemand übernimmt die Scrum-Master-Rolle und stellt sicher, dass wir uns nicht in endlosem Tuning verlieren. Die anderen arbeiten parallel an Modellen — jede:r mit einem eigenen Sprint-Goal.

### 10.3 Wir machen tägliche Mini-Retrospektiven am Abend

Fünf Minuten am Ende jedes Hackathon-Tags: Was hat geklappt? Was nicht? Was machen wir morgen anders? Genau das hat uns in diesem Projekt geholfen, mit jedem Sprint besser zu werden. Im Hackathon — mit weniger Zeit und mehr Druck — ist das noch wichtiger als hier.

### 10.4 Wir setzen Sprint-Goals statt einer Wunschliste

*"Heute Baseline mit über 70 % Accuracy"* ist ein Sprint-Goal. *"Heute fünf Modelle ausprobieren"* ist eine Wunschliste. Die LV hat uns gezeigt, dass ein einziges klares Ziel ein ganzes Team fokussiert — und genauso werden wir es im Hackathon angehen.

---

## 11. Anhang: GitHub-Statistik und Evidenz

### 11.1 Quantitative Zusammenfassung

| Metrik | Wert |
|---|---|
| Sprints durchgeführt | 5 |
| User Stories im Backlog | 25 (eine zusätzliche Story US-25 wurde während Sprint 5 in Reaktion auf PO-Feedback ergänzt) |
| User Stories geschlossen | 14 / 25 (56%) |
| Features (Milestones) | 7 — davon vollständig oder teilweise umgesetzt: F1, F2, F3, F4, F5 |
| Pull Requests gemerged | 3 (PR #25 Sprint 3, PR #26 Sprint 4, PR #28 Sprint 5) |
| Bugs durch PR-Review gefangen | 2 |
| Retrospektiven dokumentiert | 3 (Tag 2 mit 5 LV-Fragen, Tag 3 mit 3 LV-Fragen, plus eine Abschluss-Retro nach Sprint 5) |
| Carry-over über alle Sprints | 0 |

### 11.2 Links zur Evidenz

- **Repository:** https://github.com/xxTAYOxx/Group_Quest_IM
- **GitHub Project Board (Backlog):** https://github.com/users/xxTAYOxx/projects/1
- **Milestones (Features):** https://github.com/xxTAYOxx/Group_Quest_IM/milestones
- **Sprint-3 Pull Request (mit Hotfix-Loop):** https://github.com/xxTAYOxx/Group_Quest_IM/pull/25
- **Sprint-4 Pull Request:** https://github.com/xxTAYOxx/Group_Quest_IM/pull/26
- **Sprint-5 Pull Request:** https://github.com/xxTAYOxx/Group_Quest_IM/pull/28

### 11.3 Verzeichnis der projektrelevanten Dokumente im Repository

```
docs/
├── sprint-01-planning.md        Sprint Goal + DoD + Selected Stories
├── sprint-02-planning.md
├── sprint-03-planning.md
├── sprint-03-review.md          Sprint-Review-Doku inkl. Bug-Analyse
├── sprint-04-planning.md
├── sprint-05-planning.md
├── retrospective-sprint-01-02.md  (5 LV-Fragen, deutsch)
├── retrospective-sprint-03-04.md  (3 LV-Fragen, deutsch)
├── retrospective-sprint-04-05.md  (Abschluss-Retro nach Sprint 5)
├── final-presentation.md         Speaker-Skript für die finale Präsentation
└── github-presentation-guide.md  Demo-Pfad durch das GitHub-Setup
```

### 11.4 Lokale Inbetriebnahme der App

```bash
git clone https://github.com/xxTAYOxx/Group_Quest_IM.git
cd Group_Quest_IM
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
# Öffnet http://localhost:8501
```

---

*Ende des Projektberichts.*
