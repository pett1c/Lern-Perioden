# Lern-Periode 12
# 07.11 bis ?

## fertiges Projekt

...

## Grobe Beschreibung

Mein Projekt ist ein Spiel im Roguelike-Genre (Deckbuilder), inspiriert von Balatro, bei dem der Spieler sein „Lexikon“ (52 Buchstaben zu Beginn, wie ein Kartenspiel) zusammenstellt, mit 8 verfügbaren Buchstaben in Runden spielt und Wörter auf Deutsch (optional: Englisch, Russisch) bildet, um „Punktequoten“ zu sammeln. Nicht genug Schritte geschafft? Dann hast du verloren. Zwischen den Runden gibt es einen Shop, um das Lexikon zu verbessern. Die Buchstaben selbst können ebenfalls verbessert werden, ebenso wie die Bonusse für eine bestimmte Anzahl von Buchstaben in Wörtern und vieles mehr. Um zu gewinnen, muss der Spieler 6 oder 7 Stufen (dies ist in jeder Partie zufällig) durchlaufen, die aus zwei normalen Runden und einer besonderen Runde mit einem Debuff als Boss bestehen. Bei 6 Stufen kann man nach dem Durchspielen einen erschwerten Endlosmodus spielen. Bei 7 Stufen besteht die letzte Stufe aus den finalen drei Bossen als drei Runden mit Debuffs. Danach kann man ebenfalls den Endlosmodus spielen. Jede Partie ist aufgrund des Zufallsprinzips einzigartig. Tech: Godot

## Epics

**1: Wörterbuch, Buchstabensatz und Wortvalidierung**

Als Spieler möchte ich, dass das Spiel die von mir eingegebenen Wörter überprüft, damit der Fokus auf Fairness liegt.
**Features:**
- Laden und Interpretieren des Wörterbuchs
- Validierung der vom Benutzer eingegebenen Wörter

**2: Runde – Tastatur, Felder, Eingabe, Schritt**

Als Spieler möchte ich die Möglichkeit haben, Wörter aus einem festen Satz von Buchstaben zusammenzustellen, um die Spannung des Limits zu spüren.
**Features:**
- QWERTZ-Tastatur, auf der die Buchstaben aus dem aktuellen Buchstabensatz hervorgehoben werden
- 7 Slots, in die der Spieler Buchstaben eingeben kann
- Animierte Enter-Taste, die erscheint, wenn ein Wort eingegeben werden kann
- Animation beim Einreichen eines Wortes
- Beim Bewegen des Mauszeigers über einen Buchstaben erscheint ein Popup-Fenster, in dem alle erforderlichen Eigenschaften des Buchstabens beschrieben werden

**3: Formel für Punkte und Buchstabenverbesserungen**

Als Spieler möchte ich strategische Buchstabenverbesserungen, damit meine Combos Euphorie auslösen.
**Features:**
- Jeder Buchstabe hat ein Gewicht (abhängig von der Häufigkeit, mit der der Buchstabe in Wörtern verwendet wird)
- Jeder Buchstabe kann nun Verbesserungen erhalten, nämlich Bonus (+5-10 Punkte), Glas (x2 Multiplikator, 25 % Chance, dass er zerstört wird), Stahl (x1,5 Multiplikator, solange er im aktuellen Buchstabensatz enthalten ist), Gold (+3-5 $, wenn er am Ende übrig bleibt)

**4: Progression – Stufen, Runden, Bosse**

Als Spieler möchte ich einen steigenden Schwierigkeitsgrad mit einer Quote haben, damit mein Sieg wertvoll ist.
**Features:**
- Eine Quote, die mit jeder Runde steigt
- Eine sich mit jeder Stufe ändernde Anzahl von Schritte
- Eine Stufenkarte, auf der Informationen zu den Runden in der Stufe zu sehen sind
- Boss-Debuffs für die letzte Runde in jeder Stufe
- Endlosmodus

**5: Shop + Karten**

