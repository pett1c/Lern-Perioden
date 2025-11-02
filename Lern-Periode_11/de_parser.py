import requests
from bs4 import BeautifulSoup
import re
import time

def parse(urls):
	all_text = []

	for url in urls:
		print("Parsing:", url)
		response = requests.get(url, timeout=10)
		response.encoding = 'utf-8'

		soup = BeautifulSoup(response.text, 'html.parser')
		content = soup.find('div', {'id': 'mw-content-text'})
		if not content:
			content = soup.find('div', {'class': 'mw-parser-output'})

		if content:
			for unwanted in content.find_all(['script', 'style', 'table']):
				unwanted.decompose()
			for nav in content.find_all('div', class_=True):
				class_names = ' '.join(nav.get('class', []) or []).lower()
				if 'navbox' in class_names or 'infobox' in class_names:
					nav.decompose()

			paragraphs = content.find_all('p')
			for p in paragraphs:
				text = p.get_text().strip()
				if text and len(text) > 20:
					all_text.append(text)
		time.sleep(1)
	
	full_text = ' '.join(all_text)
	full_text = clean_text(full_text)

	return full_text

def clean_text(text):
	# -links & -[]
	text = re.sub(r'\[\[.*?\]\]', '', text)
	text = re.sub(r'\[.*?\]', '', text)

	# -{}
	text = re.sub(r'\{\{.*?\}\}', '', text)
	text = re.sub(r'\{.*?\}', '', text)

	# -spaces & -tabs
	text = re.sub(r'\s+', ' ', text)
	text = re.sub(r'\n+', ' ', text)

	# -speacialsymbols & -wikisymbols
	text = re.sub(r'[''«»„“]', '"', text)
	text = re.sub(r'[–—]', '-', text)

	return text.strip()

