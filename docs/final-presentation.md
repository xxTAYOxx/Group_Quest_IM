# Finale Präsentation — ListMate

**Team:** Karl Schmidt (PO) · Aloys Trinker (SM) · Paul Wiedermann · Tim Sindilar · Laetitia Weben
**Repo:** https://github.com/xxTAYOxx/Group_Quest_IM
**Project Board:** https://github.com/users/xxTAYOxx/projects/1

> Zeitbudget: max. 10 min. Punkt 1 ist Live-Demo (kein Skript hier). Punkte 2–4 sind fertig zum Vorlesen formuliert, mit Scrum- und Team-Fokus.

---

## Punkt 1 — Wie schaut die finale App aus

*Live-Demo — kein Speaker-Skript notwendig.*

---

## Punkt 2 — Die drei wichtigsten Lessons Learned

Wenn wir auf die fünf Sprints zurückblicken, gibt es drei Erkenntnisse, die für uns als Team am wertvollsten waren — und alle drei haben weniger mit Technik zu tun als mit der Art, wie wir miteinander gearbeitet haben.

### Lesson 1: T-Shirt-Sizing macht Sprint-Kapazität verhandelbar statt geraten

Am ersten Tag haben wir alle User Stories nach Größen geschätzt — XS, S, M, L, XL. Das hat erst banal gewirkt, war aber eines der wichtigsten Tools im ganzen Projekt. Vor jedem Sprint konnten wir mit einem Blick entscheiden, was realistisch in der verfügbaren Zeit reinpasst.

Das Ergebnis: über alle fünf Sprints hatten wir **kein einziges Carry-over**. Wir haben in jedem Sprint exakt das geschafft, was wir uns vorgenommen haben. Das war kein Zufall — das war die Disziplin, sich nicht zu überfordern, und der Mut, eine Story aus dem Sprint rauszuhalten, wenn die Kapazität es nicht hergibt. Scrum ist erst dann wirksam, wenn man auch "Nein" zu Stories sagen kann, die nicht reinpassen.

### Lesson 2: Retrospektiven sind das Herz von Scrum, nicht Pflicht-Theater

Wir haben pro Sprint-Block eine Retrospektive geschrieben — drei insgesamt. Und jede einzelne hat unsere Arbeitsweise im nächsten Sprint konkret verändert.

Nach der ersten Retrospektive haben wir Feature-Branches eingeführt. Nach der zweiten haben wir vereinbart, dass Tests niemals die echte Datenbank anfassen dürfen. Nach der dritten haben wir vor jedem Sprint einen kurzen "Confidence-Check" eingeführt, um nur Stories anzunehmen, bei denen wir uns wirklich sicher waren.

Eine Retrospektive ist nur dann wertvoll, wenn aus ihr Action Items entstehen, die im nächsten Sprint wirklich umgesetzt werden. Bei uns war das jedes Mal so. Und genau deshalb haben sich unsere Sprints im Laufe des Projekts sichtbar verbessert.

### Lesson 3: Feature-Branches und Pull Requests schaffen Vertrauen im Team

Bis Sprint 2 haben wir alles direkt auf den Hauptzweig committed. Das hat funktioniert, aber wir hatten ständig das Gefühl, uns gegenseitig auf die Füße zu treten — niemand wollte derjenige sein, der den Build kaputt macht. Ab Sprint 3 hat jedes Sprint-Ergebnis einen eigenen Branch und einen Pull Request bekommen.

Plötzlich konnten alle parallel arbeiten ohne Angst. Und der Product Owner konnte den Sprint Review nicht nur am Live-Bildschirm sondern auch am Code-Diff machen — was sogar einen Bug aufgedeckt hat, der uns sonst erst in der Final-Demo um die Ohren geflogen wäre. Pull Requests sind nicht nur ein Werkzeug — sie sind ein Vertrauens-Mechanismus, der das Team produktiver und entspannter gemacht hat.

---

## Punkt 3 — Was würden wir beim nächsten Projekt anders machen

Wir würden nicht alles anders machen — vieles hat funktioniert. Aber drei Dinge nehmen wir uns für das nächste Mal konkret vor.

### Den Pull-Request-Workflow von Sprint 1 an nutzen

