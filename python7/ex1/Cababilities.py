# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Cababilities.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: vsack <vsack@student.42vienna.com>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/14 14:42:59 by vsack           #+#    #+#               #
#  Updated: 2026/05/14 15:10:38 by vsack           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from abc import ABC, abstractmethod
from ..ex0.Creature import Creature
from ..ex0.factory import CreatureFactory


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: Creature) -> str:
        pass


class TransformCapability(ABC):
    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Sproutling(Creature, HealCapability):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Grass")

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def heal(self, target: Creature) -> str:
        return f"{self.name} heals {target} for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Grass/Fairy")

    def attack(self) -> str:
        return f"{self.name} uses Dazzling gleam!"

    def heal(self, target: Creature) -> str:
        return f"{self.name} heals {target} for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Normal")
        self.transformed: bool = False

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} shifts into a sharper form"

    def attack(self) -> str:
        if self.transformed == True:
            return f"{self.name} performs a boosted attack"
        return f"{self.name} attacks normally"
