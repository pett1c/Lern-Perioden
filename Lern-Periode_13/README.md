# Lern-Periode 13

# 09.01 bis 30.01

## 3 Technologien

In dieser Lernphase wollte ich mein Projekt auf Godot weiter umsetzen, aber kurz vor dem Start bat mich ein guter Freund um Hilfe. Genauer gesagt bat er mich, ihm einen Telegram-Bot zu erstellen, um alle Kanäle/Gruppen seines „Clans” zu verwalten. Ich habe gerne zugestimmt, da ich mich schon lange mit Telegram-Bots beschäftigen wollte, aber mir fehlten völlig die Ideen und der Zweck dieser Bots. Jetzt habe ich eine klare Vorstellung davon, was von mir verlangt wird. Deshalb habe ich beschlossen, für dieses Projekt die folgenden Technologien zu erlernen (und parallel dazu das Projekt selbst zu entwickeln, wobei ich zusätzlich KI nutze):

- Aiogram (Framework): asynchrone Bibliothek für die Telegram-API.
- SQLAlchemy + AsyncPG (Library): asynchrone Arbeit mit PostgreSQL
- Redis (Technologie/Speicher): Caching, Anti-Spam und FSM-Status
  Für diese vier Sitzungen wähle ich Aiogram als Grundlage, da es im Wesentlichen der Hauptantrieb des Bots sein wird. Ich werde mit den Mustern Router, Dependency Injection und Finite State Machine (FSM) arbeiten.

## 09.01

- [X] Hello World mit Anpassungen

Heute habe ich mir die [Aiogram-Dokumentation](https://docs.aiogram.dev/en/v3.24.0/) angesehen und ein einfaches Startmenü mit Buttons  erstellt, die vorerst noch keine Funktion haben. Anschliessend werde ich mich weiter mit der Dokumentation beschäftigen und versuchen, die Funktionen zu implementieren, die mein Freund sich wünscht.

## 16.01

- [X] Environment Setup: Übertragung von Variablen, die in .env versteckt sein müssen + Installation von PostgreSQL und anderen Bibliotheken

—

- [X] Echo-Logic: Den Bot lehren, nicht nur auf Befehle, sondern auch auf einfache Nachrichten zu reagieren
- [X] Economics Menu: Eine Funktion erstellen, die eine neue Tastatur mit Tasten zeichnet, und diese an eine Taste im Hauptmenü binden
- [X] Error Handling: try-except, um Netzwerkfehler zu behandeln und nützliche Meldungen in der Konsole auszugeben.

Heute habe ich meine Kenntnisse über die Grundlagen von Aiogram weiter vertieft und parallel dazu alles beschrieben, was ich in einem echten Bot umsetzen muss.

## 23.01

- [X] FSM-Implementierung: Umsetzung von „Werbung versenden” mit Hilfe von aiogram.fsm

—

- [X] Admin-Filter Logik: benutzerdefinierter Filter, der die Benutzer-ID mit ADMIN_ID in .env abgleicht
- [X] Datenbank: Implementierung der Gutschrift und Abbuchung von „Münzen“
- [X] API-Anbindung (AI Mode): Anschluss der kostenlosen API von Openrouter
- [X] Logging: vollständige Protokollierung der Benutzeraktionen + Statistiken

Heute war ein äusserst produktiver Tag. Als Erstes habe ich die Struktur des Projekts überarbeitet, damit sie den Standards entspricht und ich angenehmer arbeiten kann. Als Nächstes habe ich die Datenbank aktualisiert, um neue Funktionen zu unterstützen, und anschliessend den Zugriff auf die KI implementiert. Dazu habe ich eines der kostenlosen DeepSeek-Modelle auf [openrouter.ai](https://openrouter.ai/) verwendet. Danach habe ich Werbung im Bot implementiert (die nun von jedem Benutzer vom Bot versendet wird) + Statistiken. Neben den grundlegenden Arbeitspaketen habe ich auch Folgendes implementiert:

— **Wirtschaftsystem:**

– Inventarsystem
– Erstellen und Löschen von Artikeln im Shop
– Kauf von Artikeln im Shop
– Tausch von Artikeln und auch Geld

— **Benutzerverwaltung:**

– Verwaltung des Benutzerguthabens
– Einrichtung des Zugriffs auf „Managment”
– Sperren/Entsperren des Zugriffs auf den Bot

![screenshot](https://files.catbox.moe/6ua37i.png)

## 30.01

tutorial

...
