extends Control

func _ready():
	visible = false
	# Важно: Узлу PauseMenu в инспекторе поставь Process Mode = Always,
	# а остальной игре (корневой ноде Round) можно оставить Pausable.

func _input(event):
	if event.is_action_pressed("ui_cancel"): # ESC по умолчанию
		toggle_pause()

func toggle_pause():
	visible = not visible
	get_tree().paused = visible

func _on_resume_pressed():
	toggle_pause()

func _on_exit_pressed():
	toggle_pause() # Снимаем паузу перед выходом
	get_tree().change_scene_to_file("res://scenes/main_menu.tscn")
