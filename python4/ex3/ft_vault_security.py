# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_vault_security.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vsack <vsack@student.42vienna.com>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/04 21:43:46 by vsack             #+#    #+#              #
#    Updated: 2026/05/08 21:15:24 by vsack            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import typing


def secure_archive(filename: str, action: str = "read",
                   content: typing.Optional[str] = None
                   ) -> typing.Tuple[bool, str]:

    try:
        if action == "read":
            with open(filename, "r") as file:
                read_content = file.read()
                return True, read_content
        elif action == "write":
            with open(filename, "w") as file:
                file.write(content if content is not None else "")
                return True, "Content successfully written to the file"

        else:
            return False, "Invalid Action"
    except Exception as e:
        return False, str(e)


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive'to read from a nonexistent file:")
    print(secure_archive("nothere", "read"))
    print("\nUsing 'secure_archive'to read from a inaccessible file:")
    print(secure_archive("permit.txt", "read"))
    print("\nUsing 'secure_archive'to read from a regular file:")
    read_result = secure_archive("test.txt", "read")
    print(read_result)
    print("\nUsing 'secure_archive'to write previous content to a new file:")
    print(secure_archive("newfile.txt", "write", read_result[1]))
