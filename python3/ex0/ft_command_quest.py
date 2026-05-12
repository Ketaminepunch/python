# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_command_quest.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: vsack <vsack@student.42vienna.com>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/12 16:59:19 by vsack           #+#    #+#               #
#  Updated: 2026/05/12 16:59:20 by vsack           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys


def main() -> None:
    print("=== Command Quest ===")
    print("Program Name:", sys.argv[0])
    i = 1
    total = len(sys.argv)
    if total == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {total - 1}")
        while i < total:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1


if __name__ == "__main__":
    main()
