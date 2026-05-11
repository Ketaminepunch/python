# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vsack <vsack@student.42vienna.com>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/01 19:44:48 by vsack             #+#    #+#              #
#    Updated: 2026/05/11 16:37:10 by vsack            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def ft_water_reminder() -> None:
    waterTime = int(input("Days since last watering: "))
    if waterTime > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
