# GitHub-Präsentations-Guide

Eine 2-Minuten-Demo durch das GitHub-Setup, falls die Jury den Scrum-Workflow sehen will (oder als Backup, wenn die Live-App-Demo nicht startet).

> **Tipp vor der Präsi:** Öffne alle vier Tabs unten **vorher** im Browser, dann musst du live nur zwischen Tabs springen.

---

## Vorbereitung: vier Tabs offen lassen

| Tab | URL | Was darauf zu sehen |
|---|---|---|
| 1 | https://github.com/users/xxTAYOxx/projects/1 | Project Board mit allen 25 Stories, sortiert nach Sprint |
| 2 | https://github.com/xxTAYOxx/Group_Quest_IM/milestones | 7 Features mit Done/Open-Balken |
| 3 | https://github.com/xxTAYOxx/Group_Quest_IM/pulls?q=is%3Apr+is%3Aclosed | 3 gemergte Sprint-PRs |
| 4 | https://github.com/xxTAYOxx/Group_Quest_IM/tree/main/docs | docs/-Ordner mit allen Scrum-Artefakten |

---

## Der Erzähl-Pfad (2 Minuten, 5 Stationen)

### Station 1 — Project Board (Tab 1) — ~30 Sek
**Klicke:** [github.com/users/xxTAYOxx/projects/1](https://github.com/users/xxTAYOxx/projects/1)

**Sag:**
> *"Das hier ist unser zentrales Scrum-Tool: 25 User Stories, sauber organisiert. Jede Karte hat Sprint, Priority und T-Shirt Size als Custom Fields — so haben wir vor jedem Sprint entschieden, was reinpasst."*

**Zeig kurz:**
- Status-Spalten **Todo / In Progress / Done** — 14 Stories sind in Done
- Filter/Gruppieren nach `Sprint` (oben rechts auf das Filter-Icon klicken, dann "Group by: Sprint") — visualisiert wie sauber sich die Arbeit auf 5 Sprints verteilt hat

### Station 2 — Closed Issue als Beispiel (1 Klick weiter) — ~30 Sek
**Klicke** im Board auf eine Done-Karte, z. B. **US-13 (Invite collaborator)** oder **US-01 (Register)**.

**Sag:**
> *"Jede Story hat den 'As a … I want … so that …'-Aufbau, klare Acceptance Criteria und eine Definition of Done. Beides ist abgehakt — die Story wurde im Sprint Review vom Product Owner formal abgenommen."*

**Zeig:**
- Title im User-Story-Format
- Acceptance Criteria — alle abgehakt ✓
- Definition of Done — alle abgehakt ✓
- Labels: `feature`, `P0`, `size:M` (oder ähnlich)
- Milestone: `F1 - Authentication & Profile`
- Unten: `Closed by PR #25` oder ähnlich → **direkter Sprung zum Sprint Review**

### Station 3 — Pull Requests (Tab 3) — ~30 Sek
**Klicke** auf [PR #25 "Sprint 3 — Sharing & Collaboration"](https://github.com/xxTAYOxx/Group_Quest_IM/pull/25).

**Sag:**
> *"Ab Sprint 3 haben wir mit Pull Requests gearbeitet. Das ist unser Sprint-Review-Artefakt — der Product Owner hat hier nicht nur die App live gesehen, sondern auch den Code-Diff geprüft. Genau in diesem PR hat er einen Bug entdeckt, den wir auf demselben Branch gefixt haben, bevor wir gemerged haben."*

**Zeig:**
- PR-Description mit `Closes #13`, `#14`, `#15`
- 2 Commits sichtbar: erst `feat(sprint-3)…`, dann `fix(sprint-3)…` (der Hotfix nach PO-Feedback)
- "Merged" Label
- Linked Issues, die durchgestrichen erscheinen weil geschlossen

### Station 4 — Milestones (Tab 2) — ~20 Sek
**Klicke:** [github.com/xxTAYOxx/Group_Quest_IM/milestones](https://github.com/xxTAYOxx/Group_Quest_IM/milestones)

**Sag:**
> *"Unsere 7 Features sind GitHub Milestones. Ein Blick zeigt, wo wir stehen — bei Sharing zum Beispiel 4 von 5 Stories done."*

**Zeig:**
- Progress-Balken pro Feature
- F4 (Sharing): 80% (4/5 done)
- F1, F3: ~75%
- F6, F7: 0% — diese Features sind im Backlog, nicht zu Ende gebracht — **bewusst priorisiert**

### Station 5 — docs/-Ordner (Tab 4) — ~20 Sek
**Klicke:** [github.com/xxTAYOxx/Group_Quest_IM/tree/main/docs](https://github.com/xxTAYOxx/Group_Quest_IM/tree/main/docs)

**Sag:**
> *"Alle Scrum-Artefakte sind im Repo dokumentiert: 5 Sprint-Plannings, 1 Sprint-Review mit Bug-Analyse, 3 Retrospektiven auf Deutsch, und diese finale Präsentation. Das ist der Anhang für unseren Projektbericht — alles wiederverwendbar."*

**Zeig:**
- Liste der ~10 Markdown-Dateien
- Optional: kurz `retrospective-sprint-01-02.md` öffnen → die 5 LV-Fragen mit Antworten

---

## Was du **nicht** zeigen musst (aber als Backup parat)

- **Issues-Tab** mit allen 25: ist redundant mit Project Board und Milestones
- **Code-Tab** und einzelne `.py`-Dateien: nicht Scrum-relevant, lieber in der App-Demo
- **Commit-Historie**: nett aber nicht nötig — die 3 PRs reichen als Sprint-Evidenz

---

## Wenn dich jemand was fragt

| Frage aus dem Plenum | Kurzantwort + welcher Tab darauf zeigt |
|---|---|
| "Wie habt ihr Stories priorisiert?" | Project Board → Filter auf `Priority` → P0/P1/P2 zeigen |
| "Was passiert wenn PO eine Story ablehnt?" | PR #25 öffnen → der Hotfix-Commit zeigt die Re-Review-Schleife |
| "Wo seht ihr was *nicht* gemacht wurde?" | Milestones (Tab 2) → die offenen Issue-Counts oder Project Board → Filter `Status = Todo` |
| "Macht ihr Retrospektiven?" | docs/-Tab → drei `retrospective-…md`-Dateien zeigen |
| "Wer hat was gemacht?" | PR-Liste → unterschiedliche Author-Avatare wären sichtbar (aber bei uns ist alles unter `xxTAYOxx` — kannst du transparent erklären als "alle Implementierung von einem zentralen Entwickler-Account") |

---

## Fallback wenn das Internet/GitHub langsam ist

- Repo lokal in VS Code oder im File-Explorer öffnen
- `docs/`-Ordner zeigen — alle Markdown-Files sind dort lesbar
- Project Board und Issues sind dann nicht zeigbar, aber die Dokumentation steht für sich
