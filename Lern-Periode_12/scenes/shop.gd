extends Control

@onready var money_label = $CenterContainer/VBoxContainer/MoneyLabel

func _ready():
	money_label.text = "Current Money: $" + str(GameManager.current_money)

func _on_next_round_pressed():
	# advance progression and return to map
	GameManager.advance_progression()
	get_tree().change_scene_to_file("res://scenes/stage_map.tscn")
