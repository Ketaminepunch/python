
from .elements import create_air, create_earth
import elements as el


def healing_potion() -> str:
    return (f"Healing potion brewed with '{create_earth()}' "
            f"and '{create_air()}'")


def strength_potion() -> str:
    return (
        f"Strength potion brewed with '{el.create_fire()}' "
        f"and '{el.create_water()}'"
    )
