# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_archive_creation.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: vsack <vsack@student.42vienna.com>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/12 17:00:33 by vsack           #+#    #+#               #
#  Updated: 2026/05/12 17:00:49 by vsack           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 ft_ancient_text.py <filename>")
        return
    filename: str = sys.argv[1]
    try:
        with open(filename, mode="r") as file:
            content: str = file.read()
            print("=== Cyber Archive Recovery ===")
            print(f"Accessing file '{filename}\n---\n")
            print(content)
            print(f"\n---\nFile '{filename}' closed\n")
        new_content: str = content.replace("\n", "#\n")
        if content and not content.endswith("\n"):
            new_content += "#"
        print("Transform Data:\n---\n")
        print(new_content)
        print("\n---")
        new_name: str = input("Enter file name (or empty):")
        if new_name == "":
            print("Not saving data.")
        else:
            try:
                with open(new_name, "w")as out_file:
                    out_file.write(new_content)
                print(
                    f"Saving data to '{new_name}'\n"
                    f"Data saved in file '{new_name}'")
            except PermissionError as e:
                print(f"Error opening file '{filename}': {e}")

    except FileNotFoundError as e:
        print(f"Error opening file '{filename}': {e}")
    except PermissionError as e:
        print(f"Error opening file '{filename}': {e}")
    except UnicodeDecodeError as e:
        print(f"Error opening file '{filename}': {e}")


if __name__ == "__main__":
    main()
