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
		"https://absurdopedia.wiki/%D0%A1%D0%B0%D1%80%D0%B0%D0%BD%D1%87%D0%B0",
		"https://absurdopedia.wiki/%D0%9E%D0%B1%D1%8A%D0%B5%D0%BA%D1%82%D0%B8%D0%B2%D0%BD%D0%B0%D1%8F_%D1%80%D0%B5%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C",
		"https://absurdopedia.wiki/%D0%A0%D0%B0%D0%B9",
		"https://absurdopedia.wiki/%D0%9F%D0%B8%D0%B2%D0%BE",
		"https://absurdopedia.wiki/%D0%92%D0%BE%D0%B4%D0%BA%D0%B0",
		"https://absurdopedia.wiki/%D0%91%D0%BE%D0%B3",
		"https://absurdopedia.wiki/%D0%A0%D0%90%D0%AF",
		"https://absurdopedia.wiki/%D0%91%D0%B8%D0%B1%D0%BB%D0%B8%D1%8F",
		"https://absurdopedia.wiki/%D0%98%D0%B8%D1%81%D1%83%D1%81_%D0%A5%D1%80%D0%B8%D1%81%D1%82%D0%BE%D1%81",
		"https://absurdopedia.wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B4%D0%B0%D1%82_%D0%BA%D0%BE%D0%BD%D1%86%D0%B0_%D1%81%D0%B2%D0%B5%D1%82%D0%B0",
		"https://absurdopedia.wiki/%D0%90%D0%B4%D0%BE%D0%BB%D1%8C%D1%84_%D0%90%D0%BB%D0%BE%D0%B8%D0%B7%D0%BE%D0%B2%D0%B8%D1%87_%D0%93%D0%B8%D1%82%D0%BB%D0%B5%D1%80",
		"https://absurdopedia.wiki/%D0%9F%D1%83%D1%88%D0%BA%D0%B8%D0%BD",
		"https://absurdopedia.wiki/%D0%9A%D0%BE%D1%81%D0%BC%D0%BE%D1%81",
		"https://absurdopedia.wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D1%86%D0%B5",
		"https://absurdopedia.wiki/%D0%97%D0%B5%D0%BC%D0%BB%D1%8F",
		"https://absurdopedia.wiki/%D0%9B%D1%83%D0%BD%D0%B0",
		"https://absurdopedia.wiki/%D0%92%D1%82%D0%BE%D1%80%D0%B0%D1%8F_%D0%BB%D1%83%D0%BD%D0%B0",
		"https://absurdopedia.wiki/%D0%9C%D0%B0%D1%80%D1%81",
		"https://absurdopedia.wiki/%D0%97%D0%B5%D0%BB%D1%91%D0%BD%D1%8B%D0%B5_%D1%87%D0%B5%D0%BB%D0%BE%D0%B2%D0%B5%D1%87%D0%BA%D0%B8",
		"https://absurdopedia.wiki/%D0%9A%D0%B0%D0%BA_%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D1%8C%D0%BD%D0%BE:%D0%92%D1%81%D1%82%D1%83%D0%BF%D0%B8%D1%82%D1%8C_%D0%B2_%D0%BA%D0%BE%D0%BD%D1%82%D0%B0%D0%BA%D1%82_%D1%81_%D0%B8%D0%BD%D0%BE%D0%BF%D0%BB%D0%B0%D0%BD%D0%B5%D1%82%D1%8F%D0%BD%D0%B0%D0%BC%D0%B8",
		"https://absurdopedia.wiki/%D0%9A%D0%B0%D0%BA_%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D1%8C%D0%BD%D0%BE:%D0%9F%D0%B5%D1%80%D0%B5%D0%B6%D0%B8%D1%82%D1%8C_%D0%B2%D1%82%D0%BE%D1%80%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_%D0%B8%D0%BD%D0%BE%D0%BF%D0%BB%D0%B0%D0%BD%D0%B5%D1%82%D1%8F%D0%BD",
		"https://absurdopedia.wiki/%D0%9D%D0%9B%D0%9E",
		"https://absurdopedia.wiki/*******",
		"https://absurdopedia.wiki/%D0%91%D0%B8%D0%BB%D0%BB%D0%B8_%D0%93%D0%B5%D0%B9%D1%82%D1%81",
		"https://absurdopedia.wiki/%D0%98%D0%BD%D1%82%D0%B5%D1%80%D0%BD%D0%B5%D1%82",
		"https://absurdopedia.wiki/%D0%A1%D0%BE%D1%82%D0%BE%D0%BD%D0%B0",
		"https://absurdopedia.wiki/%D0%97%D0%B2%D0%B5%D0%B7%D0%B4%D0%B0_%D1%81%D0%BC%D0%B5%D1%80%D1%82%D0%B8",
		"https://absurdopedia.wiki/%D0%92%D0%B8%D0%BA%D0%B8%D0%BF%D0%B5%D0%B4%D0%B8%D1%8F",
		"https://absurdopedia.wiki/%D0%A7%D1%91%D1%80%D0%BD%D0%B0%D1%8F_%D0%B4%D1%8B%D1%80%D0%B0",
		"https://absurdopedia.wiki/%D0%A1%D0%B2%D0%B5%D1%82%D0%BE%D0%B2%D0%BE%D0%B9_%D0%B3%D0%BE%D0%B4",
		"https://absurdopedia.wiki/%D0%9A%D0%BE%D1%81%D0%B0%D1%80%D1%8C",
		"https://absurdopedia.wiki/%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F",
		"https://absurdopedia.wiki/%D0%9F%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%81%D1%82",
		"https://absurdopedia.wiki/%D0%9C%D0%BE%D0%B7%D0%B3",
		"https://absurdopedia.wiki/%D0%9C%D1%8B%D1%88%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5",
		"https://absurdopedia.wiki/%D0%98%D0%BD%D1%82%D0%B5%D0%BB%D0%BB%D0%B5%D0%BA%D1%82",
		"https://absurdopedia.wiki/%D0%A1%D1%84%D0%B5%D1%80%D0%B0_%D0%94%D0%B0%D0%B9%D1%81%D0%BE%D0%BD%D0%B0",
		"https://absurdopedia.wiki/%D0%97%D0%B2%D0%B5%D0%B7%D0%B4%D0%B0",
		"https://absurdopedia.wiki/%D0%81%D0%B6",
		"https://absurdopedia.wiki/%D0%A1%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%BD%D1%8B%D0%B9_%D0%B0%D0%B4%D0%BC%D0%B8%D0%BD%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%82%D0%BE%D1%80",
		"https://absurdopedia.wiki/%D0%9D%D0%B0%D1%80%D0%BA%D0%BE%D1%82%D0%B8%D0%BA%D0%B8",
		"https://absurdopedia.wiki/%D0%9F%D1%8F%D1%82%D0%BD%D0%B8%D1%86%D0%B0",
		"https://absurdopedia.wiki/%D0%A7%D0%B8%D1%82%D0%B2%D0%B5%D1%80%D1%85",
		"https://absurdopedia.wiki/%D0%9D%D0%B5%D0%B4%D0%B5%D0%BB%D1%8F",
		"https://absurdopedia.wiki/%D0%9F%D0%BE%D0%BD%D0%B5%D0%B4%D0%B5%D0%BB%D1%8C%D0%BD%D0%B8%D0%BA",
		"https://absurdopedia.wiki/%D0%A4%D1%82%D0%BE%D1%80%D0%BD%D0%B8%D0%BA",
		"https://absurdopedia.wiki/%D0%A1%D1%80%D0%B5%D0%B4%D0%B0",
		"https://absurdopedia.wiki/%D0%A1%D1%83%D0%B1%D0%BA%D0%BE%D1%82%D0%B0",
		"https://absurdopedia.wiki/%D0%92%D0%BE%D1%81%D0%BA%D1%80%D0%B5%D1%81%D0%B5%D0%BD%D1%8C%D0%B5",
		"https://absurdopedia.wiki/%D0%AF%D1%85%D0%B2%D0%B5",
		"https://absurdopedia.wiki/%D0%AF%D1%89%D0%B8%D0%BA_%D0%A8%D0%B0%D0%B9%D1%82%D0%B0%D0%BD%D0%B0",
		"https://absurdopedia.wiki/%D0%9B%D0%B5%D0%BD%D1%82%D0%B0_%D0%9C%D1%91%D0%B1%D0%B8%D1%83%D1%81%D0%B0",
		"https://absurdopedia.wiki/%D0%91%D0%B5%D1%81%D0%BA%D0%BE%D0%BD%D0%B5%D1%87%D0%BD%D0%BE%D1%81%D1%82%D1%8C",
		"https://absurdopedia.wiki/%D0%91%D0%B8%D1%81%D1%81%D0%B5%D0%BA%D1%82%D1%80%D0%B8%D1%81%D0%B0",
		"https://absurdopedia.wiki/%D0%9A%D1%80%D1%8B%D1%81%D0%B0",
		"https://absurdopedia.wiki/%D0%9A%D0%BE%D1%82",
		"https://absurdopedia.wiki/%D0%95%D0%B3%D0%B8%D0%BF%D0%B5%D1%82",
		"https://absurdopedia.wiki/%D0%A8%D0%B2%D0%B5%D0%B9%D1%86%D0%B0%D1%80%D0%B8%D1%8F",
		"https://absurdopedia.wiki/%D0%9D%D0%B8%D0%BA%D1%82%D0%BE",
		"https://absurdopedia.wiki/%D0%9B%D0%B5%D0%BE%D0%BD%D0%B0%D1%80%D0%B4%D0%BE_%D0%94%D0%B0_%D0%92%D0%B8%D0%BD%D1%87%D0%B8",
		"https://absurdopedia.wiki/%D0%9A%D0%BE%D0%BD%D0%B5%D1%87%D0%BD%D1%8B%D0%B9_%D0%B0%D0%B2%D1%82%D0%BE%D0%BC%D0%B0%D1%82",
		"https://absurdopedia.wiki/3",
		"https://absurdopedia.wiki/%D0%9F%D0%BB%D0%B0%D0%B3%D0%B8%D0%B0%D1%82",
		"https://absurdopedia.wiki/%D0%98%D0%B4%D0%B5%D1%8F",
		"https://absurdopedia.wiki/%D0%93%D0%B4%D0%B5",
		"https://absurdopedia.wiki/%D0%9F%D0%BB%D0%B0%D0%BD%D0%B5%D1%82%D0%B0",
		"https://absurdopedia.wiki/%D0%96%D0%B8%D0%B7%D0%BD%D1%8C",
		"https://absurdopedia.wiki/%D0%9D%D0%B0%D1%80%D0%BE%D0%B4",
		"https://absurdopedia.wiki/%D0%9D%D0%B0%D1%86%D0%B8%D0%B7%D0%BC",
		"https://absurdopedia.wiki/%D0%A6%D0%B5%D0%BC%D0%B5%D0%BD%D1%82",
		"https://absurdopedia.wiki/%D0%96%D0%B5%D0%BB%D0%B5%D0%B7%D0%BE",
		"https://absurdopedia.wiki/%D0%97%D0%B0%D0%B3%D0%BE%D0%B3%D1%83%D0%BB%D0%B8%D0%BD%D0%B0",
		"https://absurdopedia.wiki/%D0%9E%D1%80%D1%83%D0%B6%D0%B8%D0%B5",
		"https://absurdopedia.wiki/%D0%9E%D0%B3%D0%BE%D0%BD%D1%8C",
		"https://absurdopedia.wiki/%D0%A5%D0%B0%D1%80%D0%B0%D0%BA%D0%B8%D1%80%D0%B8",
		"https://absurdopedia.wiki/%D0%AF%D0%BF%D0%BE%D0%BD%D0%B8%D1%8F",
		"https://absurdopedia.wiki/%D0%93%D0%BE%D0%BB%D0%BE%D0%B4%D0%BE%D0%BC%D0%BE%D1%80",
		"https://absurdopedia.wiki/%D0%91%D0%B5%D0%BB%D0%B0%D1%80%D1%83%D1%81%D1%8C",
		"https://absurdopedia.wiki/%D0%9F%D0%BE%D0%BA%D0%B5%D0%BC%D0%BE%D0%BD",
		"https://absurdopedia.wiki/%D0%A0%D0%B5%D0%BA%D1%83%D1%80%D1%81%D0%B8%D0%B2%D0%BD%D0%B0%D1%8F_%D1%83%D1%82%D0%BA%D0%B0",
		"https://absurdopedia.wiki/%D0%90%D0%BD%D0%B8%D0%BC%D0%B5",
		"https://absurdopedia.wiki/%D0%9C%D0%BE%D0%B7%D0%B3",
		"https://absurdopedia.wiki/IQ",
		"https://absurdopedia.wiki/%D0%99%D0%B0%D0%B4",
		"https://absurdopedia.wiki/%D0%AD%D0%B2%D1%82%D0%B0%D0%BD%D0%B0%D0%B7%D0%B8%D1%8F",
		"https://absurdopedia.wiki/%D0%9A%D1%80%D0%B0%D1%81%D0%BE%D1%82%D0%B0",
		"https://absurdopedia.wiki/%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D1%8B%D0%B9_%D1%86%D0%B2%D0%B5%D1%82",
		"https://absurdopedia.wiki/%D0%91%D0%B5%D0%B7%D1%83%D0%BC%D0%BD%D1%8B%D0%B5_%D1%83%D1%87%D1%91%D0%BD%D1%8B%D0%B5",
		"https://absurdopedia.wiki/%D0%93%D0%B5%D0%BD%D0%B5%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D0%BC%D0%BE%D0%B4%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%86%D0%B8%D1%8F",
		"https://absurdopedia.wiki/%D0%93%D0%9C%D0%9E-%D1%84%D0%BE%D0%B1%D1%8B",
		"https://absurdopedia.wiki/%D0%9A%D1%80%D0%BE%D1%82",
		"https://absurdopedia.wiki/%D0%91%D0%BE%D0%BB%D1%8C%D1%88%D0%BE%D0%B9_%D0%B0%D0%B4%D1%80%D0%BE%D0%BD%D0%BD%D1%8B%D0%B9_%D0%BA%D0%BE%D0%BB%D0%BB%D0%B0%D0%B9%D0%B4%D0%B5%D1%80",
		"https://absurdopedia.wiki/%D0%A1%D0%B8%D0%BB%D0%B0",
		"https://absurdopedia.wiki/%D0%A1%D1%84%D0%B5%D1%80%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D0%BA%D0%BE%D0%BD%D1%8C_%D0%B2_%D0%B2%D0%B0%D0%BA%D1%83%D1%83%D0%BC%D0%B5",
		"https://absurdopedia.wiki/%D0%94%D0%BE%D0%BB%D0%B3%D0%BE%D0%BD%D0%BE%D1%81%D0%B8%D0%BA",
		"https://absurdopedia.wiki/%D0%A1%D0%BB%D0%BE%D0%BD",
		"https://absurdopedia.wiki/%D0%9D%D0%B5%D0%B3%D1%80",
		"https://absurdopedia.wiki/%D0%93%D0%BB%D0%BE%D0%B1%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F",
		"https://absurdopedia.wiki/%D0%9C%D0%B0%D0%BA%D0%B4%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%B4%D1%81",
		"https://absurdopedia.wiki/%D0%9A%D0%BE%D0%BB%D0%B0",
		"https://absurdopedia.wiki/%D0%A1%D0%BA%D0%BE%D1%80%D0%B0%D1%8F_%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C",
		"https://absurdopedia.wiki/%D0%A8%D0%BA%D0%BE%D0%BB%D0%B0",
		"https://absurdopedia.wiki/%D0%91%D0%BE%D1%82%D0%B0%D0%BD%D1%8B",
		"https://absurdopedia.wiki/%D0%A8%D0%B0%D1%80%D0%BE%D0%B2%D0%B0%D1%80%D1%8B",
		"https://absurdopedia.wiki/%D0%A8%D0%B8%D0%B7%D0%BE%D1%84%D0%B0%D0%B7%D0%B8%D1%8F",
		"https://absurdopedia.wiki/%D0%AF%D0%B7%D1%8B%D0%BA_%D0%B3%D0%BB%D1%83%D1%85%D0%BE%D0%BD%D0%B5%D0%BC%D1%8B%D1%85_%D1%81%D0%BF%D0%B5%D1%86%D0%BD%D0%B0%D0%B7%D0%BE%D0%B2%D1%86%D0%B5%D0%B2",
		"https://absurdopedia.wiki/%D0%A7%D0%B0%D1%81%D1%8B",
		"https://absurdopedia.wiki/%D0%A0%D0%B5%D0%BC%D0%BE%D0%BD%D1%82_%D1%87%D0%B0%D1%81%D0%BE%D0%B2",
		"https://absurdopedia.wiki/%D0%A5%D0%B5%D1%80%D0%B0%D0%BD%D1%83%D0%BA%D0%B0_%D0%9F%D0%BE%D1%80%D0%BE%D1%8F%D0%BB%D1%8E",
		"https://absurdopedia.wiki/%D0%A1%D0%BC%D0%B5%D1%85_%D0%B1%D0%B5%D0%B7_%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D0%BB",
		"https://absurdopedia.wiki/%D0%A4%D0%B0%D0%BD%D1%84%D0%B8%D0%BA",
		"https://absurdopedia.wiki/%D0%A3%D0%B6%D0%B0%D1%81%D0%BD%D0%BE%D0%B5_%D1%87%D0%B8%D1%81%D0%BB%D0%BE_%D0%BA%D0%BE%D1%82%D0%BE%D0%B2_%D0%BD%D0%B0_%D1%87%D0%B5%D1%80%D0%B4%D0%B0%D0%BA%D0%B5_(%D1%81%D1%82%D0%B0%D1%82%D1%8C%D1%8F)",
		"https://absurdopedia.wiki/%D0%93%D0%B5%D0%BE%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D1%8F",
		"https://absurdopedia.wiki/%D0%91%D0%B5%D1%81%D0%BA%D0%BE%D0%BD%D0%B5%D1%87%D0%BD%D0%BE%D1%81%D1%82%D1%8C",
		"https://absurdopedia.wiki/%D0%A1%D1%80%D0%B5%D0%B4%D0%BD%D0%B5%D1%81%D1%82%D0%B0%D1%82%D0%B8%D1%81%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D0%B3%D1%80%D0%B0%D0%B6%D0%B4%D0%B0%D0%BD%D0%B8%D0%BD",
		"https://absurdopedia.wiki/%D0%98%D0%BD%D0%B4%D0%B8%D1%8F_(%D1%81%D0%B5%D0%B2%D0%B5%D1%80%D0%BD%D0%B0%D1%8F)",
		"https://absurdopedia.wiki/%D0%98%D1%80%D0%BB%D0%B0%D0%BD%D0%B4%D0%B8%D1%8F",
		"https://absurdopedia.wiki/%D0%9A%D0%B0%D0%BC%D0%B0%D0%B7",
		"https://absurdopedia.wiki/%D0%9C%D0%B0%D1%88%D0%B8%D0%BD%D0%BD%D1%8B%D0%B9_%D0%BF%D0%B5%D1%80%D0%B5%D0%B2%D0%BE%D0%B4",
		"https://absurdopedia.wiki/%D0%9C%D0%B8%D1%80%D0%BE%D0%B2%D0%BE%D0%B9_%D0%B7%D0%B0%D0%B3%D0%BE%D0%B2%D0%BE%D1%80_%D0%BF%D1%80%D0%BE%D1%82%D0%B8%D0%B2_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8",
		"https://absurdopedia.wiki/%D0%9C%D1%8B%D1%88%D1%8C",
		"https://absurdopedia.wiki/%D0%9D%D0%BE%D1%81%D1%82%D1%80%D0%B0%D0%B4%D0%B0%D0%BC%D1%83%D1%81",
		"https://absurdopedia.wiki/%D0%9E%D0%B3%D1%80%D0%BE%D0%BC%D0%BD%D1%8B%D0%B5_%D0%B1%D0%BE%D0%B5%D0%B2%D1%8B%D0%B5_%D1%80%D0%BE%D0%B1%D0%BE%D1%82%D1%8B",
		"https://absurdopedia.wiki/%D0%9F%D0%B0%D1%80%D0%B0%D0%BD%D0%BE%D0%B9%D1%8F",
		"https://absurdopedia.wiki/%D0%9F%D0%BE%D1%80%D0%BE%D1%88%D0%BE%D0%BA",
		"https://absurdopedia.wiki/%D0%A0%D0%B5%D0%B2%D0%BE%D0%BB%D1%8E%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D0%B0%D1%8F_%D1%8D%D0%BD%D0%B5%D1%80%D0%B3%D0%B8%D1%8F_%D0%A7%D0%B5",
		"https://absurdopedia.wiki/IP",
		"https://absurdopedia.wiki/%D0%91%D0%B0%D0%BD%D0%B0%D0%BD%D0%BE%D0%B2%D0%B0%D1%8F_%D0%BA%D0%BE%D0%B6%D1%83%D1%80%D0%B0",
		"https://absurdopedia.wiki/%D0%AF%D0%B7%D1%8C",
		"https://absurdopedia.wiki/%D0%A7%D0%B8%D0%BF%D1%81%D1%8B",
		"https://absurdopedia.wiki/%D0%A7%D1%83%D0%B3%D1%83%D0%BD%D0%B8%D0%B9",
		"https://absurdopedia.wiki/%D0%AD%D1%84%D1%84%D0%B5%D0%BA%D1%82_%D1%82%D0%BE%D0%BF%D0%BE%D1%80%D0%B0",
		"https://absurdopedia.wiki/%D0%A4%D0%B0%D0%BA%D1%82",
		"https://absurdopedia.wiki/%D0%A4%D0%B8%D0%BB%D0%BE%D1%81%D0%BE%D1%84%D0%B8%D1%8F",
		"https://absurdopedia.wiki/%D0%A4%D1%80%D0%B0%D0%BA%D1%82%D0%B0%D0%BB",
		"https://absurdopedia.wiki/%D0%A3%D0%B4%D0%B0%D0%BB%D0%B8%D0%B7%D0%BC",
		"https://absurdopedia.wiki/%D0%A2%D0%B5%D1%80%D0%BC%D0%B8%D0%BD%D0%B0%D1%82%D0%BE%D1%80",
		"https://absurdopedia.wiki/%D0%A2%D1%80%D0%B0%D0%B2%D0%BC%D0%B0%D0%B9",
		"https://absurdopedia.wiki/%D0%A2%D1%80%D0%B8%D0%B4%D1%86%D0%B0%D1%82%D1%8C_%D1%88%D0%B5%D1%81%D1%82%D1%8C_%D1%81%D1%82%D1%80%D0%B0%D1%82%D0%B0%D0%B3%D0%B5%D0%BC",
		"https://absurdopedia.wiki/%D0%A1%D0%B0%D0%B4_%D0%B7%D0%B5%D0%BC%D0%BD%D1%8B%D1%85_%D0%BD%D0%B0%D1%81%D0%BB%D0%B0%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D0%B9",
		"https://absurdopedia.wiki/%D0%A1%D0%B0%D0%BC%D0%BE%D0%B3%D0%BE%D0%BD%D0%BE%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D1%8F",
		"https://absurdopedia.wiki/%D0%A1%D0%BC%D0%B0%D0%B9%D0%BB%D0%BE%D1%81%D1%82%D0%BE%D0%BC%D0%B0%D1%82%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%8F",
		"https://absurdopedia.wiki/%D0%9F%D1%8B%D0%BB%D0%B5%D1%81%D0%BE%D1%81",
		"https://absurdopedia.wiki/%D0%A0%D1%83%D0%BC%D1%8B%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D1%8F%D0%B7%D1%8B%D0%BA",
		"https://absurdopedia.wiki/%D0%9F%D0%BE%D1%87%D1%82%D0%B0",
		"https://absurdopedia.wiki/%D0%9F%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D0%B0_%D0%B4%D0%BE%D1%80%D0%BE%D0%B6%D0%BD%D0%BE%D0%B3%D0%BE_%D0%B4%D0%B2%D0%B8%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F",
		"https://absurdopedia.wiki/%D0%9F%D1%81%D0%B8%D1%85%D0%BE%D0%B4%D0%B5%D0%BB%D0%B8%D0%BA%D0%B8",
		"https://absurdopedia.wiki/%D0%9F%D1%82%D0%B8%D1%87%D1%8C%D0%B8_%D0%BF%D1%80%D0%B0%D0%B2%D0%B0",
		"https://absurdopedia.wiki/%D0%9F%D1%83%D0%B7%D1%8B%D0%BA%D0%B0%D0%BD%D1%82",
		"https://absurdopedia.wiki/%D0%9F%D0%BE%D0%B6%D0%B0%D1%80%D0%BD%D0%B0%D1%8F_%D0%B1%D0%B5%D0%B7%D0%BE%D0%BF%D0%B0%D1%81%D0%BD%D0%BE%D1%81%D1%82%D1%8C",
		"https://absurdopedia.wiki/%D0%9F%D0%BE%D0%BB%D0%B8%D0%B3%D0%BE%D0%BD%D1%8B",
		"https://absurdopedia.wiki/%D0%9E%D0%B4%D0%B5%D1%81%D1%81%D0%B0",
		"https://absurdopedia.wiki/%D0%9E%D0%B1%D1%8A%D1%8F%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5",
		"https://absurdopedia.wiki/%D0%9F%D0%B8%D0%BD%D0%B3-%D0%BF%D0%BE%D0%BD%D0%B3",
		"https://absurdopedia.wiki/%D0%9B%D0%B8%D1%85%D0%B8%D0%B5_90-%D0%B5",
		"https://absurdopedia.wiki/%D0%9D%D0%B0%D1%83%D1%88%D0%BD%D0%B8%D0%BA%D0%B8",
		"https://absurdopedia.wiki/%D0%9D%D0%B5%D0%BB%D0%B5%D0%B3%D0%B0%D0%BB%D1%8B",
		"https://absurdopedia.wiki/%D0%9D%D0%B5%D0%BD%D0%B0%D0%B2%D0%B8%D1%81%D1%82%D1%8C",
		"https://absurdopedia.wiki/%D0%97%D0%B0%D0%BA%D0%BE%D0%BD",
		"https://absurdopedia.wiki/%D0%98%D0%BC%D0%B8%D0%B4%D0%B6%D0%B1%D0%BE%D1%80%D0%B4",
		"https://absurdopedia.wiki/%D0%98%D0%BD%D1%82%D0%B5%D1%80%D0%BD%D0%B5%D1%82-%D0%BD%D0%B5%D0%B7%D0%B0%D0%B2%D0%B8%D1%81%D0%B8%D0%BC%D0%BE%D1%81%D1%82%D1%8C",
		"https://absurdopedia.wiki/%D0%98%D1%82%D0%B0%D0%BB%D0%B8%D1%8F",
		"https://absurdopedia.wiki/1984",
		"https://absurdopedia.wiki/Half-Life",
		"https://absurdopedia.wiki/%D0%90%D1%80%D0%BC%D0%B5%D0%BD%D0%B8%D1%8F",
		"https://absurdopedia.wiki/%D0%91%D0%B5%D0%B7%D0%B4%D0%B5%D0%BB%D1%8C%D0%BD%D0%B8%D0%BA",
		"https://absurdopedia.wiki/%D0%91%D0%B8%D0%B7%D0%BD%D0%B5%D1%81%D0%BC%D0%B5%D0%BD",
		"https://absurdopedia.wiki/%D0%92%D0%B0%D0%BD%D0%B4%D0%B0%D0%BB%D0%B8%D0%B7%D0%BC",
		"https://absurdopedia.wiki/%D0%92%D0%BE%D0%B9%D0%BD%D0%B0",
		"https://absurdopedia.wiki/%D0%92%D0%A3%D0%97",
		"https://absurdopedia.wiki/%D0%9A%D0%BE%D1%84%D0%B5"
	]

	corpus = parse(urls)
	with open('ru_corpus.txt', 'w', encoding='utf-8') as f:
		f.write(corpus)
	
	print(f"Collected {len(corpus)} text symbols.")
	print("Corpus succesfully saved in 'ru_corpus.txt'.")



