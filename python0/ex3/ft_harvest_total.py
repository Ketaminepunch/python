# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_harvest_total.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: vsack <vsack@student.42vienna.com>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/12 16:56:47 by vsack           #+#    #+#               #
#  Updated: 2026/05/12 16:56:47 by vsack           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


def ft_harvest_total() -> None:
    day1 = int(input("day 1 harvest: "))
    day2 = int(input("day 2 harvest: "))
    day3 = int(input("day 3 harvest: "))
    total = day1 + day2 + day3
    print("Total harvest:", total)
