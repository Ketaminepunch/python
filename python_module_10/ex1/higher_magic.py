from collections.abc import Callable


def heal(target: str, power: int) -> str:
    return f"Heal spell heals {target} for {power} HP"


def freeze(target: str, power: int) -> str:
    return f"Freeze spell freezes {target} and does {power} damage"


def power_check(target: str, power: int) -> bool:
    return power > 20


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def multiply(target: str, power: int) -> str:
        return (base_spell(target, (power*multiplier)))
    return multiply


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def newspell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return newspell


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list[str]:
        return list(map(lambda s: s(target, power), spells))
    return sequence


if __name__ == "__main__":
    combined = spell_combiner(heal, freeze)
    result = combined("Dragon", 12)
    print(*result)
    gigafreeze = power_amplifier(freeze, 3)
    print(gigafreeze("Your mum", 140))
    condition = conditional_caster(power_check, freeze)
    print(condition("Bee", 52))
    sequence = spell_sequence([heal, freeze])
    result = sequence("Dragon", 50)
    print(*result)
