# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vsack <vsack@student.42vienna.com>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/01 20:18:27 by vsack             #+#    #+#              #
#    Updated: 2026/05/01 21:00:27 by vsack            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
	capSeed = seed_type.capitalize() + " seeds:"
	if unit == "packets":
		print(capSeed, quantity, "packets available")
	elif unit == "grams":
		print(capSeed, quantity, "grams total")
	elif unit == "area":
		print(capSeed, "covers", quantity, "square meters")
	else:
		print("Unknown unit type")
