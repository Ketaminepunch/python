# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_achievement_tracker.py                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vsack <vsack@student.42vienna.com>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/04 19:00:21 by vsack             #+#    #+#              #
#    Updated: 2026/05/08 22:05:50 by vsack            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random


def gen_player_achievements(all_achievements: list) -> set:
    count = random.randint(15, len(all_achievements) - 5)
    return set(random.sample(all_achievements, count))


if __name__ == "__main__":
    all_possible = {
        'First Steps', 'Hello World', 'Syntax Savior', 'The Debugger',
        'Infinite Loop Survivor', 'Stack Overflow Expert', 'Pointers Master',
        'Memory Leak Fixer', 'Segfault Conqueror', 'Valgrind Warrior',
        'Makefile Architect', 'Git Hero', 'Merge Conflict Mediator',
        'Commit King', 'Push Enthusiast', 'Pull Request Professional',
        'Code Reviewer', 'Unit Test Titan', 'Integration Inspector',
        'Deployment Dragon', 'Scalability Sage', 'Performance Polisher',
        'Refactoring Ranger', 'Documentation Druid', 'README Writer',
        'Clean Code Crusader', 'Algorithm Alchemist', 'Data Structure Duke',
    }
    masterList = list(all_possible)
    LeeSin = gen_player_achievements(masterList)
    Katarina = gen_player_achievements(masterList)
    Garen = gen_player_achievements(masterList)
    Lissandra = gen_player_achievements(masterList)

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
    print("Only Garen has:", Garen.difference(Katarina, Garen, Lissandra))
    print("Only Lissandra has:", Lissandra.difference(LeeSin, Garen, Katarina))
    print("\nLee Sin is missing:", all_possible.difference(LeeSin))
    print("Katarina is missing:", all_possible.difference(Katarina))
    print("Garen is missing:", all_possible.difference(Garen))
    print("Lissandra is missing:", all_possible.difference(Lissandra))
