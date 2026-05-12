# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  light_validator.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: vsack <vsack@student.42vienna.com>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/12 21:08:19 by vsack           #+#    #+#               #
#  Updated: 2026/05/12 21:51:49 by vsack           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    allowed = light_spell_allowed_ingredients()
    if any(item in ingredients for item in allowed):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
