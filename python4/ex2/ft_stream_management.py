# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_stream_management.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vsack <vsack@student.42vienna.com>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/04 17:42:27 by vsack             #+#    #+#              #
#    Updated: 2026/05/11 18:35:00 by vsack            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


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
            print(f"Accessing file '{filename}'\n---\n")
            print(content)
            print(f"\n---\nFile '{filename}' closed\n")
        new_content: str = content.replace("\n", "#\n")
        if content and not content.endswith("\n"):
            new_content += "#"
        print("Transform Data:\n---\n")
        print(new_content)
        print("\n---")
        print("Enter file name (or empty):", end="")
        sys.stdout.flush()
        new_name = sys.stdin.readline().strip()
        if new_name == "":
            print("Not saving data.")
        else:
            try:
                with open(new_name, "w") as out_file:
                    out_file.write(new_content)
                print(f"Saving data to '{new_name}'")
                print(f"Data saved in file '{new_name}'")
            except PermissionError as e:
                print(f"[STDERR] Error opening file '{new_name}': {e}", file=sys.stderr)

    except FileNotFoundError as e:
        print(f"[STDERR] Error opening file '{filename}': {e}", file=sys.stderr)
    except PermissionError as e:
        print(f"[STDERR] Error opening file '{filename}': {e}", file=sys.stderr)
    except UnicodeDecodeError as e:
        print(f"[STDERR] Error opening file '{filename}': {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
