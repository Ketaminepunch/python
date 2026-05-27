# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  recipes.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: vsack <vsack@student.42vienna.com>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/12 22:00:32 by vsack           #+#    #+#               #
#  Updated: 2026/05/13 22:03:55 by vsack           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
from ..elements import create_air
from .. import strength_potion
import elements as el


def lead_to_gold() -> str:
    return (f"Recipe transmuting Lead to Gold: brew '{create_air()}' and "
            f"{strength_potion()} mixed with '{el.create_fire()}'")
