# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_factory.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vsack <vsack@student.42vienna.com>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/01 22:20:30 by vsack             #+#    #+#              #
#    Updated: 2026/05/08 21:43:01 by vsack            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    name: str
    age: int
    height: float

    def __init__(self, name: str, age: int, height: float) -> None:
        self.name = name
        self.age = age
        self.height = height

    def grow(self, increment: float) -> None:
        self.height += increment
        self.age += 1

    def show(self) -> None:
        print(f"Created: {self.name}: {self.height:.1f}cm, {self.age} days old")


garden = [
    Plant("Rose", 12, 14.3),
    Plant("Potato", 2, 1.4),
    Plant("Apple Tree", 1242, 2000.321),
    Plant("Sunflower", 80, 88),
    Plant("Pumpkin", 5, 0.4)
]
print("=== Plant Factory Output")
for plant in garden:
    plant.show()
