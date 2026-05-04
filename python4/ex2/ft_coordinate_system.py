# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_coordinate_system.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tino <tino@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/04 00:33:29 by tino              #+#    #+#              #
#    Updated: 2026/05/04 03:50:54 by tino             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import math

def get_player_pos()->tuple:
	"""Prompts for coordinates and returns a validated 3D tuple."""
	while True:
		try:
			line = input("Enter new player coordinates (x,y,z): ")
			parts = line.split(',')

			if len(parts) != 3:
				print("Error: Exactly three values (x,y,z) are required.")
				continue

			return tuple(float(p.strip()) for p in parts)


		except ValueError:
			print("Error: Please enter numeric values only.")

if __name__ == "__main__":

	player_coords = get_player_pos()

	print(f"\nCaptured Tuple: {player_coords}")
	x, y, z = player_coords
	print(f"Coordinate X: {x}, Coordinate Y: {y}, Coordinate Z: {z}")
	distanceToZero=math.sqrt((x-0)**2+(y-0)**2+(z-0)**2)
	print(f"Distance to center: {distanceToZero:.6f}")


