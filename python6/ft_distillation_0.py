# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_distillation_0.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: vsack <vsack@student.42vienna.com>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/12 17:04:40 by vsack           #+#    #+#               #
#  Updated: 2026/05/12 17:04:41 by vsack           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from alchemy.potions import healing_potion, strength_potion


def distillation() -> None:
    print(healing_potion())
    print(strength_potion())


if __name__ == "__main__":
    print("=== Distillation 0 === \nDirect access to alchemy/potions.py")
    distillation()
