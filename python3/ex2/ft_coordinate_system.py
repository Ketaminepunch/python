# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_coordinate_system.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: vsack <vsack@student.42vienna.com>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/12 16:59:24 by vsack           #+#    #+#               #
#  Updated: 2026/05/12 16:59:25 by vsack           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import math


def get_player_pos() -> tuple[float, float, float]:
    """Prompts for coordinates and returns a validated 3D tuple."""
    while True:
        try:
            line = input("Enter new player coordinates (x,y,z): ")
            parts = line.split(",")

            if len(parts) != 3:
                print("Error: Exactly three values (x,y,z) are required.")
                continue

            return (
                float(parts[0].strip()),
                float(parts[1].strip()),
                float(parts[2].strip()),
            )

        except ValueError:
            print("Error: Please enter numeric values only.")


if __name__ == "__main__":

    player_coords = get_player_pos()

    print(f"\nCaptured Tuple: {player_coords}")
    x, y, z = player_coords
    print(f"Coordinate X: {x}, Coordinate Y: {y}, Coordinate Z: {z}")
    distanceToZero = math.sqrt((x - 0) ** 2 + (y - 0) ** 2 + (z - 0) ** 2)
    print(f"Distance to center: {distanceToZero:.6f}")
