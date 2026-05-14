# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  tournament.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: vsack <vsack@student.42vienna.com>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/14 22:45:49 by vsack           #+#    #+#               #
#  Updated: 2026/05/14 22:58:21 by vsack           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0 import AquaFactory, FlameFactory, CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AgressiveStrategy, DefensiveStrategy, BattleStrategy

water_maker = AquaFactory()
flame_maker = FlameFactory()
heal_maker = HealingCreatureFactory()
trans_maker = TransformCreatureFactory()
agressive = AgressiveStrategy()
normal = NormalStrategy()
defensive = DefensiveStrategy()
opponent = tuple[CreatureFactory, BattleStrategy]


def battle(roster: list[opponent]) -> None:
    for factory, strategy in roster:
        figher = factory.create_base()
