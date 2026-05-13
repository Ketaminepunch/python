# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  light_spellbook.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: vsack <vsack@student.42vienna.com>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/12 21:04:49 by vsack           #+#    #+#               #
#  Updated: 2026/05/13 22:04:00 by vsack           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    valstr = validate_ingredients(ingredients)
    if valstr.endswith("VALID"):
        return (f"Spell recorded: {spell_name} ({valstr})")
    return (f"Spell not recorded: {spell_name} ({valstr})")
