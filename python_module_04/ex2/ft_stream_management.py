# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_stream_management.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: vsack <vsack@student.42vienna.com>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/12 17:01:23 by vsack           #+#    #+#               #
#  Updated: 2026/05/27 21:17:57 by vsack           ###   ########.fr        #
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
    try:
        file: typing.IO = open(filename, "r")
        content: str = file.read()
        print(f"Accessing file '{filename}'\n---\n")
        print(content)
        file.close()
        print(f"\n---\nFile '{filename}' closed\n")
        new_content: str = content.replace("\n", "#\n")
        if content and not content.endswith("\n"):
            new_content += "#"
        print("Transform Data:\n---\n")
        print(new_content)
        print("\n---")
        print("Enter file name (or empty for no save):", end="")
        sys.stdout.flush()
        new_name = sys.stdin.readline().strip("\n")
        if new_name == "":
            print("Not saving data.")
        else:
            try:
                out_file: typing.IO = open(new_name, "w")
                out_file.write(new_content)
                print(f"Saving data to '{new_name}'")
                print(f"Data saved in file '{new_name}'")
                out_file.close()
            except PermissionError as e:
                print(f"[STDERR] Error opening file '{new_name}': {e}",
                      file=sys.stderr)

    except FileNotFoundError as e:
        print(
            f"[STDERR] Error opening file '{filename}': {e}", file=sys.stderr)
    except PermissionError as e:
        print(
            f"[STDERR] Error opening file '{filename}': {e}", file=sys.stderr)
    except UnicodeDecodeError as e:
        print(
            f"[STDERR] Error opening file '{filename}': {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
