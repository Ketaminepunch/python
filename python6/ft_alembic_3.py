# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_alembic_3.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: vsack <vsack@student.42vienna.com>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/12 20:41:31 by vsack           #+#    #+#               #
#  Updated: 2026/05/12 20:41:49 by vsack           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from alchemy.elements import create_air

if __name__ == "__main__":
    print("=== Albemic 3 ===")
    print("Accessing alchemy/elements.py using "
          "'from ... import ...' structure")
    print(f"Testing create_air: {create_air()}")
