# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_data.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vsack <vsack@student.42vienna.com>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/01 21:16:06 by vsack             #+#    #+#              #
#    Updated: 2026/05/08 21:42:38 by vsack            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    name: str
    age: int
    height: float

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_manage_plants() -> None:
    plant_1 = Plant()
    plant_1.name = "Rose"
    plant_1.age = 23
    plant_1.height = 31

    plant_2 = Plant()
    plant_2.name = "Potato"
    plant_2.age = 12
    plant_2.height = 20

    plant_3 = Plant()
    plant_3.name = "Blueberry"
    plant_3.age = 90
    plant_3.height = 85.5

    plant_1.show()
    plant_2.show()
    plant_3.show()


def main() -> None:
    ft_manage_plants()


if __name__ == "__main__":
    main()
