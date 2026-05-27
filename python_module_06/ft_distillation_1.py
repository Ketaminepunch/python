# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_distillation_1.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: vsack <vsack@student.42vienna.com>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/12 17:04:36 by vsack           #+#    #+#               #
#  Updated: 2026/05/27 21:59:33 by vsack           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import alchemy


def distillation() -> None:
    print("=== Distillation 0 ===")
    print("Using: 'import alchemy' structure to access potions alias")
    print(alchemy.potions.strength_potion())
    print(alchemy.heal())


if __name__ == "__main__":
    distillation()
