extends TextureButton

@onready var char_label = $CharLabel
@onready var weight_label = $WeightLabel

var char_value: String = ""
var letter_data: Dictionary = {}

func setup(character: String):
	char_value = character
	
	# retrieve score data from manager
	if GameManager.letter_config.has(character):
		letter_data = GameManager.letter_config[character]
	
	char_label.text = character.to_upper()
	
	# display score if label exists
	if letter_data.has("score") and weight_label:
		weight_label.text = str(letter_data["score"])
	
	# center pivot for scaling effects
	pivot_offset = size / 2

func _ready():
	# pop-in animation
	scale = Vector2.ZERO
	var tween = create_tween()
	tween.tween_property(self, "scale", Vector2.ONE, 0.3).set_trans(Tween.TRANS_BACK).set_ease(Tween.EASE_OUT)
