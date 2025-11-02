# main.py
from pyodide.http import open_url
from pyodide.ffi import create_proxy
import markovify
import js
import re

# global state
model = None
last_generated_span = None
current_lang = "de"

# dom elements
text_input = js.document.getElementById("text-input")
length_slider = js.document.getElementById("length-slider")
length_value = js.document.getElementById("length-value")
creativity_slider = js.document.getElementById("creativity-slider")
creativity_value = js.document.getElementById("creativity-value")
continue_button = js.document.getElementById("continue-button")
another_button = js.document.getElementById("another-button")
loading = js.document.getElementById("loading")

# update slider values
def update_length_value(*args): length_value.innerText = length_slider.value
def update_creativity_value(*args): creativity_value.innerText = creativity_slider.value
length_slider.oninput = update_length_value
creativity_slider.oninput = update_creativity_value
update_length_value(); update_creativity_value()

# load markov model for language
def load_model(lang):
    global model
    corpus = "./ru_corpus.txt" if lang == "ru" else "./de_corpus.txt"
    with open_url(corpus) as f: raw = f.read()
    model = markovify.Text(raw, state_size=2, well_formed=True)

# clean generated text
def post_process(text):
    if not text: return "."
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'(\b\w+\b)(\s+\1){2,}', r'\1', text)
    if not re.search(r'[.!?]$', text): text += '.'
    return text.strip()

# generate continuation
def generate_continuation(replace_last=False, *args):
    global last_generated_span, current_lang
    continue_button.disabled = True
    another_button.disabled = True
    loading.classList.remove("hidden")

    if not text_input.innerText.strip() and not replace_last:
        reset(); return

    word_limit = int(length_slider.value)
    creativity = int(creativity_slider.value) / 100
    max_overlap = 1.0 - creativity * 0.7
    min_overlap = max(0.1, creativity * 0.5)

    sentences = []; total = 0; tries = 0; max_tries = 60

    while total < word_limit and tries < max_tries:
        remaining = word_limit - total
        sentence = None
        if remaining <= 12:
            sentence = model.make_short_sentence(remaining * 2,
                max_overlap_ratio=max_overlap,
                min_overlap_ratio=min_overlap,
                tries=20)
        else:
            sentence = model.make_sentence(
                max_overlap_ratio=max_overlap,
                min_overlap_ratio=min_overlap,
                tries=20)

        if sentence:
            words = len(sentence.split())
            if words <= remaining * 1.3:
                if total + words > word_limit:
                    take = word_limit - total
                    sentence = ' '.join(sentence.split()[:take])
                    words = take
                sentences.append(sentence)
                total += words
        tries += 1

    result = post_process(' '.join(sentences))
    span = js.document.createElement("span")
    span.className = "new-text"
    span.innerText = " " + result

    if replace_last and last_generated_span and last_generated_span.parentNode == text_input:
        text_input.replaceChild(span, last_generated_span)
        last_generated_span = span
    else:
        text_input.appendChild(span)
        last_generated_span = span

    reset()

# reset ui state
def reset():
    continue_button.disabled = False
    another_button.disabled = False
    loading.classList.add("hidden")

# change language and reload model
def change_language(lang):
    global current_lang
    if lang != current_lang:
        current_lang = lang
        loading.classList.remove("hidden")
        continue_button.disabled = True
        another_button.disabled = True
        def reload(): load_model(lang); reset()
        js.setTimeout(create_proxy(reload), 100)

# expose to js
js.window.changeLanguage = change_language

# button proxies (owned)
continue_proxy = create_proxy(lambda e: generate_continuation(False))
another_proxy = create_proxy(lambda e: generate_continuation(True))
continue_button.onclick = continue_proxy
another_button.onclick = another_proxy

# init german model
load_model("de")