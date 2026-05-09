# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vsack <vsack@student.42vienna.com>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/01 19:41:40 by vsack             #+#    #+#              #
#    Updated: 2026/05/08 21:26:51 by vsack            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plant_age() -> None:
    plantAge = int(input("Enter plant age in days: "))
    if plantAge > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
