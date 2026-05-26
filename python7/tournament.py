# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  tournament.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: vsack <vsack@student.42vienna.com>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/14 22:45:49 by vsack           #+#    #+#               #
#  Updated: 2026/05/22 16:23:58 by vsack           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0 import AquaFactory, FlameFactory, CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (NormalStrategy, AgressiveStrategy,
                 DefensiveStrategy, BattleStrategy)


def battle(roster: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(roster)} opponents involved")
    for i in range(len(roster)):
        for j in range(i+1, len(roster)):
            f1, s1 = roster[i]
            f2, s2 = roster[j]

            c1 = f1.create_base()
            c2 = f2.create_base()

            print(f"\n* Battle {j}")
            print(f"{c1.describe()}\nVS.\n{c2.describe()}\nnow fight!")

            try:
                print(s1.act(c1))
                print(s2.act(c2))

            except Exception as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":
    water_maker = AquaFactory()
    flame_maker = FlameFactory()
    heal_maker = HealingCreatureFactory()
    trans_maker = TransformCreatureFactory()

    normal = NormalStrategy()
    aggressive = AgressiveStrategy()
    defensive = DefensiveStrategy()

    test_roster = [
        (water_maker, normal),
        (heal_maker, defensive),
        (trans_maker, aggressive)
    ]
    print("Tournament 0 (basic)\n")
    battle(test_roster)
