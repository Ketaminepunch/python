# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  construct.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: vsack <vsack@student.42vienna.com>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/17 15:56:02 by vsack           #+#    #+#               #
#  Updated: 2026/05/17 16:24:22 by vsack           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys
import os
import site


def in_venv() -> bool:
    return sys.prefix != sys.base_prefix


def main() -> None:
    if in_venv() is False:
        print("MATRIX STATUS: Youre still plugged in\n")
        print(f"Current python {sys.executable}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!\n"
              "The machines can see everything you install.\n")
        print("To enter the construct, run:\n"
              "python -m venv matrix_env\n"
              "source matrix_env/bin/activate #Unix")
        print(r"matrix_env\Scripts\activate #Windows")
        print("Then run this program again")
    else:
        print("MATRIX STATUS: Welcome to the construct")
        print(f"Current python {sys.executable}")
        print(f"Virtual environment: {os.path.basename(sys.prefix)}")
        print(f"Environment path:{os.environ.get('VIRTUAL_ENV')}")
        print("\nSUCCESS: You're in an isolated environment!\n"
              "Safe to install packages without affecting the global system\n")
        print(f"Package installation path:\n{site.getsitepackages()}")


if __name__ == "__main__":
    main()
