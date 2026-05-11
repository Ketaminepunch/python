# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_different_errors.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vsack <vsack@student.42vienna.com>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/03 20:13:27 by vsack             #+#    #+#              #
#    Updated: 2026/05/11 16:56:57 by vsack            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1 / 0  # type: ignore
    elif operation_number == 2:
        open("non.txt")
    elif operation_number == 3:
        stri = "HELLO"
        n = 12
        n + stri  # type: ignore


def test_error_types() -> None:
    print("=== Garden Error Types")
    print("Testing operation 0...")
    try:
        garden_operations(0)
    except ValueError as e:
        print(f"Caught Value Error: {e}")
    print("Testing operation 1...")
    try:
        garden_operations(1)
    except ZeroDivisionError as e:
        print(f"Caught divide by zero error: {e}")
    print("Testing operation 2...")
    try:
        garden_operations(2)
    except FileNotFoundError as e:
        print(f"Caught FileNotFound Error: {e}")
    print("Testing operation 2...")
    try:
        garden_operations(3)
    except TypeError as e:
        print(f"Caught TypeError Error: {e}")
    print("Operation completed successfully\n")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