if __name__ == "__main__":
	urls = [
		"https://de.uncyclopedia.co/wiki/Belgien",
		"https://de.uncyclopedia.co/wiki/Russland",
		"https://de.uncyclopedia.co/wiki/Ukraine",
		"https://de.uncyclopedia.co/wiki/F%C3%BChrer",
		"https://de.uncyclopedia.co/wiki/Vietnam",
		"https://de.uncyclopedia.co/wiki/China",
		"https://de.uncyclopedia.co/wiki/USA",
		"https://de.uncyclopedia.co/wiki/W%C3%A4hrung",
		"https://de.uncyclopedia.co/wiki/Euro",
		"https://de.uncyclopedia.co/wiki/Deutschland",
		"https://de.uncyclopedia.co/wiki/Aldi",
		"https://de.uncyclopedia.co/wiki/Ausl%C3%A4nder",
		"https://de.uncyclopedia.co/wiki/Ausland",
		"https://de.uncyclopedia.co/wiki/Kapitalismus",
		"https://de.uncyclopedia.co/wiki/Bill_Gates",
		"https://de.uncyclopedia.co/wiki/Steve_Jobs",
		"https://de.uncyclopedia.co/wiki/Microsoft",
		"https://de.uncyclopedia.co/wiki/Windows",
		"https://de.uncyclopedia.co/wiki/Erde",
		"https://de.uncyclopedia.co/wiki/Merkur",
		"https://de.uncyclopedia.co/wiki/Venus",
		"https://de.uncyclopedia.co/wiki/Jupiter",
		"https://de.uncyclopedia.co/wiki/Uranus",
		"https://de.uncyclopedia.co/wiki/Mensch",
		"https://de.uncyclopedia.co/wiki/Mann",
		"https://de.uncyclopedia.co/wiki/Strom",
		"https://de.uncyclopedia.co/wiki/Frau",
		"https://de.uncyclopedia.co/wiki/Auto",
		"https://de.uncyclopedia.co/wiki/Bier",
		"https://de.uncyclopedia.co/wiki/Dihydrogenmonoxid",
		"https://de.uncyclopedia.co/wiki/Wissenschaft",
		"https://de.uncyclopedia.co/wiki/Internet",
		"https://de.uncyclopedia.co/wiki/Ebay",
		"https://de.uncyclopedia.co/wiki/Facebook",
		"https://de.uncyclopedia.co/wiki/Psychologe",
		"https://de.uncyclopedia.co/wiki/Arzt",
		"https://de.uncyclopedia.co/wiki/Polen",
		"https://de.uncyclopedia.co/wiki/England",
		"https://de.uncyclopedia.co/wiki/Kaffee",
		"https://de.uncyclopedia.co/wiki/Fr%C3%BCher_war_alles_besser",
		"https://de.uncyclopedia.co/wiki/Kafffee",
		"https://de.uncyclopedia.co/wiki/Tee",
		"https://de.uncyclopedia.co/wiki/Medusa_Markt",
		"https://de.uncyclopedia.co/wiki/Gesundheit",
		"https://de.uncyclopedia.co/wiki/Schweiz",
		"https://de.uncyclopedia.co/wiki/Familie",
		"https://de.uncyclopedia.co/wiki/Kind",
		"https://de.uncyclopedia.co/wiki/Fernsehen",
		"https://de.uncyclopedia.co/wiki/Wirtschaft",
		"https://de.uncyclopedia.co/wiki/H%26M",
		"https://de.uncyclopedia.co/wiki/Preis",
		"https://de.uncyclopedia.co/wiki/Wein",
		"https://de.uncyclopedia.co/wiki/Italien",
		"https://de.uncyclopedia.co/wiki/Burger_King",
		"https://de.uncyclopedia.co/wiki/Essen",
		"https://de.uncyclopedia.co/wiki/Armut",
		"https://de.uncyclopedia.co/wiki/Europ%C3%A4ische_Union",
		"https://de.uncyclopedia.co/wiki/Marketing",
		"https://de.uncyclopedia.co/wiki/Kunst",
		"https://de.uncyclopedia.co/wiki/Katze",
		"https://de.uncyclopedia.co/wiki/Zombie",
		"https://de.uncyclopedia.co/wiki/Hund",
		"https://de.uncyclopedia.co/wiki/Wurst",
		"https://de.uncyclopedia.co/wiki/Sport",
		"https://de.uncyclopedia.co/wiki/Fu%C3%9Fball",
		"https://de.uncyclopedia.co/wiki/Fussball",
		"https://de.uncyclopedia.co/wiki/Schach",
		"https://de.uncyclopedia.co/wiki/Tennis",
		"https://de.uncyclopedia.co/wiki/Baseball",
		"https://de.uncyclopedia.co/wiki/Tastatur",
		"https://de.uncyclopedia.co/wiki/Langeweile%E2%84%A2",
		"https://de.uncyclopedia.co/wiki/Gehirn",
		"https://de.uncyclopedia.co/wiki/Buch",
		"https://de.uncyclopedia.co/wiki/Kopf",
		"https://de.uncyclopedia.co/wiki/Leber",
		"https://de.uncyclopedia.co/wiki/Afrika",
		"https://de.uncyclopedia.co/wiki/Area_51",
		"https://de.uncyclopedia.co/wiki/Arbeitgeber",
		"https://de.uncyclopedia.co/wiki/Aspirin",
		"https://de.uncyclopedia.co/wiki/Astrologie",
		"https://de.uncyclopedia.co/wiki/Sonne",
		"https://de.uncyclopedia.co/wiki/Bachelor",
		"https://de.uncyclopedia.co/wiki/Bento",
		"https://de.uncyclopedia.co/wiki/Beton",
		"https://de.uncyclopedia.co/wiki/Bitcoin",
		"https://de.uncyclopedia.co/wiki/B%C3%BCro",
		"https://de.uncyclopedia.co/wiki/Schnapp_den_Parkplatz",
		"https://de.uncyclopedia.co/wiki/Einsamkeit%E2%84%A2",
		"https://de.uncyclopedia.co/wiki/Flugzeug",
		"https://de.uncyclopedia.co/wiki/Zug",
		"https://de.uncyclopedia.co/wiki/Atom-U-Bahn",
		"https://de.uncyclopedia.co/wiki/Pause",
		"https://de.uncyclopedia.co/wiki/Denkmalschutz",
		"https://de.uncyclopedia.co/wiki/Deutsche_Bahn_AG",
		"https://de.uncyclopedia.co/wiki/Versp%C3%A4tung",
		"https://de.uncyclopedia.co/wiki/K%C3%A4se",
		"https://de.uncyclopedia.co/wiki/Deutschland_in_2040",
		"https://de.uncyclopedia.co/wiki/Die_WAHRHEIT%E2%84%A2",
		"https://de.uncyclopedia.co/wiki/Diskothek",
		"https://de.uncyclopedia.co/wiki/Donald_Trump",
		"https://de.uncyclopedia.co/wiki/Engel",
		"https://de.uncyclopedia.co/wiki/Farbe",
		"https://de.uncyclopedia.co/wiki/Fanfiction",
		"https://de.uncyclopedia.co/wiki/Urheberrecht",
		"https://de.uncyclopedia.co/wiki/Fiat",
		"https://de.uncyclopedia.co/wiki/Flugsicherheit",
		"https://de.uncyclopedia.co/wiki/Alkohol",
		"https://de.uncyclopedia.co/wiki/Sinn",
		"https://de.uncyclopedia.co/wiki/Smartphone",
		"https://de.uncyclopedia.co/wiki/Wikipedia",
		"https://de.uncyclopedia.co/wiki/Spam",
		"https://de.uncyclopedia.co/wiki/Leben",
		"https://de.uncyclopedia.co/wiki/Tod",
		"https://de.uncyclopedia.co/wiki/Kind",
		"https://de.uncyclopedia.co/wiki/Altern",
		"https://de.uncyclopedia.co/wiki/Einfamilienhaus",
		"https://de.uncyclopedia.co/wiki/Musik",
		"https://de.uncyclopedia.co/wiki/Musiker",
		"https://de.uncyclopedia.co/wiki/Weltraum",
		"https://de.uncyclopedia.co/wiki/Reflektive_Logik",
		"https://de.uncyclopedia.co/wiki/Stephen_Hawking",
		"https://de.uncyclopedia.co/wiki/Unsinn_des_Lebens",
		"https://de.uncyclopedia.co/wiki/Werbung",
		"https://de.uncyclopedia.co/wiki/IKEA",
		"https://de.uncyclopedia.co/wiki/Polizei",
		"https://de.uncyclopedia.co/wiki/Hanf",
		"https://de.uncyclopedia.co/wiki/Feuerwehr",
		"https://de.uncyclopedia.co/wiki/Drogen",
		"https://de.uncyclopedia.co/wiki/Marihuana",
		"https://de.uncyclopedia.co/wiki/Alkoholismus",
		"https://de.uncyclopedia.co/wiki/L%C3%BCge",
		"https://de.uncyclopedia.co/wiki/Propaganda",
		"https://de.uncyclopedia.co/wiki/LinkedIn",
		"https://de.uncyclopedia.co/wiki/Apple",
		"https://de.uncyclopedia.co/wiki/Microsoft_Office",
		"https://de.uncyclopedia.co/wiki/Excel",
		"https://de.uncyclopedia.co/wiki/Drucker",
		"https://de.uncyclopedia.co/wiki/PC",
		"https://de.uncyclopedia.co/wiki/Windows_XP",
		"https://de.uncyclopedia.co/wiki/Counter-Strike",
		"https://de.uncyclopedia.co/wiki/Informatik",
		"https://de.uncyclopedia.co/wiki/Informatiker",
		"https://de.uncyclopedia.co/wiki/Hacker",
		"https://de.uncyclopedia.co/wiki/Undictionary:A",
		"https://de.uncyclopedia.co/wiki/Undictionary:B",
		"https://de.uncyclopedia.co/wiki/Undictionary:C",
		"https://de.uncyclopedia.co/wiki/Undictionary:D",
		"https://de.uncyclopedia.co/wiki/Undictionary:E",
		"https://de.uncyclopedia.co/wiki/Undictionary:F",
		"https://de.uncyclopedia.co/wiki/Undictionary:G",
		"https://de.uncyclopedia.co/wiki/Undictionary:H",
		"https://de.uncyclopedia.co/wiki/Undictionary:I",
		"https://de.uncyclopedia.co/wiki/Undictionary:J",
		"https://de.uncyclopedia.co/wiki/Undictionary:K",
		"https://de.uncyclopedia.co/wiki/Undictionary:L",
		"https://de.uncyclopedia.co/wiki/Undictionary:M",
		"https://de.uncyclopedia.co/wiki/Undictionary:N",
		"https://de.uncyclopedia.co/wiki/Undictionary:O",
		"https://de.uncyclopedia.co/wiki/Undictionary:P",
		"https://de.uncyclopedia.co/wiki/Undictionary:Q",
		"https://de.uncyclopedia.co/wiki/Undictionary:R",
		"https://de.uncyclopedia.co/wiki/Undictionary:S",
		"https://de.uncyclopedia.co/wiki/Undictionary:T",
		"https://de.uncyclopedia.co/wiki/Undictionary:U",
		"https://de.uncyclopedia.co/wiki/Undictionary:V",
		"https://de.uncyclopedia.co/wiki/Undictionary:W",
		"https://de.uncyclopedia.co/wiki/Undictionary:X",
		"https://de.uncyclopedia.co/wiki/Undictionary:Y",
		"https://de.uncyclopedia.co/wiki/Undictionary:Z",
		"https://de.uncyclopedia.co/wiki/Toilette",
		"https://de.uncyclopedia.co/wiki/B%C3%BCrokratie",
		"https://de.uncyclopedia.co/wiki/Computer",
		"https://de.uncyclopedia.co/wiki/Currywurst",
		"https://de.uncyclopedia.co/wiki/D%C3%B6ner",
		"https://de.uncyclopedia.co/wiki/K%C3%BChlschrank",
		"https://de.uncyclopedia.co/wiki/Kindergarten",
		"https://de.uncyclopedia.co/wiki/Bebsi",
		"https://de.uncyclopedia.co/wiki/Pizza",
		"https://de.uncyclopedia.co/wiki/Poker",
		"https://de.uncyclopedia.co/wiki/Nike",
		"https://de.uncyclopedia.co/wiki/K%C3%BCnstliche_Intelligenz",
		"https://de.uncyclopedia.co/wiki/Reis",
		"https://de.uncyclopedia.co/wiki/Experte",
		"https://de.uncyclopedia.co/wiki/Aktie",
		"https://de.uncyclopedia.co/wiki/Blut",
		"https://de.uncyclopedia.co/wiki/Waffe",
		"https://de.uncyclopedia.co/wiki/Feuer",
		"https://de.uncyclopedia.co/wiki/Kommunismus"
	]

	corpus = parse(urls)
	with open('de_corpus.txt', 'w', encoding='utf-8') as f:
		f.write(corpus)
	
	print(f"Collected {len(corpus)} text symbols.")
	print("Corpus succesfully saved in 'de_corpus.txt'.")


