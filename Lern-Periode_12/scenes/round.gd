extends Node

@onready var quota_bar = $QuoteProgressBar
@onready var moves_label = $Moves
@onready var hand_container = $HandContainer
@onready var word_slots_container = $WordSlots
@onready var feedback_label = $FeedbackLabel

var current_quota = 100
var moves_left = 5
var current_hand_chars: Array[String] = []
var current_word_chars: Array[String] = []

var letter_scene = preload("res://scenes/letter.tscn")

func _ready():
	quota_bar.max_value = current_quota
	# wait for autoload to initialize
	await get_tree().process_frame 
	start_round()

func start_round():
	# deal initial cards
	current_hand_chars = GameManager.get_hand(8)
	render_hand()
	render_slots()
	update_ui()

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

func _on_submit_pressed():
	if current_word_chars.is_empty():
		return
		
	var word = "".join(current_word_chars)
	
	if GameManager.is_word_valid(word):
		print("valid word: ", word)
		feedback_label.text = "SUPER! " + word
		feedback_label.modulate = Color.GREEN
		
		# process turn logic
		moves_left -= 1
		current_word_chars.clear()
		
		# draw cards to fill hand
		var need = 8 - current_hand_chars.size()
		if need > 0:
			current_hand_chars.append_array(GameManager.get_hand(need))
			
		update_ui()
		render_hand()
		render_slots()
	else:
		print("invalid word")
		feedback_label.text = "NO SUCH WORD!"
		feedback_label.modulate = Color.RED

func update_ui():
	quota_bar.value = 0 
	moves_label.text = "%d/%d" % [moves_left, 5]
