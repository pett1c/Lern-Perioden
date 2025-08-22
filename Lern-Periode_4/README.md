# Lern-Periode 4
## 20.02.24 bis 02.04.24

Lern-Periode 4 war eine ziemlich umstrittene Lern-Periode, da ich immer noch nicht in der Lage war, meine Zeit richtig zu organisieren, und deshalb auf der Suche nach Ideen von einer zur nächsten wanderte. Ursprünglich war die Idee, einen Telegram-Bot zu erstellen, aber am Ende der Lernperiode kam mir eine interessante Idee, die ich leider in Lern-Periode 5 nicht weiterverfolgen konnte, da wir unbedingt eine Website erstellen mussten. Das letzte erfolglose Projekt.

## Grob-Planung

**1.** Wo stehen Sie mit Ihren Noten? In welchen Modulen waren Sie besonders stark; in welchen sind die ungenügend? Welche davon sind besonders wichtig?

*Überraschenderweise beendete ich das Semester mit ausgezeichneten Noten für mein Deutschniveau und meine allgemeinen Kenntnisse. Alles lief gut und reibungslos genug. Im Moment bin ich besonders stark in Modul 164, ich kann SQL-Code perfekt verstehen und kenne mich mit Datenbanken im Allgemeinen aus. Ursprünglich hatte ich mir so etwas von den Modulen versprochen, aber die ersten Module, die ich durchgegangen bin, haben mich ein bisschen traurig gemacht. 120, oder 122, ich weiß es nicht mehr, war ein interessantes Modul, wenn auch nicht sehr klar. Obwohl es nicht so weit von mir entfernt war, fiel es mir schwer, mich in das Ganze hineinzudenken. Ich denke, Modul 164 ist das wichtigste, weil es mir eine neue Art der Datenverarbeitung (genauer gesagt, der Datenspeicherung) eröffnet - Datenbanken.*


**2.** Was hatten Sie sich am Ende von LP3 vorgenommen? Was war Ihr VBV? Wie könnten Sie diesen besonders gut üben?

*Mein Ziel am Ende von LP3 war es, alles rechtzeitig fertig zu bekommen, das habe ich gerade noch geschafft, mit einer Dehnung. VBV? Ich weiß es nicht. Das Zeitmanagement leidet bei mir immer noch, es ist schwer, die Aufgaben richtig zu verteilen und die Zeit für jede Aufgabe zu bestimmen. Ich nehme mir immer wieder Projekte vor, die zu groß für einen relativ kurzen Zeitraum sind, obwohl RABEB ganz gut geworden ist.*


**3.** **Neu**: Was möchten Sie Neues lernen?

