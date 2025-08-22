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
		"https://absurdopedia.wiki/%D0%9A%D0%BE%D1%81%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D0%BC%D1%83%D1%81%D0%BE%D1%80",
		"https://absurdopedia.wiki/%D0%9B%D1%8E%D0%B4%D0%B8",
		"https://absurdopedia.wiki/%D0%A1%D0%B0%D1%80%D0%B0%D0%BD%D1%87%D0%B0"
	]

	corpus = parse(urls)
	with open('ru_corpus.txt', 'w', encoding='utf-8') as f:
		f.write(corpus)
	
	print(f"Collected {len(corpus)} text symbols.")
	print("Corpus succesfully saved in 'ru_corpus.txt'.")



