extends Node

@onready var quota_bar = $QuoteProgressBar
@onready var moves_label = $Moves
var current_quota = 100
var moves_left = 5

func _ready():
	quota_bar.max_value = current_quota
	update_ui()

func update_ui():
	quota_bar.value = 0  # just plug by now
	moves_label.text = "%d/%d" % [5 - moves_left, 5]
