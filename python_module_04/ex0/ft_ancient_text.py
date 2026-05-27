# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_ancient_text.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: vsack <vsack@student.42vienna.com>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/12 17:00:29 by vsack           #+#    #+#               #
#  Updated: 2026/05/27 20:50:46 by vsack           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys
import typing


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 ft_ancient_text.py <filename>")
        return
    print("=== Cyber Archives Recovery ===")

    filename: str = sys.argv[1]
    print(f"Accessing file '{filename}'")

    try:
        file: typing.IO = open(filename, "r")
        content = file.read()
        print(content)
        file.close()
        print(f"\n---\nFile '{filename}' closed")
    except (FileNotFoundError, PermissionError, UnicodeDecodeError) as e:
        print(f"Error: opening file '{filename}': {e}")


if __name__ == "__main__":
    main()
