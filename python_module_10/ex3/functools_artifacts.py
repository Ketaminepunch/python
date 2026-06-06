from functools import reduce, partial, lru_cache, singledispatch
import operator
from collections.abc import Callable
from typing import Any
from time import time


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{element} {target} now does {power} damage"


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    operations: dict[str, Callable[[Any, Any], Any]] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }
    if operation not in operations:
        print("Unknown operation")
        return 0
    return reduce(operations[operation], spells)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def cast(spell: Any) -> str:
        return "Unknown spell type"

    @cast.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @cast.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @cast.register(list)
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"
    return cast


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n-1)+memoized_fibonacci(n-2)


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
    print("\nTesting fibonacci")
    start = time()
    print("500th fibonnaci number:", memoized_fibonacci(100))
    end = time()
    print(f"Time taken first: {end-start}")
    start = time()
    print("500th fibonnaci number:", memoized_fibonacci(200))
    end = time()
    print(f"Time taken second: {end-start}")

    print("\nTesting spell dispatcher:")
    dispatch = spell_dispatcher()
    print(dispatch(42))
    print(dispatch("fireball"))
    print(dispatch([1, 2, 3]))
    print(dispatch(3.14))
