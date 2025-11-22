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
	if not FileAccess.file_exists("res://data/dictionary.jsonl"):
		printerr("dictionary file missing")
		return
		
	var file = FileAccess.open("res://data/dictionary.jsonl", FileAccess.READ)
	while file.get_position() < file.get_length():
		var line = file.get_line()
		var json = JSON.parse_string(line)
		
		# extract "word" field and ignore short words
		if json and "word" in json:
			var word = json["word"].to_lower()
			if word.length() >= 2:
				valid_words[word] = true
	
	print("dictionary loaded: ", valid_words.size())

func init_deck() -> void:
	deck.clear()
	# populate deck based on frequency counts
	for letter in letter_config:
		var count = letter_config[letter]["count"]
		for i in range(count):
			deck.append(letter)
	deck.shuffle()

func is_word_valid(word: String) -> bool:
	return valid_words.has(word.to_lower())

func get_hand(size: int) -> Array[String]:
	var hand: Array[String] = []
	for i in range(size):
		if deck.size() > 0:
			hand.append(deck.pop_back())
	return hand
