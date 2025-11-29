@tool
extends EditorScript

const SOURCE_PATH = "res://data/dictionary.jsonl"
const TARGET_PATH = "res://data/clean_dictionary.json"

# defines all allowed lowercase german letters
const ALLOWED_CHARS = "abcdefghijklmnopqrstuvwxyzäöüß"

func _run():
	print("starting dictionary cleaning (removing duplicates and special characters)...")
	
	if not FileAccess.file_exists(SOURCE_PATH):
		printerr("source file missing: ", SOURCE_PATH)
		return

	var source_file = FileAccess.open(SOURCE_PATH, FileAccess.READ)
	var target_file = FileAccess.open(TARGET_PATH, FileAccess.WRITE)
	
	# use dictionary as a set for efficient uniqueness
	var unique_words_set = {}
	var processed_lines = 0
	
	while source_file.get_position() < source_file.get_length():
		var line = source_file.get_line()
		var json_result = JSON.parse_string(line)
		
		if json_result is Dictionary and "word" in json_result:
			var word = json_result["word"].to_lower()
			
			if word.length() >= 2:
				var is_clean = true
				
				# check word for disallowed characters (hyphens, spaces, etc.)
				for i in range(word.length()):
					if ALLOWED_CHARS.find(word[i]) == -1:
						is_clean = false
						break
				
				if is_clean:
					unique_words_set[word] = true
					
		processed_lines += 1
		
		# progress tracking
		if processed_lines % 50000 == 0:
			print("lines processed: %d | unique clean words found: %d" % [processed_lines, unique_words_set.size()])
	
	# convert dictionary keys to final array
	var final_list = unique_words_set.keys()
	final_list.sort()
	
	# save clean array to new json file
	target_file.store_string(JSON.stringify(final_list))
	
	print("--- finished ---")
	print("total lines processed: ", processed_lines)
	print("saved unique clean words: ", final_list.size())
	print("file created: ", TARGET_PATH)