*Im Moment stehe ich am Scheideweg zwischen dem Erlernen einer Bibliothek, die mit Discord oder Telegramm funktioniert, aber ich werde wahrscheinlich Telegram als Basis nehmen. Es gibt auch eine Option, um Tetris in Unity zu tun (Hinweis: Ich habe mit ihm vor gearbeitet, und ziemlich erfolgreich. im Allgemeinen begann ich С# lernen nur mit Unity)*


**4.** Was wäre ein geeignetes Projekt für diese LP4?

*Ich habe bereits oben geantwortet, aber ich neige eher dazu, einen Telegram-Bot zu schreiben. Ich denke, ich sollte mir die Menge und Qualität der Tutorials ansehen, die ich finden kann*

## 20.02.2024
Zumindest heute habe ich mich für ein Thema entschieden. Ich werde einen Telegramm-Bot schreiben. Zuerst hatte ich nicht die geringste Idee, was genau ich darin implementieren will, und dann erinnerte ich mich daran, dass ich diese kleine Tradition mit meinen Freunden in unserer Gruppe habe - jeden Montag und Freitag entsprechende Bilder zu schicken. Ich beschloss, einen Bot zu schreiben, der automatisch ein zufälliges Bild aus dem richtigen Ordner auswählt und es zur richtigen Zeit versendet (gegen vier Uhr morgens, wenn alle zur Schule aufstehen). Ich werde auch nur zufällige Bilder zum gleichen Thema, aber nicht direkt mit Montag / Freitag, die zu einer zufälligen Zeit mit einer Abkühlung von etwa vier Stunden gesendet werden wird, zu implementieren.
Ich habe höchstens einen einfachen Code implementiert, der ein Bot-Token in Telegram nimmt, und ich kann sogar schon auf die Bilder antworten. (138 Wörter)

## 27.02.2024

- [x] Versuchen, mit [KI](https://gemini.google.com/) Code zu erzeugen. Analysieren.
- [x] Schauen sich die [Dokumentation](https://telegrambots.github.io/book/1/quickstart.html) an, um genauer zu verstehen, wie genau ich Fotos aus dem Code-Ordner hochladen kann.
- [x] Schauen sich [dieses](https://youtu.be/eUjshrMUUig?si=gBcF2v5nErr_h7az) Tutorial noch einmal an, um die Grundlagen der Verwendung der API zu verstehen.
- [x] Um mit der [KI](https://gemini.google.com/) und meinem Freund (ja-ja, der) über bestimmte obskure Punkte zu diskutieren.

| Testfall-Nummer | Ausgangslage (Given) | Eingabe (When) | Ausgabe (Then) | Erfüllt? |
| --------------- | -------------------- | -------------- | -------------- | -------- |
| 1 | Gemini (von Google) | Prompt | Ein Code, der nicht funktioniert, der aber auch zum allgemeinen Verständnis beiträgt, denn Gemini verweist auf Quellen. | Ja. |
| 2 | Dokumentation | Überprüfung der Dokumentation mit einem klaren Ziel | Eine konkrete Antwort wurde nicht gefunden, wohl aber ein Verständnis. | Ja. |
| 3 | Tutorial | Anschauen des Videos | Ich erinnerte mich an alles und begann, die Basis besser zu verstehen. | Ja. |
| 4 | KI | Prompt mit Fragen, und die Fragen selbst an einen Freund. | Ich habe nie konkrete Antworten gefunden, ich kann nur auf einen Freund hoffen. | Ja. |

Heute habe ich mir vor allem verschiedene Tutorials und einige Informationen angesehen, und im Allgemeinen habe ich bereits eine Vorstellung davon, wie der Code aussehen sollte. Die Struktur selbst und wie es im Allgemeinen funktionieren sollte, ist klar. Aber was den Code angeht... Ich werde mich weiter mit dem Thema beschäftigen. Meine Idee ist, dass die API Zugriff auf drei Ordner haben soll, in denen sich die benötigten Bilder befinden, und dann, je nach Wochentag, wählt der Bot den benötigten Ordner aus und nimmt ein zufälliges Bild von dort. Klingt etwas kompliziert, aber in der Praxis ist es gar nicht so kompliziert, man muss sich nur ein bisschen mehr mit der API beschäftigen. (113 Wörter)

## 05.03.2024

- [x] Von [Gemini](https://gemini.google.com/) geschriebenen Code bearbeiten
- [x] Besprechung des von mir geschriebenen Codes mit einem Freund und Behebung von Fehlern, die auftreten
- [x] Weiteres Verständnis der [API](https://telegrambots.github.io/book/1/quickstart.html), um zu verstehen, wie man mit Gruppen arbeitet, nicht nur mit privaten Nachrichten von Benutzern.
- [x] Suche nach weiteren Tutorials zur Arbeit mit der Zeit (und Timern)

| Testfall-Nummer | Ausgangslage (Given) | Eingabe (When) | Ausgabe (Then) | Erfüllt? |
| --------------- | -------------------- | -------------- | -------------- | -------- |
| 1 | Gemini (von Google) | Nicht funktionierender Code | Bearbeitung des Codes | Ja. |
| 2 | Freund (ha-ha) | Fragen zum Code im Allgemeinen und zu Fehlern, die auftreten | Ich erkannte genauer, wie genau ich mit dem Code arbeiten muss, und kam auch zu einem umfassenderen Verständnis des Codes und der anschließend auftretenden (möglichen) Fehler | Ja. |
| 3 | API | Arbeit mit Gruppen | Ich recherchierte die verfügbaren Informationen und begann, besser zu verstehen, wie man mit Gruppen arbeitet, im Gegensatz zu privaten Nachrichten mit einem Benutzer. | Ja. |
| 4 | Suche nach Tutorials | Das nie gefundene Tutorial | Leider konnte ich trotz meiner Suche kein normales Tutorial finden, aus dem ich etwas verstehen würde. | Nein. |

Heute habe ich spezifischer mit dem Code gearbeitet, der von Gemini generiert wurde, und habe auch allgemein verstanden, welche Fehler bei der Arbeit mit solchem Code auftreten können, und ich habe auch verstanden, wie genau ich den Code schreiben sollte, um diese Fehler zu vermeiden, aber auch, damit alles so funktioniert, wie es sollte. Außerdem habe ich einige Probleme besprochen und meinem Freund (der bald großartig sein wird, haha) ein paar Fragen zu meinem Code gestellt, auf die ich zwar keine Antwort bekommen habe (weil er auch morgens beschäftigt ist, was logisch ist), aber einige davon konnte er in seiner Freizeit beantworten. Außerdem werde ich heute nach Schulschluss mit ihm weiter an dem Code arbeiten, was mir helfen wird, den Code allgemein zu verstehen und ihn auch tatsächlich zu schreiben. (130 Wörter)

## 12.03.2024

- [x] Neugestaltung aller Objektnamen (Variablen, Felder, Methoden usw.) gemäss Pascal Case und Camel Case.
- [x] Aufteilung von Konstanten in separate statische Klassen zur leichteren Änderung.
- [x] Umbenennung von Objekten (Variablen, Felder, Methoden usw.), so dass sie genau beschreiben, was sie speichern bzw. direkt tun, um die Lesbarkeit des Codes zu verbessern.
- [x] Verringerung der Anzahl der Zuständigkeiten und Gründe für Änderungen in Methoden.

| Testfall-Nummer | Ausgangslage (Given) | Eingabe (When) | Ausgabe (Then) | Erfüllt? |
| --------------- | -------------------- | -------------- | -------------- | -------- |
| 1 | Variablen, Felder, Methoden, usw. | Seltsame und unsinnige Namen | Namen gemäss den Regeln für das Schreiben von Code. | Ja. |
| 2 | Konstanten | Seltsame und inkongruente Anordnung von Konstanten nach Klassen. | Aufteilung der Konstanten auf separate statische Klassen, um Änderungen zu erleichtern. | Ja. |
| 3 | Variablen, Felder, Methoden, usw. | Seltsame, obskure und unsinnige Namen, die manchmal nicht beschreiben, was das Objekt tun soll | Umbenennung von Objekten, so dass sie genau beschreiben, was sie speichern / tun, direkt für eine bessere Lesbarkeit des Codes. | Ja. |
| 4 | Methoden. | Grosse Anzahl von Zuständigkeiten und Gründen für die Änderung von Methoden. | Verringerung der Anzahl der Zuständigkeiten und der Gründe für Änderungen in Methoden. | Ja. |

Heute war ich damit beschäftigt, meinen gesamten Code für die weitere Arbeit mit ihm qualitativ vorzubereiten. Mit den Regeln, nach denen gerade der Code geschrieben werden soll, bzw. dem Finden dieser Regeln - ein Freund hat mir dabei geholfen. Alles andere habe ich von Hand gemacht, gemäß den Regeln für das Schreiben von Code. Als Erstes habe ich alle Namen so geändert, dass sie direkt ihre Aufgabe widerspiegeln, damit es klar und lesbar ist. Als nächstes benannte ich alle Objekte nach Pascal und Camel Case um. Die vorletzte Maßnahme war, alle Konstanten in separate statische Klassen zu verschieben, um die Lesbarkeit zu verbessern, und schließlich habe ich die Anzahl der Verantwortlichkeiten und Gründe für Methoden reduziert. (115 Wörter)

## 19.03.2024

Heute habe ich mein Projekt überdacht und bin zu dem Schluss gekommen, dass ich dies nicht tun möchte, zumindest nicht im Moment. Ich habe für mich erkannt, dass ich noch nicht bereit bin für neue Bibliotheken, und ich muss mir generell einen bequemen Boden bereiten, damit ich in Zukunft klar und reibungslos arbeiten kann. In der Tat habe ich von Projekt zu Projekt ein Problem mit dem Zeitmanagement, das ich nicht in den Griff bekomme. Also habe ich darüber nachgedacht, außerdem habe ich mir Hilfe von (diesem) Freund geholt, und ich bin zu dem Entschluss gekommen, dass ich mit Telegram-Bot nicht weitermachen werde (außerdem hat sich herausgestellt, dass ich keinen normalen Server habe, um es zu unterstützen), und ich möchte lieber etwas Einfaches machen. Also wird dieses Verzeichnis aufgeräumt und durch neue Dateien ersetzt werden, näher an 26.03 (137 Wörter)

## 26.03.2024

Leider habe ich heute nicht am Unterricht teilgenommen, da ich leicht verschlafen habe :(
Während der Woche bin ich zu dem gekommen, was ich machen wollte. Es wird ein kleines Projekt sein, das ich erfolgreich in drei ganze Teile aufteilen werde (40 Wörter)

| Erster Teil                                                                                                                                                                                                                                                                                                                                               | Zweiter Teil                                                                                                                                                                                                                                                                                                                                                                                                | Dritte, abschliessende Teil                                                                                                                                                |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Ein Konsolenprogramm, mit dem man mit einer einzigen .json-Datei arbeiten kann, die buchstäblich eine Datenbank enthält, mit der der Benutzer interagieren kann (Datensätze in der Datenbank hinzufügen, bearbeiten und löschen). Ich werde dies vor dem Ende der vierten Lernperiode machen und über die Feiertage (wenn ich es nicht bis 02.04 schaffe) | Von nun an wird der Benutzer in der Lage sein, nicht mehr nur Datensätze zu erstellen, zu bearbeiten und zu löschen, sondern auch seine eigenen Datenbanken, mit der Möglichkeit, absolut auch verschiedene Arten von Argumenten und Datensatztypen in den Datenbanken selbst hinzuzufügen und zu löschen. Damit werde ich mich über die Feiertage und in der ersten Hälfte der Lernperiode 5 beschäftigen. | Das Programm wird nun grafisch, unter Verwendung von WindowsForms, dargestellt und hat eine schöne Oberfläche. Dies werde ich in der zweiten Hälfte der Lernperiode 5 tun. |

## Reflexion

Diese Lern-Periode ist mir ziemlich fremd geworden, aber gleichzeitig hat sie endlich die Spielregeln des "Spiels" verändert.

Vorher konnte ich mir kein richtiges Zeitmanagement aufbauen, ich wusste nicht, was ich tun würde, ich konnte nicht richtig verstehen, was ich an diesem (oder irgendeinem anderen) Dienstag tun würde. Aber jetzt weiß ich, wenn auch nicht vollständig, so doch in größerem Maße, wie genau ich arbeiten werde, wann genau ich arbeiten werde und was genau ich tun werde. Diese Lernperiode hat mir die Augen für all das geöffnet, was ich vorher so krampfhaft zu vermeiden suchte.

Ich hatte es satt, ständig Angst zu haben, dass ich es nicht bis zum Ende der Lernperiode schaffe oder nicht weiß, was ich tun soll, dass ich irgendein seltsames Problem mit dem Code habe und so weiter. Ich habe für mich beschlossen, dass ich von nun an nur noch Projekte in Angriff nehmen werde, die ich ganz allein und ohne fremde Hilfe bewältigen kann. Ich werde nicht mehr meiner Fantasie freien Lauf lassen, sondern die Grenzen meiner Fähigkeiten erkennen und nur noch auf dieser Grundlage etwas schaffen und tun.

In der letzten Lernperiode habe ich die Kreativität und den Ideenreichtum in den Vordergrund gestellt, und der Code war buchstäblich die Grundlage aller Projekte im unteren Bereich. Ich habe den Code ganz nach unten gestellt, anstatt mich speziell auf ihn zu konzentrieren. Ich zog es vor, von "funktionierender Software" zu träumen, statt tatsächlich zu arbeiten, und deshalb habe ich jetzt beschlossen, dass ich das nicht mehr tun will. Ich will endlich wirklich arbeiten und nicht nur so tun (261 Wörter)
