# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_growth.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vsack <vsack@student.42vienna.com>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/01 21:38:59 by vsack             #+#    #+#              #
#    Updated: 2026/05/11 16:37:31 by vsack            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


class Plant:
    name: str
    age: int
    height: float

    def grow(self) -> None:
        if self.name == "Rose":
            self.height += 0.8
        elif self.name == "Sunflower":
            self.height += 1.8
        elif self.name == "Potato":
            self.height += 0.2

    def age_up(self) -> None:
        self.age += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")


def simulate() -> None:
    counter = 1
    plant_1 = Plant()
    plant_1.name = "Sunflower"
    plant_1.age = 30
    plant_1.height = 9
    initialHeight = plant_1.height
    print("=== Garden Plant Growth ===")
    while counter <= 7:
        plant_1.show()
        print("=== Day", counter, "===")
        plant_1.grow()
        plant_1.age_up()
        counter += 1
    heightGain = round(plant_1.height - initialHeight, 2)
    print(f"{plant_1.name} grew {heightGain}cm this week")


def main() -> None:
    simulate()


if __name__ == "__main__":
    main()
