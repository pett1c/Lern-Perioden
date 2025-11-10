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

- [] Suche nach geeigneten Assets
—
- [] Einen Projekt erstellen, Assets importieren, MainMenu mit minimaler UI erstellen
- [] Round-Szene mit minimaler UI erstellen
- [] GameManager mit Laden und Verarbeiten eines Testwörterbuchs erstellen

...

## 21.11

- [] 
—
- [] 
- [] 
- [] 

...

## 28.11

- [] 
—
- [] 
- [] 
- [] 

...

## 05.12

- [] 
—
- [] 
- [] 
- [] 

...

## 12.12

- [] 
—
- [] 
- [] 
- [] 

...

## 19.12

- [] 
—
- [] 
- [] 
- [] 

...

## Reflexion

...