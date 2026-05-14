# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  battle.py                                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: vsack <vsack@student.42vienna.com>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/14 05:33:40 by vsack           #+#    #+#               #
#  Updated: 2026/05/14 15:50:05 by vsack           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0 import FlameFactory, AquaFactory, CreatureFactory


def verify_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(f"{base.describe()}\n{base.attack()}")
    print(f"{evolved.describe()}\n{evolved.attack()}")


def fight(c1: CreatureFactory, c2: CreatureFactory) -> None:
    print("Testing battle")
    f1 = c1.create_base()
    f2 = c2.create_base()

    print(f"{f1.describe()}\nvs.\n{f2.describe()}")
    print(f"{f1.attack()}\n{f2.attack()}")


if __name__ == "__main__":
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    verify_factory(flame_factory,)
    print()
    verify_factory(aqua_factory)
    print()
    fight(flame_factory, aqua_factory)
