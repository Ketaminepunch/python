# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_analytics.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: vsack <vsack@student.42vienna.com>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/12 16:58:21 by vsack           #+#    #+#               #
#  Updated: 2026/05/12 16:58:21 by vsack           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


class Plant:
    class Analytics:
        def __init__(self) -> None:
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0
            self.shade_calls = 0

        def display(self, name: str) -> None:
            print(f" --- Statistics for {name} ---")
            print(
                f" Stats: {self.grow_calls} grow,"
                f"{self.age_calls} age, {self.show_calls} show"
            )

    def __init__(self, name: str, age: int, height: float) -> None:
        self.name = name
        self.age_val = 0  # Renamed to avoid collision with age() method
        self.height = 0.0
        self.stats = self.Analytics()
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
            self.age_val = value
        else:
            print(f"{self.name}: Error, age can't be negative")

    def set_height(self, value: float) -> None:
        if value >= 0:
            self.height = value
        else:
            print(f"{self.name}: Error, height can't be negative")

    def grow(self, increment: float) -> None:
        self.stats.grow_calls += 1
        if increment > 0:
            self.height += increment
        else:
            print("Growth increment must be positive")

    def age(self, days: int) -> None:
        self.stats.age_calls += 1
        if days < 0:
            print("Error cant grow by negative days")
        else:
            self.age_val += days

    def show(self) -> None:
        self.stats.show_calls += 1
        print(f"{self.name}: {self.height:.1f}cm, {self.age_val} days old")


class Flower(Plant):
    def __init__(
        self,
        name: str,
        age: int,
        height: float,
        color: str,
    ) -> None:
        super().__init__(name, age, height)
        self.color = color
        self.blooming = False

    def bloom(self) -> None:
        print(f" [Asking {self.name} to bloom]")
        self.blooming = True

    def grow(self, increment: float) -> None:
        super().grow(increment)

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.blooming:
            print(f" The {self.name} is blooming beautifully!")
        else:
            print(f" The {self.name} is not blooming yet.")


class Tree(Plant):
    class Tree_Analytics(Plant.Analytics):
        def __init__(self) -> None:
            super().__init__()

        def display(self, name: str) -> None:
            super().display(name)
            print(f" Shade Calls: {self.shade_calls}")

    def __init__(self, name: str, age: int, height: float,
                 trunk_diameter: int) -> None:
        super().__init__(name, age, height)
        self.thickness = trunk_diameter
        self.stats = self.Tree_Analytics()

    def shade(self) -> None:
        self.stats.shade_calls += 1
        print(f" [Asking {self.name} to give shade]")
        print(
            f" Tree {self.name} is now giving a shade of {self.height}"
            f"cm long and {self.thickness}cm wide"
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk Diameter of {self.thickness}cm")


class Vegetable(Plant):
    def __init__(
        self, name: str, age: int, height: float,
        harvest_season: str, nutrition: int
    ) -> None:
        super().__init__(name, age, height)
        self.season = harvest_season
        self.nutrition = nutrition

    def grow(self, increment: float) -> None:
        super().grow(increment)
        self.nutrition += 10

    def age(self, days: int) -> None:
        super().age(days)
        self.nutrition += 10

    def show(self) -> None:
        super().show()
        print(f"Harvest Season: {self.season}")
        print(f"Nutritional Value: {self.nutrition}")


class Seed(Flower):
    def __init__(self, name: str, age: int, height: float, color: str) -> None:
        super().__init__(name, age, height, color)
        self.seeds = 0

    def bloom(self) -> None:
        super().bloom()
        if self.blooming:
            self.seeds = round(self.height * 0.8)

    def grow(self, increment: float) -> None:
        super().grow(increment)

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seeds}")

    @staticmethod
    def seed_potential(height: float) -> int:
        return round(height * 0.8)


def display_statistics(plant_obj: Plant) -> None:
    if hasattr(plant_obj, "stats"):
        plant_obj.stats.display(plant_obj.name)
    else:
        print("Object is not a valid Plant with analytics.")


if __name__ == "__main__":
    print("=== Garden Analytics Test ===")

    print("\n === Check year-old")
    test = Plant("test", 500, 200)
    test.age_over_year(test.age_val)
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
