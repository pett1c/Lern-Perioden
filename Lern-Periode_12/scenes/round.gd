extends Node

# ui references
@onready var quota_bar = $MainLayout/RightSide/ProgressBarContainer/QuoteProgressBar
@onready var score_label = $MainLayout/LeftPanel/VBoxContainer/ScoreContainer/CurrentScoreLabel
@onready var quota_label = $MainLayout/LeftPanel/VBoxContainer/ScoreContainer/TargetScoreLabel
@onready var moves_label = $MainLayout/LeftPanel/MovesLabel
@onready var hand_container = $MainLayout/RightSide/HandArea/HandContainer
@onready var word_slots_container = $MainLayout/RightSide/PlayArea/WordSlots
@onready var feedback_label = $MainLayout/RightSide/PlayArea/FeedbackLabel
@onready var round_name_label = $MainLayout/LeftPanel/VBoxContainer/ScoreContainer/RoundNameLabel

# popups
@onready var win_popup = $CanvasLayer/WinPopup
@onready var win_money_label = $CanvasLayer/WinPopup/Panel/VBoxContainer/MoneyLabel
@onready var game_over_popup = $CanvasLayer/GameOverPopup # Создай простую панель Game Over

# round state
var current_quota = 0
var target_quota = 100
var moves_left = 10
var current_hand_chars: Array[String] = []
var current_word_chars: Array[String] = []

var letter_scene = preload("res://scenes/letter.tscn")

func _ready():
	# setup round based on manager
	target_quota = GameManager.get_current_quota()
	
	var r_info = GameManager.get_round_info()
	if r_info.get("is_boss", false):
		round_name_label.text = "BOSS: " + r_info["name"] + "\nDebuff: Words min 4 chars"
		round_name_label.modulate = Color.RED
	else:
		round_name_label.text = r_info["name"] + " (Ante " + str(GameManager.current_stage) + ")"
		round_name_label.modulate = Color.WHITE
		
	# init ui
	quota_bar.max_value = target_quota
	quota_bar.value = 0
	score_label.text = "0"
	quota_label.text = str(target_quota)
	
	# reset deck
	GameManager.init_deck()
	
	await get_tree().process_frame 
	start_round()

func start_round():
	current_hand_chars = GameManager.get_hand(8)
	render_hand()
	render_slots()
	update_ui()

# --- scoring logic ---

func calculate_score(word: String) -> int:
	var base_score = 0
	for char in word:
		if GameManager.letter_config.has(char):
			base_score += GameManager.letter_config[char]["score"]
	
	# basic length multiplier
	var multiplier = word.length() 
	return base_score * multiplier

func _on_submit_pressed():
	if current_word_chars.is_empty(): return
	var word = "".join(current_word_chars)
	
	# check boss debuff
	var r_info = GameManager.get_round_info()
	if r_info.get("is_boss", false) and r_info["debuff"] == "min_length_4":
		if word.length() < 4:
			show_floating_text("BOSS: TOO SHORT!", Color.RED)
			return

	# check validity
	if GameManager.is_word_valid(word):
		var word_score = calculate_score(word)
		
		animate_score_gain(word_score)
		
		# consume resources
		current_word_chars.clear()
		moves_left -= 1
		
		# refill hand
		draw_cards_to_full()
		
		render_hand()
		render_slots()
		
		update_ui()
		check_round_end()
	else:
		show_floating_text("Not a word!", Color.RED)

func _on_discard_pressed():
	if moves_left <= 0: return
	
	current_word_chars.clear()
	current_hand_chars.clear()
	draw_cards_to_full()
	
	moves_left -= 1
	show_floating_text("Discarded!", Color.YELLOW)
	
	render_hand()
	render_slots()
	update_ui()
	check_round_end()

# --- animations & feedback ---

func show_floating_text(text: String, color: Color):
	var lbl = Label.new()
	lbl.text = text
	lbl.modulate = color
	lbl.position = word_slots_container.global_position + Vector2(0, -40)
	lbl.add_theme_font_size_override("font_size", 24)
	add_child(lbl)
	
	var tween = create_tween()
	tween.tween_property(lbl, "position:y", lbl.position.y - 50, 0.8)
	tween.parallel().tween_property(lbl, "modulate:a", 0.0, 0.8)
	tween.tween_callback(lbl.queue_free)

func animate_score_gain(amount: int):
	show_floating_text("+%d" % amount, Color.GOLD)
	
	var old_score = current_quota
	current_quota += amount
	
	# tween number rollup
	var tween = create_tween()
	tween.tween_method(func(val): score_label.text = str(int(val)), old_score, current_quota, 0.5)
	
	# progress bar smooth update
	var bar_tween = create_tween()
	bar_tween.tween_property(quota_bar, "value", current_quota, 0.5).set_trans(Tween.TRANS_CUBIC)

# --- game end logic ---

func check_round_end():
	if current_quota >= target_quota:
		# win
		GameManager.complete_round_success(current_quota)
		win_money_label.text = "Reward: $" + str(GameManager.get_round_info()["reward"])
		win_popup.visible = true
		$HandArea.visible = false
		
	elif moves_left <= 0:
		# lose
		game_over_popup.visible = true

func _on_win_popup_shop_pressed():
	get_tree().change_scene_to_file("res://scenes/shop.tscn")

func _on_game_over_menu_pressed():
	get_tree().change_scene_to_file("res://scenes/main_menu.tscn")

# --- helper functions ---

func draw_cards_to_full():
	var need = 8 - current_hand_chars.size()
	if need > 0:
		current_hand_chars.append_array(GameManager.get_hand(need))

func update_ui():
	moves_label.text = "Hands: %d" % moves_left

func render_hand():
	for child in hand_container.get_children(): child.queue_free()
	for i in range(current_hand_chars.size()):
		var char = current_hand_chars[i]
		var btn = letter_scene.instantiate()
		hand_container.add_child(btn)
		btn.setup(char)
		btn.pressed.connect(_on_hand_letter_pressed.bind(i, char))

func render_slots():
	for child in word_slots_container.get_children(): child.queue_free()
	for i in range(current_word_chars.size()):
		var char = current_word_chars[i]
		var btn = letter_scene.instantiate()
		word_slots_container.add_child(btn)
		btn.setup(char)
		btn.pressed.connect(_on_slot_letter_pressed.bind(i, char))

func _on_hand_letter_pressed(index, char):
	current_hand_chars.remove_at(index)
	current_word_chars.append(char)
	render_hand()
	render_slots()

func _on_slot_letter_pressed(index, char):
	current_word_chars.remove_at(index)
	current_hand_chars.append(char)
	render_hand()
	render_slots()
