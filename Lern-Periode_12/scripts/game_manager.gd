extends Node

# dictionary for fast word lookups
var valid_words: Dictionary = {}

# current deck
var deck: Array[String] = []

# progression state
var current_money: int = 0
var current_stage: int = 1         # ante (stage) number
var current_round_index: int = 0   # 0 = small, 1 = big, 2 = boss

# round configuration
var round_config = {
	0: {"name": "Small Blind", "base_quota": 300, "reward": 3, "is_boss": false},
	1: {"name": "Big Blind",   "base_quota": 450, "reward": 4, "is_boss": false},
	2: {"name": "The Wall",    "base_quota": 600, "reward": 5, "is_boss": true, "debuff": "min_length_4"}
}

# letter distribution and scores
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

func load_dictionary() -> void:
	const DICT_PATH = "res://data/clean_dictionary.json" 
	
	if not FileAccess.file_exists(DICT_PATH):
		printerr("clean dictionary file missing: ", DICT_PATH)
		return
	
	var file = FileAccess.open(DICT_PATH, FileAccess.READ)
	var parsed_json = JSON.parse_string(file.get_as_text())
	
	if parsed_json is Array:
		for word in parsed_json:
			valid_words[word] = true 
		print("dictionary loaded. clean words: ", valid_words.size())
	else:
		printerr("dictionary parsing error.")

func init_deck() -> void:
	deck.clear()
	for char in letter_config.keys():
		var count = letter_config[char]["count"]
		for _i in range(count):
			deck.append(char)
	deck.shuffle()
	print("deck initialized and shuffled.")

func get_hand(count: int) -> Array[String]:
	var hand: Array[String] = []
	for _i in range(count):
		if deck.is_empty():
			break 
		var char = deck.pop_at(randi() % deck.size())
		hand.append(char)
	return hand

func is_word_valid(word: String) -> bool:
	return valid_words.has(word)

# --- progression functions ---

func get_current_quota() -> int:
	# formula: base quota * stage
	return round_config[current_round_index]["base_quota"] * current_stage

func get_round_info() -> Dictionary:
	return round_config[current_round_index]

func complete_round_success(_score_achieved: int):
	# add reward
	var reward = round_config[current_round_index]["reward"]
	current_money += reward
	print("round won! money: ", current_money)

func advance_progression():
	current_round_index += 1
	if current_round_index > 2:
		current_round_index = 0
		current_stage += 1 # ante up
