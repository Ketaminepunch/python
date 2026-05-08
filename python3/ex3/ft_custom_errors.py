# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_custom_errors.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vsack <vsack@student.42vienna.com>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/03 20:55:39 by vsack             #+#    #+#              #
#    Updated: 2026/05/08 22:14:52 by vsack            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class GardenError(Exception):
    def __init__(self, message: str = "An Error occurred") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown Plant Error occurred") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown Water Error occurred") -> None:
        super().__init__(message)


def trigger_plant_issue() -> None:
    raise PlantError("The tomato is wilting")


def trigger_water_issue() -> None:
    raise WaterError("The water hose is disconnected")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    try:
        trigger_plant_issue()
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")
    print("Testing WaterError...")
    try:
        trigger_water_issue()
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")
    print("Testing caching all GardenErrors...")
    try:
        trigger_plant_issue()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        trigger_water_issue()
    except GardenError as e:
        print(f"Caught GardenError: {e}\n")
    print("All custom error types work correctly")


if __name__ == "__main__":
    test_custom_errors()
