# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_alembic_5.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vsack <vsack@student.42vienna.com>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/07 18:11:46 by vsack             #+#    #+#              #
#    Updated: 2026/05/11 18:43:16 by vsack            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from alchemy import create_air

if __name__ == "__main__":
    print("=== Alembic 5 ===")
    print("Accessing the alchemy module using 'from alchemy import create_air'")
    print(f"Testing 'create_air': {create_air()}")
