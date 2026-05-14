# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Factory2.py                                       :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: vsack <vsack@student.42vienna.com>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/14 15:42:03 by vsack           #+#    #+#               #
#  Updated: 2026/05/14 17:13:09 by vsack           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0 import Creature, CreatureFactory
from .Cababilities import Sproutling, Shiftling, Morphagon, Bloomelle


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
