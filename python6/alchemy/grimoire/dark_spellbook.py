# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  dark_spellbook.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: vsack <vsack@student.42vienna.com>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/12 21:31:42 by vsack           #+#    #+#               #
#  Updated: 2026/05/12 21:33:00 by vsack           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    return (f"Spell recorded: {spell_name} "
            f"({validate_ingredients(ingredients)})")
