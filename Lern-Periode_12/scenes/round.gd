extends Node

# --- UI References ---
@onready var quota_bar = $MainLayout/RightSide/ProgressBarContainer/QuoteProgressBar
@onready var score_label = $MainLayout/LeftPanel/VBoxContainer/ScoreContainer/CurrentScoreLabel
@onready var quota_label = $MainLayout/LeftPanel/VBoxContainer/ScoreContainer/TargetScoreLabel
@onready var round_name_label = $MainLayout/LeftPanel/VBoxContainer/ScoreContainer/RoundNameLabel

# Ресурсы игрока
@onready var moves_label = $MainLayout/LeftPanel/VBoxContainer2/MovesLabel
@onready var discards_label = $MainLayout/LeftPanel/VBoxContainer2/DiscardsLabel

# Игровые зоны
@onready var hand_container = $MainLayout/RightSide/HandArea/HandContainer
@onready var word_slots_container = $MainLayout/RightSide/PlayArea/WordSlots
@onready var feedback_label = $MainLayout/RightSide/PlayArea/FeedbackLabel

# Popups & Menus
@onready var win_popup = $CanvasLayer/WinPopup
@onready var win_money_label = $CanvasLayer/WinPopup/Panel/VBoxContainer/MoneyLabel
@onready var game_over_popup = $CanvasLayer/GameOverPopup
@onready var pause_menu = $CanvasLayer/PauseMenu # Ссылка на твое новое меню паузы

# --- Round State ---
var current_quota = 0
var target_quota = 100

# Ресурсы (Баланс можно менять тут)
var moves_left = 4     # "Hands": Количество попыток сыграть слово
var discards_left = 5  # "Discards": Количество сбросов

var current_hand_chars: Array[String] = []
var current_word_chars: Array[String] = []

var letter_scene = preload("res://scenes/letter.tscn")

func _ready():
	# Инициализация раунда данными из GameManager
	target_quota = GameManager.get_current_quota()
	var r_info = GameManager.get_round_info()
	
	if round_name_label:
		round_name_label.text = r_info["name"]
	
	# Заполняем колоду и руку
	GameManager.init_deck()
	draw_cards_to_full()
	
	update_ui()
	render_hand()
	render_slots()

# --- Input Handling ---
func _input(event):
	if event.is_action_pressed("ui_cancel"): # ESC
		if pause_menu:
			pause_menu.toggle_pause()

# --- Button Signals ---

# Кнопка SHUFFLE
func _on_shuffle_pressed():
	current_hand_chars.shuffle()
	render_hand()

# Кнопка PLAY (SUBMIT)
func _on_submit_pressed():
	var word = "".join(current_word_chars).to_lower()
	
	if word.length() == 0:
		return

	if GameManager.is_word_valid(word):
		play_valid_word(word)
	else:
		feedback_label.text = "Unknown Word!"
		# Можно добавить звук ошибки или тряску экрана

# Кнопка DISCARD
func _on_discard_pressed():
	# Логика: сбрасываем карты, которые находятся в СЛОТАХ (Play Area)
	if current_word_chars.is_empty():
		feedback_label.text = "Place cards to discard!"
		return

	if discards_left > 0:
		discards_left -= 1
		
		# Карты сгорают, очищаем массив слова
		current_word_chars.clear()
		
		# Добираем новые карты в руку
		draw_cards_to_full()
		
		# Обновляем визуал
		render_slots()
		render_hand()
		update_ui()
		feedback_label.text = "Discarded!"
	else:
		feedback_label.text = "No discards left!"

# --- Core Game Logic ---

func play_valid_word(word: String):
	# 1. Считаем очки
	var score_data = calculate_score_complex(word)
	var total_points = score_data["total"]
	
	# 2. Обновляем прогресс
	current_quota += total_points
	moves_left -= 1
	
	# 3. Визуальный фидбек (Chips x Mult)
	feedback_label.text = "%s\nChips: %d x Mult: %d\nTotal: %d" % [
		word.to_upper(), 
		score_data["chips"], 
		score_data["mult"], 
		total_points
	]
	
	# 4. Очистка и проверка состояния
	current_word_chars.clear()
	render_slots()
	
	check_game_state()
	
	# Если игра продолжается - добираем карты
	if moves_left > 0 and current_quota < target_quota:
		draw_cards_to_full()
		render_hand()
		update_ui()

# Новая система подсчета: (Сумма очков букв) * (Длина слова - 1)
func calculate_score_complex(word: String) -> Dictionary:
	var chips = 0
	var mult = 0
	
	# Считаем Chips (база)
	for char in word:
		var data = GameManager.letter_config.get(char, {"score": 0})
		chips += data["score"]
	
	# Считаем Mult (множитель от длины)
	# 2 буквы = x1, 3 буквы = x2, 4 буквы = x3 и т.д.
	mult = max(1, word.length() - 1)
	
	# Тут можно добавить проверку на Joker-бонусы в будущем
	
	return {"chips": chips, "mult": mult, "total": chips * mult}

func check_game_state():
	update_ui()
	
	if current_quota >= target_quota:
		# WIN
		var reward = GameManager.get_round_info()["reward"]
		GameManager.current_money += reward
		
		if win_money_label:
			win_money_label.text = "Reward: $%d" % reward
			
		win_popup.visible = true
		$MainLayout.visible = false # Скрываем игровое поле
		
	elif moves_left <= 0:
		# GAME OVER
		game_over_popup.visible = true
		$MainLayout.visible = false

# --- Visuals & Data Helpers ---

func draw_cards_to_full():
	var need = 8 - current_hand_chars.size()
	if need > 0:
		current_hand_chars.append_array(GameManager.get_hand(need))

func update_ui():
	# Прогресс бар
	quota_bar.max_value = target_quota
	quota_bar.value = current_quota
	
	# Текстовые метки
	score_label.text = str(current_quota)
	quota_label.text = str(target_quota)
	
	# Счетчики ресурсов
	moves_label.text = "Hands: %d" % moves_left
	if discards_label:
		discards_label.text = "Discards: %d" % discards_left

func render_hand():
	# Очистка старых кнопок
	for child in hand_container.get_children(): 
		child.queue_free()
	
	# Создание новых
	for i in range(current_hand_chars.size()):
		var char = current_hand_chars[i]
		var btn = letter_scene.instantiate()
		hand_container.add_child(btn)
		btn.setup(char)
		# Привязываем нажатие: индекс в руке и сам символ
		btn.pressed.connect(_on_hand_letter_pressed.bind(i, char))

func render_slots():
	for child in word_slots_container.get_children(): 
		child.queue_free()
		
	for i in range(current_word_chars.size()):
		var char = current_word_chars[i]
		var btn = letter_scene.instantiate()
		word_slots_container.add_child(btn)
		btn.setup(char)
		# Привязываем нажатие: возвращаем карту в руку
		btn.pressed.connect(_on_slot_letter_pressed.bind(i, char))

# Перемещение карты: Рука -> Слот
func _on_hand_letter_pressed(index: int, char: String):
	current_hand_chars.remove_at(index)
	current_word_chars.append(char)
	render_hand()
	render_slots()

# Перемещение карты: Слот -> Рука
func _on_slot_letter_pressed(index: int, char: String):
	current_word_chars.remove_at(index)
	current_hand_chars.append(char)
	render_hand()
	render_slots()

# --- Scene Navigation ---

func _on_win_popup_shop_pressed():
	get_tree().change_scene_to_file("res://scenes/shop.tscn")

func _on_game_over_menu_pressed():
	get_tree().change_scene_to_file("res://scenes/main_menu.tscn")
