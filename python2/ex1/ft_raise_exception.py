# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_raise_exception.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vsack <vsack@student.42vienna.com>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/03 19:16:01 by vsack             #+#    #+#              #
#    Updated: 2026/05/08 21:25:02 by vsack            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def input_temperature(temp_str: str) -> int | None:
    if int(temp_str) >= 0 and int(temp_str) < 41:
        return int(temp_str)
    elif int(temp_str) < 0:
        raise ValueError(f"{temp_str}°C is too cold. Minimum is 0°C")
    elif int(temp_str) > 40:
        raise ValueError(f"{temp_str}°C is too hot. Maximum is 40°C")
    else:
        return 0


def test_temperature() -> None:

    print("=== Garden Temperature ===\n")
    print("Input Data is '25'")
    try:
        temp = input_temperature("25")
        print(f"Temperature is now {temp}°C\n")
    except ValueError as e:
        print(f"Caught input_temperature Error:{e}\n")
    print("Input Data is 'abc'")
    try:
        temp = input_temperature("abc")
        print(f"Temperature is now {temp}°C\n")
    except ValueError as e:
        print(f"Caught input_temperature Error: {e}\n")
    print("Input Data is '100'")
    try:
        temp = input_temperature("100")
        print(f"Temperature is now {temp}°C\n")
    except ValueError as e:
        print(f"Caught input_temperature Error: {e}\n")
    print("Input Data is '-50'")
    try:
        temp = input_temperature("-50")
        print(f"Temperature is now {temp}°C\n")
    except ValueError as e:
        print(f"Caught input_temperature Error: {e}\n")
    print("\nAll tests completed - program didnt crash")


if __name__ == "__main__":
    test_temperature()
