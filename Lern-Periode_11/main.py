from pyodide.http import open_url
import markovify
import js

# Load the corpus
with open_url("./ru_corpus.txt") as f:
    raw_text = f.read()

# Build the Markov model
model = markovify.Text(raw_text, state_size=2)

# Get DOM elements
text_input = js.document.getElementById("text-input")
length_slider = js.document.getElementById("length-slider")
length_value = js.document.getElementById("length-value")
continue_button = js.document.getElementById("continue-button")
loading = js.document.getElementById("loading")

def update_length_value(*args):
    length_value.innerText = length_slider.value

length_slider.oninput = update_length_value
update_length_value()

def generate_continuation(*args):
    continue_button.disabled = True
    loading.classList.remove("hidden")
    current_text = text_input.innerText.strip()
    if not current_text:
        reset()
        return
    word_limit = int(length_slider.value)
    generated_words = []
    beginning_words = current_text.split()[-model.state_size:]
    beginning = " ".join(beginning_words)
    tries = 0
    max_tries = 100
    while len(generated_words) < word_limit and tries < max_tries:
        try:
            sentence = model.make_sentence_with_start(beginning=beginning, tries=50)
            if sentence:
                new_words = sentence.split()
                generated_words.extend(new_words)
                beginning = " ".join(new_words[-model.state_size:])
            else:
                break
        except:
            sentence = model.make_short_sentence(word_limit * 5)
            if sentence:
                generated_words.extend(sentence.split())
            break
        tries += 1
    continuation = " ".join(generated_words[:word_limit])
    if continuation:
        text_input.innerHTML += ' <span class="new-text">' + continuation + '</span>'
    reset()

def reset():
    continue_button.disabled = False
    loading.classList.add("hidden")

continue_button.onclick = generate_continuation