Das Branching-Megatutorial der LV kam erst am Tag 3, und wir haben uns daran gehalten. Aber rückblickend hätten wir früher starten können. Hätten wir auch in Sprint 1 und 2 schon Pull Requests gemacht, hätten wir wahrscheinlich Probleme früher entdeckt und hätten uns schneller an "kleinere, fokussiertere Commits" gewöhnt. Branches einzuführen ist keine technische Hürde, es ist eine Team-Vereinbarung — und die hätten wir einfach von Anfang an treffen können.

### Die Scrum-Rollen mittendrin rotieren lassen

Wir hatten fixe Rollen über das ganze Projekt — ein Product Owner, ein Scrum Master, drei Developer. Das war pragmatisch, aber es heißt auch, dass nur eine Person Sprint Plannings moderiert hat, nur eine die Retrospektiven geleitet hat, nur eine den Backlog gepflegt hat. Beim nächsten Mal würden wir die Rollen mindestens einmal in der Mitte tauschen, damit jeder im Team die Erfahrung macht, was diese Verantwortung wirklich bedeutet. Das ist auch realistischer für die Praxis, wo Rollen in Teams öfter wechseln.

### Daily Stand-ups einführen, auch in einem kurzen Projekt

Wir haben uns vor jedem Sprint kurz synchronisiert, aber nicht jeden Tag und nicht innerhalb eines Sprints. Bei einem mehrtägigen Projekt mit Pausen dazwischen wäre ein 5-Minuten-Stand-up zu Tagesbeginn Gold wert gewesen: "Was hat jeder heute vor?", "Wo hängt's?", "Wer braucht Unterstützung?". Diese drei Fragen hätten uns Sync-Reibung erspart und das Team-Gefühl noch verstärkt.

---

## Punkt 4 — Wie nutzen wir die Lessons Learned beim Data-Science-Hackathon im 3. Semester

Der Hackathon ist die nächste echte Bewährungsprobe für alles, was wir hier gelernt haben. Und unser Plan ist, die Scrum-Disziplin eins zu eins zu übertragen.

### Wir behandeln ML-Experimente wie User Stories

Statt einer langen Brainstorming-Liste an "Ideen, die wir ausprobieren könnten" formulieren wir jede Experiment-Idee als Story: *"Als Analyst:in möchte ich ein Baseline-Modell mit Logistic Regression, damit wir eine Referenz-Genauigkeit haben."* Das zwingt uns, vor dem Code-Schreiben zu klären, **warum** wir das Experiment überhaupt machen und **wie** wir Erfolg messen. Das ist die wichtigste Übertragung aus diesem Projekt.

### Wir verteilen Rollen klar — auch in einem Daten-Projekt

Hackathons gehen oft kaputt, weil alle gleichzeitig alles probieren. Wir nehmen mit: jemand übernimmt die Product-Owner-Rolle und priorisiert, welche Modelle gebaut werden. Jemand übernimmt die Scrum-Master-Rolle und stellt sicher, dass wir uns nicht in endlosem Tuning verlieren. Die anderen arbeiten parallel an Modellen — jede:r mit einem eigenen Sprint-Goal.

### Wir machen tägliche Mini-Retrospektiven am Abend

Fünf Minuten am Ende jedes Hackathon-Tags: Was hat geklappt? Was nicht? Was machen wir morgen anders? Genau das hat uns in diesem Projekt geholfen, mit jedem Sprint besser zu werden. Im Hackathon — mit weniger Zeit und mehr Druck — ist das noch wichtiger als hier.

### Wir setzen Sprint-Goals statt einer Wunschliste

*"Heute Baseline mit über 70 % Accuracy"* ist ein Sprint-Goal. *"Heute fünf Modelle ausprobieren"* ist eine Wunschliste. Die LV hat uns gezeigt, dass ein einziges klares Ziel ein ganzes Team fokussiert — und genauso werden wir es im Hackathon angehen.

---

## Mini-Backup für etwaige Plenumsfragen

| Frage | Kurze Antwort |
|---|---|
| Wie viele Stories habt ihr geschafft? | 14 von 25, das sind 56% des Backlogs, alle in 5 sauberen Sprints ohne Carry-over |
| Wie habt ihr entschieden, was *nicht* gemacht wird? | Priorisierung P0/P1/P2 plus klares "Out of Scope" pro Sprint-Planning |
| Hattet ihr Konflikte im Team? | Keine inhaltlichen — die Rollen waren klar und die Sprint-Goals waren entscheidungsfindend |
| Was war der größte Lerneffekt? | Dass Scrum als Tool-Set wirklich Disziplin schafft, wenn man es ernst nimmt — und nicht nur als Bürokratie sieht |
