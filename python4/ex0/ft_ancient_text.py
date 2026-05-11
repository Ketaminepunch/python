# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_ancient_text.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vsack <vsack@student.42vienna.com>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/04 17:27:29 by vsack             #+#    #+#              #
#    Updated: 2026/05/11 18:19:28 by vsack            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 ft_ancient_text.py <filename>")
        return
    filename: str = sys.argv[1]
    try:
        with open(file=filename, mode="r") as file:
            content: str = file.read()
            print("=== Cyber Archive Recovery ===")
            print(f"Accessing file '{filename}\n---\n")
            print(content)
            print(f"\n---\nFile '{filename}' closed")
    except FileNotFoundError as e:
        print(f"Error opening file '{filename}': {e}")
    except PermissionError as e:
        print(f"Error opening file '{filename}': {e}")
    except UnicodeDecodeError as e:
        print(f"Error opening file '{filename}': {e}")


if __name__ == "__main__":
    main()
