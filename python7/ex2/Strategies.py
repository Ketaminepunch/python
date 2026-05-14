# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Strategies.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: vsack <vsack@student.42vienna.com>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/14 22:17:12 by vsack           #+#    #+#               #
#  Updated: 2026/05/14 22:41:45 by vsack           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from abc import ABC, abstractmethod
from ex0 import Creature
from ex1 import HealCapability, TransformCapability


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, monster: Creature) -> str:
        pass

    @abstractmethod
    def is_valid(self, monster: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, monster: Creature) -> bool:
        return True

    def act(self, monster: Creature) -> str:
        return monster.attack()


class AgressiveStrategy(BattleStrategy):
    def is_valid(self, monster: Creature) -> bool:
        return isinstance(monster, TransformCapability)

    def act(self, monster: Creature) -> str:
        if not isinstance(monster, TransformCapability):
            raise TypeError(f"Invalid Strategy for {monster.name} "
                            f"lacks Transform capability.")
        return f"{monster.transform()}{monster.attack()}{monster.revert()}"


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, monster: Creature) -> bool:
        return isinstance(monster, HealCapability)

    def act(self, monster: Creature) -> str:
        if not isinstance(monster, HealCapability):
            raise TypeError(f"Invalid Strategy for {monster.name} "
                            f"lacks Heal capability.")
        return f"{monster.attack()}{monster.heal()}"
