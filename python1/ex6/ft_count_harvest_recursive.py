# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vsack <vsack@student.42vienna.com>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/01 20:12:59 by vsack             #+#    #+#              #
#    Updated: 2026/05/08 21:41:40 by vsack            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def harvest_helper(current: int, target: int) -> None:
    if current > target:
        print("Harvest time!")
        return
    print("Day:", current)
    harvest_helper(current + 1, target)


def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))
    harvest_helper(1, days)
