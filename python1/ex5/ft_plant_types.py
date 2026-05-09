# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_types.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vsack <vsack@student.42vienna.com>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/02 00:18:13 by vsack             #+#    #+#              #
#    Updated: 2026/05/08 21:47:59 by vsack            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    def __init__(self, name: str, age: int, height: float) -> None:
        self._name = name
        self._age = 0
        self._height = 0.0
        self.set_age(age)
        self.set_height(height)

    def set_age(self, value: int) -> None:
        if value >= 0:
            self._age = value
        else:
            print(f"{self._name}: Error, age can't be negative")

    def set_height(self, value: float) -> None:
        if value >= 0:
            self._height = value
        else:
            print(f"{self._name}: Error, height can't be negative")

    def grow(self, increment: float) -> None:
        if increment > 0:
            self._height += increment

        else:
            print("Growth increment must be positive")

    def age(self, days: int) -> None:
        self._age += days

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")


class Flower(Plant):
    def __init__(self, name: str, age: int, height: float, color: str,) -> None:
        super().__init__(name, age, height)
        self._color = color
        self._blooming = False

    def bloom(self) -> None:
        self._blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._blooming:
            print(f"The {self._name} is blooming beautifully!")
        else:
            print(f"The {self._name} is not blooming yet.")


class Tree(Plant):
    def __init__(
            self,
            name: str,
            age: int,
            height: float,
            trunk_diameter: int) -> None:
        super().__init__(name, age, height)
        self._thickness = trunk_diameter

    def shade(self) -> None:
        print(
            f"Tree {
                self._name} is now giving a shade of {
                self._height}cm long and {
                self._thickness}cm wide")

    def show(self) -> None:
        super().show()
        print(f"Trunk Diameter of {self._thickness}cm")


class Vegetable(Plant):
    def __init__(
            self,
            name: str,
            age: int,
            height: float,
            harvest_season: str,
            nutrition: int) -> None:
        super().__init__(name, age, height)
        self._season = harvest_season
        self._nutrition = nutrition

    def grow(self, increment: float) -> None:
        super().grow(increment)
        self._nutrition += 10

    def age(self, days: int) -> None:
        super().age(days)
        self._nutrition += 10 * days

    def show(self) -> None:
        super().show()
        print(f"Harvest Season: {self._season}")
        print(f"Nutritional Value: {self._nutrition}")


if __name__ == "__main__":
    print("=== Specialized Garden System ===")

    rose = Flower("Rose", 5, 15.2, "Red")
    print("=== Flower")
    rose.show()
    print("making it bloom")
    rose.bloom()
    rose.show()

    oak = Tree("Oak", 2500, 200, 15)
    print("=== Tree")
    oak.show()
    oak.shade()

    days = 12
    growthIncre = 5.2
    tomato = Vegetable("Tomato", 1, 4.4, "april", 0)
    print("=== Vegetable")
    tomato.show()
    print(
        f"Growing tomato for {days} days and its growing "
        f"{growthIncre}cm per day")
    tomato.grow(growthIncre)
    tomato.show()
