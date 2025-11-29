extends Node

# ui elements
@onready var quota_bar = $QuoteProgressBar
@onready var moves_label = $Moves
@onready var hand_container = $HandContainer
@onready var word_slots_container = $WordSlots
@onready var feedback_label = $FeedbackLabel
@onready var discard_button = $DiscardButton 

# round state variables
var current_quota = 0       # current score towards target
var target_quota = 100      # target score for this round
var moves_left = 5          # available moves
var current_hand_chars: Array[String] = []
var current_word_chars: Array[String] = []

var letter_scene = preload("res://scenes/letter.tscn")

func _ready():
	quota_bar.max_value = target_quota
	quota_bar.value = current_quota
	# wait for manager initialization
	await get_tree().process_frame 
	start_round()

func start_round():
	# deal initial cards
	current_hand_chars = GameManager.get_hand(8)
	render_hand()
	render_slots()
	update_ui()

# ==============================================================================
# gameplay logic: scoring, discard, round end
# ==============================================================================

# calculates the word score
func calculate_score(word: String) -> int:
	var base_score = 0
	
	# 1. sum base score of each letter
	for char in word:
		# get score from manager config
		if GameManager.letter_config.has(char):
			# letter upgrades/multipliers can be added here later
			base_score += GameManager.letter_config[char]["score"]
	
	# 2. apply word length bonus (multiplier)
	var word_length_multiplier = word.length()
	
	return base_score * word_length_multiplier

# handles word submission
func _on_submit_pressed():
	if current_word_chars.is_empty():
		return
		
	var word = "".join(current_word_chars)
	
	if GameManager.is_word_valid(word):
		var word_score = calculate_score(word)
		current_quota += word_score
		
		feedback_label.text = "super! %s (+%d)" % [word.to_upper(), word_score]
		feedback_label.modulate = Color.GREEN
		
		# clear slots and draw cards
		current_word_chars.clear()
		draw_cards_to_full()
		
		# use a move
		moves_left -= 1
		
		# update ui and check for round end
		update_ui()
		render_hand()
		render_slots()
		check_round_end()
	else:
		feedback_label.text = "not a word!"
		feedback_label.modulate = Color.RED
		# no move is consumed
		
# handles discarding the hand and redrawing
func _on_discard_pressed():
	if moves_left <= 0:
		feedback_label.text = "no moves left to discard!"
		feedback_label.modulate = Color.RED
		return
		
	# clear slots and current hand
	current_word_chars.clear()
	current_hand_chars.clear()
	
	# draw a full hand of new cards
	draw_cards_to_full()
	
	# use a move
	moves_left -= 1
	
	feedback_label.text = "cards discarded!"
	feedback_label.modulate = Color.YELLOW
	
	update_ui()
	render_hand()
	render_slots()
	check_round_end()
	
# checks for win/loss conditions
func check_round_end():
	# win condition: quota met
	if current_quota >= target_quota:
		game_won()
	# loss condition: no moves left and quota failed
	elif moves_left <= 0:
		game_over()

func game_won():
	feedback_label.text = "round won! going to shop..."
	feedback_label.modulate = Color.GOLD
	# get_tree().change_scene_to_file("res://scenes/shop.tscn")
	set_process_input(false)

func game_over():
	feedback_label.text = "game over! quota failed."
	feedback_label.modulate = Color.DARK_RED
	# get_tree().change_scene_to_file("res://scenes/game_over.tscn")
	set_process_input(false)

# ==============================================================================
# helper functions and ui rendering
# ==============================================================================

# draws cards to fill the hand (8 max)
func draw_cards_to_full():
	var need = 8 - current_hand_chars.size()
	if need > 0:
		current_hand_chars.append_array(GameManager.get_hand(need))

func update_ui():
	# update quota bar with animation
	var tween = create_tween()
	tween.tween_property(quota_bar, "value", current_quota, 0.5).set_trans(Tween.TRANS_CUBIC)
	
	# update moves counter
	moves_label.text = "%d/%d" % [moves_left, 5] 

func render_hand():
	# clear existing buttons
	for child in hand_container.get_children():
		child.queue_free()
	
	# recreate hand buttons
	for i in range(current_hand_chars.size()):
		var char = current_hand_chars[i]
		var letter_btn = letter_scene.instantiate()
		hand_container.add_child(letter_btn)
		letter_btn.setup(char)
		letter_btn.pressed.connect(_on_hand_letter_pressed.bind(i, char))

func render_slots():
	# clear existing slots
	for child in word_slots_container.get_children():
		child.queue_free()
		
	# recreate word slot buttons
	for i in range(current_word_chars.size()):
		var char = current_word_chars[i]
		var letter_btn = letter_scene.instantiate()
		word_slots_container.add_child(letter_btn)
		letter_btn.setup(char)
		letter_btn.pressed.connect(_on_slot_letter_pressed.bind(i, char))

func _on_hand_letter_pressed(index: int, char: String):
	# move from hand to word slots
	current_hand_chars.remove_at(index)
	current_word_chars.append(char)
	render_hand()
	render_slots()

func _on_slot_letter_pressed(index: int, char: String):
	# return from word slots to hand
	current_word_chars.remove_at(index)
	current_hand_chars.append(char)
	render_hand()
	render_slots()
