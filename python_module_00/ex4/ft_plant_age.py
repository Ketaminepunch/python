# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_age.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: vsack <vsack@student.42vienna.com>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/12 16:56:49 by vsack           #+#    #+#               #
#  Updated: 2026/05/12 16:56:50 by vsack           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


def ft_plant_age() -> None:
    plantAge = int(input("Enter plant age in days: "))
    if plantAge > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
