from functools import wraps
from collections.abc import Callable
from time import time, sleep
from typing import Any


def heal(target: str, power: int) -> str:
    return f"Heal spell heals {target} for {power} HP"


def freeze(target: str, power: int) -> str:
    sleep(0.067)
    return f"Freeze spell freezes {target} and does {power} damage"


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time()
        res = func(*args, **kwargs)
        end = time()
        print(f"Spell completed in {end-start:.3f} seconds")
        return res
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:

            for arg in args:
                if isinstance(arg, int):
                    power = arg
                    break
            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


@power_validator(20)
def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            i = 1
            for _ in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        f"Spell failed retrying..."
                        f"(attempt {i}/{max_attempts})")
                    i += 1
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


@retry_spell(3)
def unstable_spell(target: str, power: int) -> str:
    for _ in range(2):
        raise Exception("Spell unstable!")
    return f"Spell hit {target} for {power} damage"


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) > 2 and all(c.isspace() or c.isalpha() for c in name):
            return True
        return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} which {power} power"


if __name__ == "__main__":
    print("Testing spell timer...")
    timed_spell = spell_timer(freeze)
    print("Result:", timed_spell("Dragon", 50))

    print(fireball("Dragon", 50))
    print(fireball("Dragon", 5))
    print(unstable_spell("Your Mum", 67))
    mage = MageGuild()
    print(mage.validate_mage_name("...asd"))
    print(mage.validate_mage_name("Alfred"))
    print(mage.cast_spell("Lightning", 15))
    print(mage.cast_spell("Lightning", 5))
