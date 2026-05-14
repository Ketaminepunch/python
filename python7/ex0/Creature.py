# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Creature.py                                       :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: vsack <vsack@student.42vienna.com>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/14 04:14:15 by vsack           #+#    #+#               #
#  Updated: 2026/05/14 14:51:35 by vsack           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, creature_type: str) -> None:
        self.name = name
        self.creature_type = creature_type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return (f"{self.name} is a "
                f"{self.creature_type} type Creature")


class Flameling(Creature):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Fire")

    def attack(self) -> str:
        return f"{self.name} used Ember"


class Pyrodon(Creature):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Fire/Flying")

    def attack(self) -> str:
        return f"{self.name} used Acrobatics"


class Torragon(Creature):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Water")

    def attack(self) -> str:
        return f"{self.name} used Surf"


class Aquabub(Creature):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Water")

    def attack(self) -> str:
        return f"{self.name} used Scald"
