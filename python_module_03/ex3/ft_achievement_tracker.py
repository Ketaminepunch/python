# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_achievement_tracker.py                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: vsack <vsack@student.42vienna.com>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/12 16:59:27 by vsack           #+#    #+#               #
#  Updated: 2026/05/27 18:41:35 by vsack           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import random


def gen_player_achievements(all_achievements: list[str]) -> set[str]:
    count = random.randint(5, len(all_achievements) - 5)
    return set(random.sample(all_achievements, count))


if __name__ == "__main__":
    all_possible = [
        "First Steps",
        "Hello World",
        "Syntax Savior",
        "The Debugger",
        "Infinite Loop Survivor",
        "Stack Overflow Expert",
        "Pointers Master",
        "Memory Leak Fixer",
        "Segfault Conqueror",
        "Valgrind Warrior",
        "Makefile Architect",
        "Git Hero",
        "Merge Conflict Mediator",
    ]
    masterset = set(all_possible)
    LeeSin = gen_player_achievements(all_possible)
    Katarina = gen_player_achievements(all_possible)
    Garen = gen_player_achievements(all_possible)
    Lissandra = gen_player_achievements(all_possible)

    print("=== Achievement Tracker System ===\n")
    print(f"Player LeeSin: {LeeSin}")
    print(f"Player Katarina: {Katarina}")
    print(f"Player Garen: {Garen}")
    print(f"Player Lissandra: {Lissandra}")

    distinct = LeeSin.union(Katarina, Garen, Lissandra)
    print(f"All distinct achievements: {distinct}")
    common = LeeSin.intersection(Katarina, Garen, Lissandra)
    print(f"\nCommon achievements: {common}")
    print("\nOnly Lee Sin has:", LeeSin.difference(Katarina, Garen, Lissandra))
    print("Only Katarina has:", Katarina.difference(LeeSin, Garen, Lissandra))
    print("Only Garen has:", Garen.difference(Katarina, LeeSin, Lissandra))
    print("Only Lissandra has:", Lissandra.difference(LeeSin, Garen, Katarina))
    print("\nLee Sin is missing:", masterset.difference(LeeSin))
    print("Katarina is missing:", masterset.difference(Katarina))
    print("Garen is missing:", masterset.difference(Garen))
    print("Lissandra is missing:", masterset.difference(Lissandra))
