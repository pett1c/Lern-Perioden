extends Node

# dictionary for fast word lookups
var valid_words: Dictionary = {}

# current deck and letter configuration
var deck: Array[String] = []

# german letter distribution and scores
var letter_config = {
	"a": {"count": 5, "score": 1}, "b": {"count": 2, "score": 3}, "c": {"count": 2, "score": 3},
	"d": {"count": 4, "score": 1}, "e": {"count": 15, "score": 1}, "f": {"count": 2, "score": 4},
	"g": {"count": 3, "score": 2}, "h": {"count": 4, "score": 2}, "i": {"count": 6, "score": 1},
	"j": {"count": 1, "score": 6}, "k": {"count": 2, "score": 4}, "l": {"count": 3, "score": 2},
	"m": {"count": 4, "score": 3}, "n": {"count": 9, "score": 1}, "o": {"count": 3, "score": 2},
	"p": {"count": 1, "score": 4}, "q": {"count": 1, "score": 10}, "r": {"count": 6, "score": 1},
	"s": {"count": 7, "score": 1}, "t": {"count": 6, "score": 1}, "u": {"count": 3, "score": 1},
	"v": {"count": 1, "score": 6}, "w": {"count": 2, "score": 3}, "x": {"count": 1, "score": 8},
	"y": {"count": 1, "score": 4}, "z": {"count": 2, "score": 3},
	"ä": {"count": 1, "score": 6}, "ö": {"count": 1, "score": 8}, "ü": {"count": 1, "score": 6}, "ß": {"count": 1, "score": 8}
}

func _ready() -> void:
	load_dictionary()
	init_deck()

func load_dictionary() -> void:
	# use new clean dictionary path
	const DICT_PATH = "res://data/clean_dictionary.json" 
	
	if not FileAccess.file_exists(DICT_PATH):
		printerr("clean dictionary file missing: ", DICT_PATH)
		return
		
	var file = FileAccess.open(DICT_PATH, FileAccess.READ)
	var content = file.get_as_text()
	
	# parse entire file as a single json array
	var parsed_json = JSON.parse_string(content)
	
	if parsed_json is Array:
		# convert array of words into a dictionary for o(1) lookup
		for word in parsed_json:
			valid_words[word] = true 
			
		print("dictionary loaded. clean words: ", valid_words.size())
	else:
		printerr("dictionary parsing error. ensure 'clean_dictionary.json' is a clean array.")

func init_deck() -> void:
	# build the initial deck based on letter_config counts
	deck.clear()
	for char in letter_config.keys():
		var count = letter_config[char]["count"]
		for _i in range(count):
			deck.append(char)
	deck.shuffle()
	print("deck initialized and shuffled.")

func get_hand(count: int) -> Array[String]:
	var hand = []
	for _i in range(count):
		if deck.is_empty():
			# refill deck from discard or reshuffle (future feature)
			break
		# draw a random card and remove it from the deck
		var char = deck.pop_at(randi() % deck.size())
		hand.append(char)
	return hand

func is_word_valid(word: String) -> bool:
	return valid_words.has(word)
