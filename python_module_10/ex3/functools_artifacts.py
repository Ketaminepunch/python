from functools import reduce, partial, lru_cache, singledispatch
import operator
from collections.abc import Callable


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{element} {target} now does {power} damage"


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    operations = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": lambda a, b: a if a > b else b,
        "min": lambda a, b: a if a < b else b,
    }
    if operation not in operations:
        print("Unknown operation")
        return 0
    return reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire = partial(base_enchantment, power=50, element="Fire")
    ice = partial(base_enchantment, power=50, element="Ice")
    magma = partial(base_enchantment, power=50, element="Magma")
    return {'fire': fire, 'ice': ice, 'magma': magma}


if __name__ == "__main__":
    test_powers = [23, 18, 14, 8]
    spell_names = ['shield', 'fireball', 'earthquake', 'meteor']
    mage_names = ['Phoenix', 'Zara', 'Luna', 'Jordan', 'Sage', 'River']
    invalid_names = ['Jo', 'A', 'Alex123', 'Test@Name']
    print("Power levels:", *test_powers)
    print(f"Max: {spell_reducer(test_powers, "max")}")
    print(f"Min: {spell_reducer(test_powers, "min")}")
    print(f"Product: {spell_reducer(test_powers, "multiply")}")
    print(f"Sum: {spell_reducer(test_powers, "add")}")
    enchanters = partial_enchanter(base_enchantment)

    print(enchanters['fire'](target="Sword"))
    print(enchanters['ice'](target="Gun"))
    print(enchanters['magma'](target="Wand"))
