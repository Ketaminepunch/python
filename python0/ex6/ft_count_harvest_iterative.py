# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vsack <vsack@student.42vienna.com>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/01 19:47:36 by vsack             #+#    #+#              #
#    Updated: 2026/05/08 21:26:57 by vsack            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative() -> None:
    count = 1
    days = int(input("Days until harvest: "))
    while count <= days:
        print("Day", count)
        count += 1
    print("Harvest time!")
