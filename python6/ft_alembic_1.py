# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_alembic_1.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vsack <vsack@student.42vienna.com>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/07 17:27:51 by vsack             #+#    #+#              #
#    Updated: 2026/05/11 18:43:05 by vsack            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from elements import create_water

if __name__ == "__main__":
    print("=== Albemic 1 ===")
    print("Using: 'from ... import ...' structure to acces elements.py")
    print(f"Testing create_water: {create_water()}")
