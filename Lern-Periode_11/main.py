from pyodide.http import open_url
import markovify
import js
import re

# load the corpus
with open_url("./ru_corpus.txt") as f:
    raw_text = f.read()
    print(f"Debug: Corpus loaded, length={len(raw_text)}")

# build markov model
model = markovify.Text(raw_text, state_size=2, well_formed=True)

# get DOM elements
text_input = js.document.getElementById("text-input")
length_slider = js.document.getElementById("length-slider")
length_value = js.document.getElementById("length-value")
continue_button = js.document.getElementById("continue-button")
loading = js.document.getElementById("loading")

def update_length_value(*args):
    length_value.innerText = length_slider.value

length_slider.oninput = update_length_value
update_length_value()

def post_process(text):
    if not text:
        return "."
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'(\b\w+\b)(\s+\1){2,}', r'\1', text)  # remove word repetitions
    if not text.endswith(('.', '!', '?')):
        text += '.'
    return text.strip()

def generate_continuation(*args):
    continue_button.disabled = True
    loading.classList.remove("hidden")
    current_text = text_input.innerText.strip() or text_input.value.strip() or ""
    if not current_text:
        print("Debug: No input text detected!")
        reset()
        return
    
    word_limit = int(length_slider.value)
    generated_sentences = []
    total_words = 0
    max_tries = 50

    words = re.split(r'\s+', current_text.strip())
    print(f"Debug: Raw input='{current_text}', Split words={words}")

    # try different continuation strategies
    last_word = words[-1] if words else ""
    last_two_words = " ".join(words[-2:]) if len(words) >= 2 else ""
    last_three_words = " ".join(words[-3:]) if len(words) >= 3 else ""
    
    print(f"Debug: Last word='{last_word}', Last two='{last_two_words}', Last three='{last_three_words}'")
    print(f"Debug: Target word limit={word_limit}")

    # strategy 1: try to continue from last few words as context
    continuation_found = False
    attempts = 0
    
    # try with different context lengths and approaches
    for context in [last_three_words, last_two_words, last_word]:
        if continuation_found or attempts >= max_tries:
            break
            
        if not context:
            continue
            
        print(f"Debug: Trying context continuation with: '{context}'")
        
        # try multiple times with this context
        for i in range(15):
            try:
                # generate sentence and check if it naturally continues from our context
                sentence = model.make_sentence(tries=20)
                if sentence:
                    # check if generated sentence connects well with our context
                    sentence_words = sentence.split()
                    if len(sentence_words) > 0:
                        # simple heuristic: if any word from context appears in first few words of sentence
                        context_words = context.lower().split()
                        first_few = [w.lower() for w in sentence_words[:3]]
                        
                        if any(cw in first_few for cw in context_words) or i > 8:  # accept after some tries
                            sentence_word_count = len(sentence_words)
                            if total_words + sentence_word_count <= word_limit:
                                generated_sentences.append(sentence)
                                total_words += sentence_word_count
                                continuation_found = True
                                print(f"Debug: Found continuation: '{sentence[:50]}...' (words: {sentence_word_count})")
                                break
                            
                attempts += 1
            except Exception as e:
                print(f"Debug: Error in context continuation: {e}")
                attempts += 1
        
        if continuation_found:
            break

    # strategy 2: if no good continuation found, generate more sentences to reach word limit
    while total_words < word_limit and attempts < max_tries:
        try:
            remaining_words = word_limit - total_words
            print(f"Debug: Need {remaining_words} more words")
            
            # try to generate appropriate length sentence
            if remaining_words <= 10:
                sentence = model.make_short_sentence(remaining_words * 2, tries=15)
            else:
                sentence = model.make_sentence(tries=15)
                
            if sentence:
                sentence_words = len(sentence.split())
                if sentence_words <= remaining_words * 1.2:  # allow slight overflow
                    if total_words + sentence_words > word_limit:
                        # trim sentence to fit word limit
                        words_to_take = word_limit - total_words
                        sentence = ' '.join(sentence.split()[:words_to_take])
                        sentence_words = len(sentence.split())
                    
                    generated_sentences.append(sentence)
                    total_words += sentence_words
                    print(f"Debug: Added sentence: '{sentence[:50]}...' (words: {sentence_words})")
                    
                    if total_words >= word_limit:
                        break
            else:
                print("Debug: Could not generate sentence, breaking")
                break
                
        except Exception as e:
            print(f"Debug: Error generating additional content: {e}")
            break
        
        attempts += 1

    continuation = ' '.join(generated_sentences)
    continuation = post_process(continuation)
    print(f"Debug: Final continuation='{continuation}' (total words: {len(continuation.split())})")

    if continuation and len(continuation.split()) > 0:
        text_input.innerHTML += f' <span class="new-text">{continuation}</span>'
    
    reset()

def reset():
    continue_button.disabled = False
    loading.classList.add("hidden")

continue_button.onclick = generate_continuation