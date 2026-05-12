# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_alembic_4.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: vsack <vsack@student.42vienna.com>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/12 20:41:34 by vsack           #+#    #+#               #
#  Updated: 2026/05/12 20:41:57 by vsack           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import alchemy

if __name__ == "__main__":
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")

    print(f"Testing 'create_air': {alchemy.create_air()}")
    print(
        "Now show that not all functions can be reached\nThis "
        "will raise an exception!"
    )
    print(alchemy.create_earth())  # type: ignore