Als Spieler möchte ich einen Shop haben, um mein Vokabular, meine Buchstaben und insgesamt mein Gameplay zu verbessern, damit jedes Spiel und jeder meiner Builds einzigartig ist.
**Features:**
- Vollwertiger Shop, in dem Folgendes erscheint: 2 Buchstaben zum Kauf (die Anzahl kann mit einem speziellen Gutschein erhöht werden), 2 zufällige Pakete, 1 Gutschein (selten), Reroll (zwei Buchstaben zum Kauf, wird jedes Mal teurer)
- Alphabetkarten, die den Multiplikator für Wörter mit einer bestimmten Anzahl von Buchstaben verbessern (z. B. können Wörter aus drei Buchstaben verbessert werden)
- Neun Wortkarten, die folgende Funktionen erfüllen: kopiert die letzte Buchstaben-/Wortkarte, macht zwei Buchstaben zu Bonusbuchstaben, macht einen Buchstaben zu einem Stahlbuchstaben, macht einen Buchstaben zu einem Glasbuchstaben, macht einen Buchstaben zu einem Goldbuchstaben, verdoppelt das Geld (max. 50 $), gibt zwei zufällige Buchstaben, zerstört zwei zufällige Buchstaben und wandelt einen Buchstaben in einen anderen um.

**6: Roguelike – Zufälligkeit des Vokabulares**

Als Spieler möchte ich, dass jedes Spiel einen einzigartigen Vokabular hat, damit ich es wiederholen kann.
**Features:**
- Zufälliger Start des Spiels einstellen
- „Schnipsel” wie Pakete mit Buchstaben und Karten. Es gibt folgende Arten: Standard (5-6 Buchstaben zur Auswahl), alphabetisch (4 alphabetische Karten zur Auswahl), wörtlich (4 wörtliche Karten zur Auswahl). Außerdem werden sie in folgende Arten unterteilt: Normal (nur ein Buchstabe/eine Karte kann ausgewählt werden) und Selten (zwei können ausgewählt werden)

**7: UI/UX, Ton, Soundtrack und Sonstiges**

Als Spieler möchte ich ein schönes und reaktionsschnelles Spiel, das mich fesselt.
**Features:**
- Kostenlose Assets aus dem Internet für GUI und Sonstiges
- Von mir komponierter Soundtrack
- Von mir erstellte Sounds
- Animationen

## 07.11

- [x] Grobe Beschreibung schreiben

—

- [x] Repository erstellen
- [x] Godot installieren
- [x] Epics schreiben

Heute habe ich die Grundlage für das Projekt vorbereitet: Die meiste Zeit habe ich damit verbracht, mir ein umfassendes Verständnis des Projekts zu verschaffen, von A bis Z, um zu verstehen, wie mein endgültiges Projekt aussehen wird. Dank dieser Vorarbeit konnte ich detaillierte Epics schreiben, an die ich mich halten werde, und ich habe auch ein kleines, von KI generiertes Designdokument. Ausserdem habe ich natürlich einen Ordner für das neue LP in meinem Repository mit allen LPs erstellt und Godot für die Arbeit installiert.

## 14.11

- [x] Suche nach geeigneten Assets

—

- [x] Einen Projekt erstellen, Assets importieren, MainMenu mit minimaler UI erstellen
- [x] Round-Szene mit minimaler UI erstellen
- [x] GameManager mit Laden und Verarbeiten eines Testwörterbuchs erstellen

Als Erstes habe ich das dezentrale Arbeitspaket erledigt, nämlich die Suche nach Assets, die ich für Texturen und anderes benötige. Ich habe drei Assets hinzugefügt: eines für die gesamte UI, ein zweites für Progressbars und ein drittes für die Tastatur. Alle wurden kostenlos auf itch.io gefunden. Der nächste Schritt für mich war die Erstellung des Projekts und des Hauptmenüs mit einer minimalistischen UI in Form von drei Buttons: Start, Einstellungen und Beenden. Die meiste Zeit habe ich für die Erstellung der Buttons gebraucht, da eigene Buttons in Godot etwas seltsam erstellt werden und ich im Internet nach Informationen suchen musste. Danach habe ich mich mit dem Schreiben des grundlegenden GameManagers beschäftigt, in dem ich einen Test-Buchstabensatz lade. Schliesslich habe ich die Round-Szene implementiert, in der sich auch die grundlegende UI in Form eines Progressbars für die Quote und die Anzahl der Schritte befindet.

## 21.11

- [x] Suche nach einem deutschen Wörterbuch zur Validierung, dessen Download und Überprüfung in der Konsole.

—

- [x] Erstellung eines Vokabulars mit Gewichtung und Anzahl jedes Buchstabens.
- [x] Generierung eines Buchstabensatzes mit Anzeige in der Round-Szene.
- [x] Erstellung einer Möglichkeit zur Eingabe von Buchstaben, Validierung der Eingabe.

