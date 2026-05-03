def get_player_pos():
	while True:
		raw_input = input("Enter coordinates (x, y, z): ")
		size = len(raw_input)
		i = 0
		current_val = ""
		parsed_count = 0
		coords = [0.0, 0.0, 0.0]
		is_valid = True

		while i < size:
			char = raw_input[i]

			if char == ',':
				if parsed_count >= 3:
					print("Error: Too many values provided.")
					is_valid = False
					break
				try:
					coords[parsed_count] = float(current_val)
					parsed_count += 1
					current_val = ""
				except ValueError:
					print(f"Error: Invalid numeric value near '{current_val}'.")
					is_valid = False
					break
			else:
				current_val += char

			i += 1

		if not is_valid:
			continue

		if parsed_count != 2:
			print("Error: Expected exactly 3 comma-separated values.")
			continue

		try:
			coords[parsed_count] = float(current_val)
			return (coords[0], coords[1], coords[2])
		except ValueError:
			print(f"Error: Invalid numeric value near '{current_val}'.")
			continue


def main():
	player_pos = get_player_pos()
	print(f"Valid coordinates registered: {player_pos}")


if __name__ == "__main__":
	main()
