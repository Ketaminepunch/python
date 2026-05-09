# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    potions.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vsack <vsack@student.42vienna.com>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/07 18:13:34 by vsack             #+#    #+#              #
#    Updated: 2026/05/07 18:18:19 by vsack            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from alchemy.elements import create_earth, create_air


def healing_potion() -> str:
	return f"Healing potion brewed with '{elements.create_earth}' and {elements.create_air}"


if __name__ == "__main__":
	print(healing_potion())
