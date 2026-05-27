# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_water_reminder.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: vsack <vsack@student.42vienna.com>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/12 16:56:51 by vsack           #+#    #+#               #
#  Updated: 2026/05/12 16:56:52 by vsack           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


def ft_water_reminder() -> None:
    waterTime = int(input("Days since last watering: "))
    if waterTime > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
