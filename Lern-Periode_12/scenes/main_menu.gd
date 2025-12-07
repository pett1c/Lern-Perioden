extends Control

func _on_start_pressed() -> void:
	# reset progression before new game
	GameManager.current_stage = 1
	GameManager.current_round_index = 0
	GameManager.current_money = 0
	
	get_tree().change_scene_to_file("res://scenes/stage_map.tscn")

func _on_exit_pressed() -> void:
	get_tree().quit()
