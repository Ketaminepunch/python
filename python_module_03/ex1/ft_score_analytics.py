# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_score_analytics.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: vsack <vsack@student.42vienna.com>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/12 16:59:22 by vsack           #+#    #+#               #
#  Updated: 2026/05/27 18:06:47 by vsack           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys


class InvalidInput(Exception):
    def __init__(self, message: str = "An Error occurred") -> None:
        super().__init__(message)


def empty_args() -> None:
    raise InvalidInput(
        "No scores provided."
        "Usage: python3 ft_score_analytics.py <score1> <score2> ..."
    )


def main() -> None:
    sys.tracebacklimit = 0
    size = len(sys.argv)

    if size < 2:
        empty_args()
        return

    valid_count = 0
    i = 1

    while i < size:
        try:
            int(sys.argv[i])
            valid_count += 1
        except ValueError:
            print(f"Invalid Input: {sys.argv[i]}")
        i += 1

    if valid_count == 0:
        empty_args()
        return

    lst = [0] * valid_count
    i = 1
    idx = 0

    while i < size:
        try:
            lst[idx] = int(sys.argv[i])
            idx += 1
        except ValueError:
            pass
        i += 1
    average = sum(lst)/valid_count
    print(f"Scores processed: {lst}")
    print("Total players:", valid_count)
    print("Total score:", sum(lst))
    print(f"Average score: {average:.2f}")
    print("High score:", max(lst))
    print("Low score:", min(lst))
    print("Score range:", max(lst) - min(lst))


if __name__ == "__main__":
    main()
