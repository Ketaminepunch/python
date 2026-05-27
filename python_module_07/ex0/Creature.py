from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, creature_type: str) -> None:
        self.name = self.__class__.__name__
        self.creature_type = creature_type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.creature_type} type Creature"


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__("Fire")

    def attack(self) -> str:
        return f"{self.name} used Ember"


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__("Fire/Flying")

    def attack(self) -> str:
        return f"{self.name} used Acrobatics"


class Aquabub(Creature):
    def __init__(self) -> None:
        super().__init__("Water")

    def attack(self) -> str:
        return f"{self.name} used Scald"


class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__("Water")

    def attack(self) -> str:
        return f"{self.name} used Surf"
