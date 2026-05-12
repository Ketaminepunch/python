# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_transmutation_0.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: vsack <vsack@student.42vienna.com>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/12 20:55:02 by vsack           #+#    #+#               #
#  Updated: 2026/05/12 21:00:13 by vsack           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import alchemy.transmutation.recipes


if __name__ == "__main__":
    print("=== Transmutation 1 ===")
    print("Using file alchemy/transmutation/recipes.py directly")
    print(
        f"Testing lead to gold:"
        f" {alchemy.transmutation.recipes.lead_to_gold()}")
