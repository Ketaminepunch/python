# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  capacitor.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: vsack <vsack@student.42vienna.com>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/14 17:15:50 by vsack           #+#    #+#               #
#  Updated: 2026/05/14 22:14:10 by vsack           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex1 import (HealingCreatureFactory, TransformCreatureFactory,
                 CreatureFactory, HealCapability, TransformCapability)


def make_creature(factory: CreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(" base:")
    print(f"{base.describe()}")
    print(f"{base.attack()}")
    if isinstance(base, TransformCapability):
        print(base.transform())
        print(base.attack())
        print(base.revert())
    if isinstance(base, HealCapability):
        print(base.heal())
    print(" evolved:")
    print(f"{evolved.describe()}")
    print(f"{evolved.attack()}")
    if isinstance(evolved, TransformCapability):
        print(evolved.transform())
        print(evolved.attack())
        print(evolved.revert())
    if isinstance(evolved, HealCapability):
        print(evolved.heal())


if __name__ == "__main__":
    print("Testing Creature with healing capability")
    make_creature(HealingCreatureFactory())
    print("\nTesting Creature with transform capability")
    make_creature(TransformCreatureFactory())
