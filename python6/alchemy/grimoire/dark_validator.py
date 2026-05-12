# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  dark_validator.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: vsack <vsack@student.42vienna.com>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/12 21:32:10 by vsack           #+#    #+#               #
#  Updated: 2026/05/12 21:33:18 by vsack           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    for e in allowed:
        if e == ingredients:
            return f"{ingredients}-VALID"
    return "INVALID"
