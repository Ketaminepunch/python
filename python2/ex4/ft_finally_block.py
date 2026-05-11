# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_finally_block.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vsack <vsack@student.42vienna.com>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/03 21:28:20 by vsack             #+#    #+#              #
#    Updated: 2026/05/11 18:06:00 by vsack            ###   ########.fr        #
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


def trigger_water_issue() -> None:
    raise WaterError("The water hose is disconnected")


def is_capitalized(text: str) -> bool:
    return text == str.capitalize(text)


def water_plant(plant_name: str) -> None:
    if not is_capitalized(plant_name):
        raise PlantError(f"'{plant_name}' is an invalid name for watering")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("=== Garden watering System ===\n")
    print("Testing valid plants")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        return
    finally:
        print("Closing watering system\n")
    print("Testing invalid plants")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("lettuce")
        water_plant("Carrots")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        return
    finally:
        print("Closing watering system\n")
        print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
