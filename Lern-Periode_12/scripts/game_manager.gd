var letters = {}
func _ready() -> void:
	var file = FileAccess.open("res://data/test_letters.json", FileAccess.READ)
	letters = JSON.parse_string(file.get_as_text())
	pass