Heute war ein produktiver Tag. Als Erstes habe ich mich auf die Suche nach einem Wörterbuch gemacht, aber letztendlich habe ich nur ein fertiges Wörterbuch im JSONL-Format direkt von Wikimedia gefunden, das leider sehr viel "Müll" enthält, den ich nicht brauche, und ausserdem sehr gross ist (1 GB), was zu langen Ladezeiten beim Testen führt. Nach der Suche habe ich mich jedoch mit der Überarbeitung von `game_manager.gd` beschäftigt, wo das Wörterbuch geladen und die eingegebenen Wörter validiert werden. Danach habe ich mich mit der Erstellung einer neuen Szene beschäftigt – `Letter`, in der sich eine Button mit Text befindet, sowie `letter.gd`, in der der Button der gewünschte Buchstabe und das gewünschte Gewicht zugewiesen werden. Zuletzt habe ich die Szene `Round` überarbeitet (die erforderlichen Bereiche für die verfügbaren Buchstaben in der Hand, die Eingabe, die Button „Submit“ und das Textfelf „Feedback“ hinzugefügt) und seine `round.gd`, in der ich alles zusammenführe.

## 28.11

- [x] Die Überarbeitung eines Wörterbuchs, bei der der "Müll" entfernt und nur die reinen Wörter übrig bleiben.

—

- [x] Eine vollständige Punkteberechnung (vorerst ohne Buchstabenverbesserungen) und eine Aktualisierung der Quote implementieren.
- [x] Die Mechanik zum Zurücksetzen/Mischen der Buchstaben implementieren.
- [x] Eine Überprüfung des Rundenendes (Sieg/Verlust) erstellen und entsprechend den Übergang zu den Ergebnissen/zum Shop implementieren.

Heute war ein äusserst produktiver Tag. Als Erstes habe ich mein Wörterbuch übergearbeitet, d. h. unnötigen Müll zu entfernen – zuerst habe ich alles ausser dem Feld `"word"` gelöscht. Danach habe ich doppelte Wörter entfernt und zum Schluss Wörter mit Sonderzeichen und Bindestrichen (wobei ich nur Buchstaben des deutschen Alphabets als zulässige Zeichen belassen habe). Am Ende hatte ich einen grossen Array mit mehr als **300.000** Wörtern. Als Nächstes habe ich mich mit der Umsetzung der Punkteberechnung und der Aktualisierung der Quote, der Umsetzung des `DiscardButton` (der derzeit einen Schritt benötigt, um zu funktionieren) beschäftigt und schliesslich alles für den Übergang zu den entsprechenden Szenen vorbereitet (bei einem Verlust – Szene / Pop-up mit Statistiken, bei einem Sieg – Übergang zum Shop).

## 05.12

- [x] Eine Szene mit Laden erstellen, die nun leer ist (um den Übergang zwischen den Runden realisieren: Runde -> Laden -> Stufenkarte)

—

- [x] Entwicklung eine Szene zwischen dem Hauptmenü und der Runde - Stufenkarte, wo alle Informationen über die Runden und den Boss am Ende der Stufe zu finden sind (wie in Balatro).
- [x] Grafische Elemente in der Runde korrigieren (derzeit sieht beispielsweise die Hand wie 7 sehr kleine Buchstaben aus, während `SubmitButton` und `DiscardButton` sehr gross sind; `Feedback` Feld entfernen und durch eine schöne Punkteanzeige auf der linken Seite ersetzen (wie in Balatro)).
- [x] Realisierung einer grundlegender Progression mit einer Erhöhung der Quote in jeder Runde und einem vollständigen Debuff in der letzten Runde (Boss). (`TBD:` Nach der vollständigen Implementierung des Shops und der Wirtschaft zuerst die Quotenlimits für die Runden anpassen, dann die Progression von der ersten bis zur letzten Stufe mit dem Endboss oder einem Endlosspiel implementieren)

Heute war ein äusserst produktiver Tag. Zuerst habe ich mich mit der Umgestaltung der Struktur der Knoten für die `Round`-Szene beschäftigt, die nun in zwei Teile „aufgeteilt” ist – den linken Teil mit Informationen und einer schönen Animation der Punktevergabe und den rechten Teil, in dem der Spieler Buchstaben auswählt und tatsächlich spielt. Danach habe ich die `StageMap`-Szene erstellt, in der der Spieler alle Runden der Stufe sehen und jede einzelne davon auswählen kann. Am Ende habe ich die `Shop`-Szene erstellt, in der es bisher nur ein Label mit dem Geld und einer Button zum Wechseln zur `StageMap` gibt. Parallel dazu habe ich mich mit dem Code beschäftigt.

## 12.12

Ausfall, da wir an der BBB ganzen Tag sein werden.

## 19.12
tbd am 12.12
- [] 

—

- [] 
- [] 
- [] 

...

## Reflexion

...
