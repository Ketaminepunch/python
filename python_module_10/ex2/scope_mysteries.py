from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    power = initial_power

    def accumulate(amount: int) -> int:
        nonlocal power
        power += amount
        return power

    return accumulate


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant(item: str) -> str:
        return f"{enchantment_type} {item}"
    return enchant


def memory_vault() -> dict[str, Callable]:
    storage: dict = {}

    def store(key: Any, value: Any) -> None:
        storage[key] = value

    def recall(key: Any) -> Any:
        return storage.get(key, "Memory not found")

    return {'store': store, 'recall': recall}


if __name__ == "__main__":
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter1:{counter_a()}\ncounter1:{counter_a()}"
          f"\ncounter2:{counter_b()}")
    powera = spell_accumulator(100)
    powerb = spell_accumulator(100)

    print(f"Base 100, add 20: {powera(20)}\n"
          f"Base 100, add 50: {powerb(50)}")
    enchantment_types = ['Frozen', 'Flaming', 'Dark']
    items_to_enchant = ['Shield', 'Staff', 'Armor', 'Ring']
    enchant1 = enchantment_factory("Pulsing")
    print(enchant1("Sword"))
    print(enchantment_factory("Shield")("Sharpness"))
    memory = memory_vault()
    memory['store']('secret', "I am a secret")
    print(memory['recall']('secret'))
    print(memory['recall']('nope'))
