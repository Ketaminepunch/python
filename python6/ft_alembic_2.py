# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_alembic_2.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vsack <vsack@student.42vienna.com>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/07 17:36:37 by vsack             #+#    #+#              #
#    Updated: 2026/05/07 18:01:32 by vsack            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import alchemy.elements

if __name__ == "__main__":
	print("=== Albemic 2 ===")
	print("Accessing alchemy/elements.py using 'import ...' structure")
	print(f"Testing create_earth: {alchemy.elements.create_earth()}")
