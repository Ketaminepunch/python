# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_alembic_1.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: vsack <vsack@student.42vienna.com>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/12 20:41:24 by vsack           #+#    #+#               #
#  Updated: 2026/05/27 21:52:14 by vsack           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from elements import create_water

if __name__ == "__main__":
    print("=== Alembic 1 ===")
    print("Using: 'from ... import ...' structure to acces elements.py")
    print(f"Testing create_water: {create_water()}")
