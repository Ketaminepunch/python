# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_first_exception.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: vsack <vsack@student.42vienna.com>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/12 16:58:35 by vsack           #+#    #+#               #
#  Updated: 2026/05/12 16:58:35 by vsack           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature(input: str) -> None:

    print(f"Input Data is '{input}'")
    try:
        temp = input_temperature(input)
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print("Caught input_temperature Error:", e)


if __name__ == "__main__":

    print("=== Garden Temperature ===\n")
    test_temperature("25")
    print()
    test_temperature("abc")
    print("\nAll tests completed - program didnt crash")
