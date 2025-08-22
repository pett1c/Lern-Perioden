# Lern-Periode 11
# 22.8 bis 26.9

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

Am 15.08. haben wir einen einfachen „Textfortsetzer” erstellt, der mir schliesslich den letzten Anstoss gab, mich endlich dazu zu entschliessen, zumindest einen Chatbot zu entwickeln, der dem aktuellen KI-System ähnelt. Als wir heute den Code des „Textfortsetzers“ betrachteten, begann ich darüber nachzudenken, welchen ungewöhnlichen, aber gleichzeitig recht einfachen Chatbot ich realisieren könnte. Da kam mir sofort []"Porfirievich"](https://porfirevich.ru/) in den Sinn, der in den Jahren 2019-2020, noch vor der Veröffentlichung von GPT3, sehr beliebt war. Das ist genau dieser „Textfortsetzer”, der so einfach wie möglich funktioniert: Der Benutzer schreibt etwas, drückt dann auf eine Button und „Porfirievich” setzt die Geschichte fort. Am Ende gab es sogar eine sogenannte „Top-Liste”, in der jeder Nutzer seine Geschichte mit „Porfirievich” veröffentlichen konnte und andere Nutzer diese Geschichten liken konnten. Das brachte mich auf die Idee, eine super absurde Quelle zu nehmen und einen „Textfortsetzer“ zu erstellen, der darauf abzielt, mit nur einem Klick möglichst seltsame, unvorhersehbare und vor allem lustige Geschichten zu generieren. Mir war sofort klar, dass ich eine minimalistische Website erstellen und den Code selbst in Python schreiben wollte. Schliesslich machte ich mich als Erstes auf die Suche nach Quellen für die Erstellung des Korpus und stiess zufällig auf speziell absurde Wikipedias sowohl in russischer als auch in deutscher Sprache (oben), woraufhin mir sofort klar wurde, dass dies meine Option war. Deshalb machte ich mich sofort daran, einen einfachen Parser zu erstellen, um die lustigsten Artikel auszuwählen und sie für den zukünftigen Chatbot zu bereinigen. Am Ende ist natürlich etwas dabei herausgekommen, grösstenteils mit Hilfe von ChatGPT (zuvor hatte ich noch nicht mit der Bibliothek ***BeautifulSoup*** gearbeitet, mit der man die gewünschten Informationen aus den Seiten „herausziehen” kann).

## 29.8

- [ ] Suche nach den lustigsten Artikeln
- [ ] Erkundung der Bibliothek ***markovify***
- [ ] Erkundung von ***PyScript***
- [ ] Erste Schritte mit der Website

...

## 05.9

- [ ] 
- [ ] 
- [ ] 
- [ ] 

...

## 12.9

- [ ] 
- [ ] 
- [ ] 
- [ ] 

...

## 19.9

- [ ] 
- [ ] 
- [ ] 
- [ ] 

...

## 26.9

- [ ] 
- [ ] 
- [ ] 
- [ ] 

...