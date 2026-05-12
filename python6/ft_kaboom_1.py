# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_kaboom_1.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: vsack <vsack@student.42vienna.com>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/12 21:54:04 by vsack           #+#    #+#               #
#  Updated: 2026/05/12 21:58:47 by vsack           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


if __name__ == "__main__":
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    from alchemy.grimoire.dark_spellbook import dark_spell_record
    print(dark_spell_record("NOOO", "frog"))
