extends Control

@onready var info_label = $InfoLabel
@onready var money_label = $MoneyLabel
@onready var small_btn = $HBoxContainer/SmallBlindBtn
@onready var big_btn = $HBoxContainer/BigBlindBtn
@onready var boss_btn = $HBoxContainer/BossBlindBtn

func _ready():
	update_view()

func update_view():
	info_label.text = "ANTE " + str(GameManager.current_stage)
	money_label.text = "$" + str(GameManager.current_money)
	
	var current_idx = GameManager.current_round_index
	var stage_mul = GameManager.current_stage
	
	# setup buttons
	setup_btn(small_btn, 0, "Small Blind", GameManager.round_config[0]["base_quota"] * stage_mul, current_idx)
	setup_btn(big_btn, 1, "Big Blind", GameManager.round_config[1]["base_quota"] * stage_mul, current_idx)
	setup_btn(boss_btn, 2, "BOSS", GameManager.round_config[2]["base_quota"] * stage_mul, current_idx)

func setup_btn(btn: Button, index: int, title: String, quota: int, current_idx: int):
	btn.text = "%s\nGoal: %d" % [title, quota]
	
	# logic: enable only the current round in sequence
	if index == current_idx:
		btn.disabled = false
		btn.modulate = Color.WHITE
	elif index < current_idx:
		btn.disabled = true
		btn.text += "\n(Completed)"
		btn.modulate = Color.GREEN
	else:
		btn.disabled = true
		btn.modulate = Color.DARK_GRAY

func _on_round_button_pressed():
	get_tree().change_scene_to_file("res://scenes/round.tscn")
