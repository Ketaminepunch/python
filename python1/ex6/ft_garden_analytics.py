# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_analytics.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vsack <vsack@student.42vienna.com>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/02 01:44:24 by vsack             #+#    #+#              #
#    Updated: 2026/05/08 21:54:13 by vsack            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


class Plant:

    class _Analytics:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0
            self._shade_calls = 0

        def display(self, name: str) -> None:
            print(f" --- Statistics for {name} ---")
            print(
                f" Stats: {
                    self._grow_calls} grow, {
                    self._age_calls} age, {
                    self._show_calls} show")

    def __init__(self, name: str, age: int, height: float) -> None:
        self._name = name
        self._age = 0
        self._height = 0.0
        self._stats = self._Analytics()
        self.set_age(age)
        self.set_height(height)

    @staticmethod
    def age_over_year(age: int) -> None:
        if age > 365:
            print(f"Is {age} days more than a year? -> True")
        else:
            print(f"Is {age} days more than a year? -> False")

    @classmethod
    def anonymus(cls) -> "Plant":
        return cls(name="Unknown Plant", age=0, height=0)

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
        self._stats._grow_calls += 1
        if increment > 0:
            self._height += increment
        else:
            print("Growth increment must be positive")

    def age(self, days: int) -> None:
        self._stats._age_calls += 1
        if days < 0:
            print("Error cant grow by negative days")
        else:
            self._age += days

    def show(self) -> None:
        self._stats._show_calls += 1
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")


class Flower(Plant):
    def __init__(self, name: str, age: int, height: float, color: str,) -> None:
        super().__init__(name, age, height)
        self._color = color
        self._blooming = False

    def bloom(self) -> None:
        print(f" [Asking {self._name} to bloom]")
        self._blooming = True

    def grow(self, increment: float) -> None:
        super().grow(increment)

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._blooming:
            print(f" The {self._name} is blooming beautifully!")
        else:
            print(f" The {self._name} is not blooming yet.")


class Tree(Plant):
    class _Tree_Analytics(Plant._Analytics):
        def __init__(self) -> None:
            super().__init__()

        def display(self, name: str) -> None:
            super().display(name)
            print(f" Shade Calls: {self._shade_calls}")

    def __init__(
            self,
            name: str,
            age: int,
            height: float,
            trunk_diameter: int) -> None:
        super().__init__(name, age, height)
        self._thickness = trunk_diameter
        self._stats = self._Tree_Analytics()

    def shade(self) -> None:
        self._stats._shade_calls += 1
        print(f" [Asking {self._name} to give shade]")
        print(
            f" Tree {
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
        self._nutrition += 10

    def show(self) -> None:
        super().show()
        print(f"Harvest Season: {self._season}")
        print(f"Nutritional Value: {self._nutrition}")


class Seed(Flower):
    def __init__(self, name: str, age: int, height: float, color: str) -> None:
        super().__init__(name, age, height, color)
        self._seeds = 0

    def bloom(self) -> None:
        super().bloom()
        if self._blooming:
            self._seeds = round(self._height * 0.8)

    def grow(self, increment: float) -> None:
        super().grow(increment)

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seeds}")

    @staticmethod
    def seed_potential(height: float) -> int:
        return round(height * 0.8)


def display_statistics(plant_obj: Plant) -> None:
    if hasattr(plant_obj, '_stats'):
        plant_obj._stats.display(plant_obj._name)
    else:
        print("Object is not a valid Plant with analytics.")


if __name__ == "__main__":
    print("=== Garden Analytics Test ===")

    print("\n === Check year-old")
    test = Plant("test", 500, 200)
    test.age_over_year(test._age)
    test.age_over_year(20)

    print("\n === Flower")
    rose = Flower("Rose", 10, 15, "red")
    rose.show()
    display_statistics(rose)
    rose.grow(8.23)
    rose.bloom()
    rose.show()
    display_statistics(rose)

    print("\n === TREE")
    oak = Tree("oak", 365, 200, 5)
    oak.show()
    display_statistics(oak)
    oak.shade()
    display_statistics(oak)

    print("\n === SEED")
    sunflower = Seed("Sunflower", 80, 45, "Yellow")
    sunflower.show()
    print(" Making Sunflower age grow and bloom")
    sunflower.bloom()
    sunflower.age(1)
    sunflower.grow(30.5)
    sunflower.show()
    display_statistics(sunflower)

    print("\n === Anonymus")
    anon = Plant.anonymus()
    anon.show()
    display_statistics(anon)
