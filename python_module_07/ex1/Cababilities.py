# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Cababilities.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: vsack <vsack@student.42vienna.com>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/14 14:42:59 by vsack           #+#    #+#               #
#  Updated: 2026/05/27 22:03:59 by vsack           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from abc import ABC, abstractmethod
from ex0 import Creature


class HealCapability(ABC):
    @abstractmethod
    def heal(self) -> str:
        pass


class TransformCapability(ABC):
    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Grass")

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def heal(self) -> str:
        return f"{self.name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Grass/Fairy")

    def attack(self) -> str:
        return f"{self.name} uses Dazzling gleam!"

    def heal(self) -> str:
        return f"{self.name} heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Normal")
        self.transformed: bool = False

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} shifts into a sharper form!"

    def attack(self) -> str:
        if self.transformed:
            return f"{self.name} performs a boosted attack!"
        return f"{self.name} attacks normally."

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} reverts to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Normal/Dragon")
        self.transformed: bool = False

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} morphs into a dragonic battle form!"

    def attack(self) -> str:
        if self.transformed:
            return f"{self.name}  unleashes a devastating morph strike!"
        return f"{self.name} attacks normally."

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} stabilizes its form."
