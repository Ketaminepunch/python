# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_archive_creation.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: vsack <vsack@student.42vienna.com>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/12 17:00:33 by vsack           #+#    #+#               #
#  Updated: 2026/05/27 21:04:02 by vsack           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys
import typing


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 ft_ancient_text.py <filename>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    filename: str = sys.argv[1]
    print(f"Accessing file '{filename}'")

    try:
        file: typing.IO = open(filename, "r")
        content = file.read()
        print(content)
        file.close()
        print(f"\n---\nFile '{filename}' closed")
        new_content: str = content.replace("\n", "#\n")
        if content and not content.endswith("\n"):
            new_content += "#"
        print("Transform Data:\n---\n")
        print(new_content)
        print("\n---")
        new_name: str = input("Enter file name (or empty for no save):")
        if new_name == "":
            print("Not saving data.")
        else:
            try:
                out_file: typing.IO = open(new_name, "w")
                out_file.write(new_content)
                print(
                    f"Saving data to '{new_name}'\n"
                    f"Data saved in file '{new_name}'")
                out_file.close()
            except PermissionError as e:
                print(f"Error opening file '{filename}': {e}")

    except (FileNotFoundError, PermissionError, UnicodeDecodeError) as e:
        print(f"Error opening file '{filename}': {e}")


if __name__ == "__main__":
    main()
