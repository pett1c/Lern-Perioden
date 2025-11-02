# Lern-Periode 11
# 22.8 bis 26.9

## fertiges Projekt

Dies ist die Webanwendung **“Fortsetzer“**, die auf *Deutsch* und *Russisch* verfügbar ist und absurde und humorvolle Fortsetzungen für vom Benutzer eingegebene Texte generiert. Die Generierung basiert auf einem **Markov-Kettenmodell** (`markovify` in Python), das anhand eines Textkorpus trainiert wird, der durch *Parsing* (`de_parser.py`, `ru_parser.py`) aus zwei satirischen Wiki-Websites zusammengestellt wurde: der deutschen **[Uncyclopedia](https://de.uncyclopedia.co/)** und der russischen **[Absurdopedia](https://absurdopedia.wiki/)**. Technisch wurde das Projekt in *HTML* und *CSS* umgesetzt, wobei die Logik über die *Pyodide*-Technologie in *Python* ausgeführt wird.

## Grob-Planung

1. Erklären Sie Ihre Projekt-Idee in einem Satz, als müssen Sie einen Investor davon überzeugen.

Mein Projekt ist ein einfacher Unterhaltungs-Webchat-Bot, der absurde und lustige Erweiterungen des Benutzertxtes mit einer minimalistischen Benutzeroberfläche generiert.

2. Erklären Sie, welche technischen Herausforderungen Sie in Ihrem Projekt erwarten.

In erster Linie wird dies meine erste Erfahrung mit der Erstellung von etwas sein, das einer KI ähnelt, was bereits viel Recherche erfordern wird.
Erstellung eines Textkorpus: Ich habe bereits eine Quelle in Form der russischen [Absurdopedia](https://absurdopedia.wiki/) und der deutschen [Stupidedia](https://www.stupidedia.org/), aber ich muss entweder die Artikel manuell parsen oder ein Skript erstellen.
Ausserdem werde ich auf Anraten von ChatGPT einen Algorithmus auf Basis von Markov-Ketten (**markovify**-Bibliothek für Python) erstellen, mit dem ich nicht vertraut bin.

3. Beschreiben Sie, welche nicht-technischen Aspekte Sie in diesem Projekt besonders üben möchten.

Erstellung eines ansprechenden und gleichzeitig einfachen Designs für die Website sowie Implementierung eines Chatbots, der in den meisten Fällen wirklich lustig ist und nicht nur sinnlos (obwohl dies indirekt auch der Kern des Absurden ist).

4. Wie unterscheidet sich dieses Projekt von Ihrem Projekt in 335; und wo ergänzen sich diese Projekte?

Mein Projekt steht in keinem Zusammenhang mit Modul 335.

## 22.8

- [x] Quelle für die Erstellung von Korpusen finden
- [x] Erste Version des Parsers für Artikel erstellen

Am 15.08. haben wir einen einfachen „Textfortsetzer” erstellt, der mir schliesslich den letzten Anstoss gab, mich endlich dazu zu entschliessen, zumindest einen Chatbot zu entwickeln, der dem aktuellen KI-System ähnelt. Als wir heute den Code des „Textfortsetzers“ betrachteten, begann ich darüber nachzudenken, welchen ungewöhnlichen, aber gleichzeitig recht einfachen Chatbot ich realisieren könnte. Da kam mir sofort ["Porfirievich"](https://porfirevich.ru/) in den Sinn, der in den Jahren 2019-2020, noch vor der Veröffentlichung von GPT3, sehr beliebt war. Das ist genau dieser „Textfortsetzer”, der so einfach wie möglich funktioniert: Der Benutzer schreibt etwas, drückt dann auf eine Button und „Porfirievich” setzt die Geschichte fort. Am Ende gab es sogar eine sogenannte „Top-Liste”, in der jeder Nutzer seine Geschichte mit „Porfirievich” veröffentlichen konnte und andere Nutzer diese Geschichten liken konnten. Das brachte mich auf die Idee, eine super absurde Quelle zu nehmen und einen „Textfortsetzer“ zu erstellen, der darauf abzielt, mit nur einem Klick möglichst seltsame, unvorhersehbare und vor allem lustige Geschichten zu generieren. Mir war sofort klar, dass ich eine minimalistische Website erstellen und den Code selbst in Python schreiben wollte. Schliesslich machte ich mich als Erstes auf die Suche nach Quellen für die Erstellung des Korpus und stiess zufällig auf speziell absurde Wikipedias sowohl in russischer als auch in deutscher Sprache (oben), woraufhin mir sofort klar wurde, dass dies meine Option war. Deshalb machte ich mich sofort daran, einen einfachen Parser zu erstellen, um die lustigsten Artikel auszuwählen und sie für den zukünftigen Chatbot zu bereinigen. Am Ende ist natürlich etwas dabei herausgekommen, grösstenteils mit Hilfe von ChatGPT (zuvor hatte ich noch nicht mit der Bibliothek ***BeautifulSoup*** gearbeitet, mit der man die gewünschten Informationen aus den Seiten „herausziehen” kann).

## 29.8

- [x] Als Entwickler möchte ich lustige Artikel aus Absurdopedia finden und sammeln, um einen Textkorpus zu erstellen, der den Nutzern witzige und absurde Fortsetzungen bietet.
- [x] Als Entwickler möchte ich mich mit der ***PyScript-Bibliothek*** vertraut machen, um Python-Code effektiv in die Website zu integrieren und die Funktion „Weiterführer” ohne komplexes Backend zu implementieren.
- [x] Als Nutzer möchte ich ein einfaches und intuitives Website-Design sehen, um Text einfach eingeben und Fortsetzungen ohne unnötige Komplikationen erhalten zu können.
- [x] Als Entwickler möchte ich ***PyScript*** implementieren und eine grundlegende Architektur für die Website erstellen, um eine Plattform für die Entwicklung und das Testen des „Weiterführers”-Codes vorzubereiten.

Heute habe ich mich als Erstes daran gemacht, lustige Artikel auf Absurdopedia zu suchen, um einen ersten gebrauchsfertigen Korpus zu erstellen. Am Ende habe ich **72** lustige Wiki-Seiten gefunden, aus denen fast **35.000 Zeichen** gewonnen werden konnten, die sofort einsatzbereit waren. Als Nächstes habe ich mich mit der ***PyScript-Dokumentation*** und der Arbeit damit beschäftigt. Das war überraschend einfach, obwohl es letztendlich zu Problemen in der nächsten Phase geführt hat. In der nächsten Phase habe ich mich mit der Erstellung einer einfachen Website und der Integration von PyScript darin beschäftigt. Die meiste Zeit habe ich damit verbracht, Importfehler zu beheben, die ich immer noch nicht behoben habe. Nächste Woche werde ich versuchen, eine erste funktionierende Version des Fortsetzungsprogramms zu erstellen und gegebenenfalls Fehler zu beheben. Dazu gehört auch ein möglicher Wechsel von ***PyScript*** zu ***Pyodide***, falls es nicht klappt, mit ***PyScript*** zu arbeiten.

## 05.9

- [x] Als Entwickler möchte ich den Code für „Weiterführer“ in Python unter Verwendung von ***markovify*** schreiben, um die Generierung absurder Texte auf der Grundlage des Korpus zu realisieren.
- [x] Als Nutzer möchte ich, dass „Weiterführer“ direkt auf der Website über PyScript und ***markovify*** funktioniert, um sofortige und lustige Textfortsetzungen zu erhalten.
- [x] Als Entwickler möchte ich einen ersten Test von „Weiterführer“ durchführen, um sicherzustellen, dass es sinnvolle und unterhaltsame Textfortsetzungen generiert.
- [x] Als Entwickler möchte ich mögliche Fehler, Bugs und Unvollkommenheiten, die während des ersten Testlaufs auftreten, beheben, damit die erste Version des Produkts stabil läuft und dem Nutzer die volle Grundfunktionalität von „Weiterführer” bietet.

Obwohl mein Laptop am Donnerstag kaputt gegangen ist, konnte ich die Logik von „Weiterführer“ dennoch umsetzen. Der Einfachheit halber bin ich jedoch von ***PyScript*** zu ***Pyodide*** gewechselt, da ich nur mit ***Pyodide*** die Integration der Logik direkt in `.html` realisieren konnte. Ausserdem habe ich einen kleinen Test durchgeführt und festgestellt, dass die Grundfunktionalität in Form einer Textfortsetzung vorhanden ist, aber bisher völlig sinnlos ist (absurde Fortsetzung != sinnlose Fortsetzung). Deshalb werde ich mich bei der nächsten Sitzung in erster Linie damit beschäftigen.

## 12.9

- [x] Als Nutzer möchte ich, dass der generierte Text im Zusammenhang mit meiner Eingabe Sinn und Logik ergibt, damit ich qualitativ hochwertigere Fortsetzungen meiner Geschichten erhalten kann.
- [x] Als Nutzer möchte ich, dass der Algorithmus zur Textgenerierung logischere und sinnvollere Fortsetzungen erstellt, damit meine Geschichten interessant und qualitativ hochwertig sind.
- [ ] Als Nutzer möchte ich zusätzliche Einstellungen zur Kontrolle der Fortsetzungsgenerierung haben, damit ich die Fortsetzungen nach meinen Vorlieben anpassen kann.
- [ ] Als Nutzer möchte ich, dass die Anwendung Fortsetzungen sowohl auf Russisch auf der Grundlage von **Absurdopedia** als auch auf Deutsch auf der Grundlage von **Stupidedia *(und anderen)*** generieren kann, damit ich Geschichten sowohl auf Russisch als auch auf Deutsch erstellen kann.

Heute habe ich mich als Erstes damit beschäftigt, den Output des Fortsetzers zu verbessern. Auf Anraten der KI habe ich zunächst die Grösse des Korpus erhöht (von fast 350.000 auf 1.000.000) und mich dann mit der Überarbeitung des Codes selbst befasst. Leider habe ich etwas Zeit gebraucht, um zu verstehen, dass ein vollwertiges neuronales Netzwerk besser für das ursprüngliche Ziel des Projekts geeignet ist als ein einfacher Text-Fortsetzer, aber da ich nur wenig Zeit habe, habe ich mich entschlossen, weiter mit Markovify zu arbeiten. Das Problem mit der Logik habe ich zunächst gelöst, indem ich den Textfortsetzer so geändert habe, dass er nicht mehr nach dem ursprünglichen Wort am Anfang des Satzes im Korpus sucht, sondern einfach nach dem ursprünglichen Wort im Korpus, unabhängig von seiner Position. Als Nächstes habe ich einen adaptiven Fallback hinzugefügt, der zunächst versucht, die letzten drei Wörter im Korpus zu finden, dann zwei, dann eins, und wenn er nichts findet, nimmt er einfach etwas Zufälliges. Die aktuellen Probleme bestehen darin, dass die Generierung immer noch sehr seltsam aussieht, oft sehr zufällig ist und es Probleme mit der Gross-/Kleinschreibung und den Kasus gibt. Bei der nächsten Sitzung werde ich bereits mit der deutschen Version und den übrigen Einstellungen arbeiten.

## 19.9

Die Arbeitspakete wurden auf den 26.9 verschoben, da ich am 19.9 auf einer Reise vom Italienischkurs war.

## 26.9

- [x] Als Nutzer möchte ich zusätzliche Einstellungen zur Kontrolle der Fortsetzungsgenerierung haben, damit ich die Fortsetzungen nach meinen Vorlieben anpassen kann.
- [x] Als Nutzer möchte ich, dass die Anwendung Fortsetzungen sowohl auf Russisch auf der Grundlage von **Absurdopedia** als auch auf Deutsch auf der Grundlage von ~~**Stupidedia *(und anderen)***~~ **Uncyclopedia** generieren kann, damit ich Geschichten sowohl auf Russisch als auch auf Deutsch erstellen kann.
- [x] Als Nutzer möchte ich die Möglichkeit haben, verschiedene Generierungsoptionen durchzugehen, um eine logischere Geschichte zu erstellen.
- [x] ~~Als Nutzer möchte ich beim Aufrufen der Website nicht warten müssen, bis sie geladen ist, und wenn ich doch warten muss, dann möchte ich eine Animation sehen, damit ich sofort mit der Website arbeiten kann, ohne darüber nachdenken zu müssen, wann ich endlich mit dem Schreiben beginnen kann.~~

Heute habe ich damit begonnen, die Seiten von **Stupidedia** zu parsen, um die URLs in `de_parser.py` zu füllen. Das hat lange gedauert und war letztendlich leider umsonst – ich habe über vier Stunden lang versucht, die Seiten von **Stupidedia** erfolgreich zu parsen, indem ich den Code des Parsers selbst geändert habe, um die *Cloudflare-Überprüfung* auf der Website zu umgehen, und am Ende musste ich die Seiten erneut sammeln, diesmal jedoch von einer anderen ähnlichen deutschen Wiki-Seite – **[Uncyclopedia](https://de.uncyclopedia.co/)**. Nachdem ich `de_corpus.txt` erfolgreich ausgefüllt hatte, begann ich mit dem Hinzufügen neuer Einstellungen und eines Ladebildschirms. Bei der Arbeit mit dem zweiten wurde mir klar, dass der Ladebildschirm überhaupt nicht erforderlich ist – die Website kann jetzt fast sofort genutzt werden. Eine neue Einstellung war die Skala *„Kreativität”*. Parallel dazu fügte ich auch die Button *„Eine weitere Option”* hinzu. Am schwierigsten und *(fast)* zeitaufwändigsten war die Umsetzung der Sprachumschaltung, was ebenfalls sehr viel Zeit in Anspruch nahm, aber letztendlich funktioniert alles einwandfrei und ich bin mit dem Ergebnis zufrieden, obwohl ich dafür sehr viel arbeiten musste.

## Reflexion

Dieses Projekt war für mich ein lang gehegter Wunsch, denn ich wollte schon seit langem mit irgendeiner Art der Textgenerierung arbeiten, sei es mit neuronalen Netzen oder, wie in meinem Fall, mit der Generierung auf Basis von Markov-Ketten. Ich habe mich nicht ohne Grund für Markov-Ketten entschieden – ich habe vor kurzem zufällig von dieser Idee gehört und sie hat mir einfach als Idee sehr gut gefallen, ebenso wie ihre Geschichte. Deshalb habe ich mich entschieden, speziell mit ihnen zu arbeiten. Abgesehen davon war das Projekt ziemlich... anstrengend. Das Sammeln der Seiten war unglaublich langweilig, aber notwendig, um zumindest ein halbwegs vernünftiges Ergebnis zu erzielen. Und die letzten Phasen der Umsetzung haben mich unglaublich viel Zeit gekostet, wahrscheinlich weil ich den größten Teil davon mit einer sinnlosen Beschäftigung verbracht habe – dem Problem mit Cloudflare auf Stupidedia. Ich hätte einfach sofort ein anderes Wiki wählen sollen, aber leider arbeitete ich auch zum ersten Mal mit Parsern speziell für Webseiten und hatte keine Ahnung, ob es trotz aller Schwierigkeiten mit Cloudflare möglich war, die von mir bereits gesammelten Seiten auf Stupidedia zu verwenden. Also ja. Das Projekt war äußerst interessant, wenn auch ziemlich komplex.