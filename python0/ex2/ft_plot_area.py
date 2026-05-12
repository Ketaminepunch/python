# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plot_area.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: vsack <vsack@student.42vienna.com>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/12 16:56:45 by vsack           #+#    #+#               #
#  Updated: 2026/05/12 16:56:45 by vsack           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


def ft_plot_area() -> None:
    lenght = int(input("Enter lenght: "))
    width = int(input("Enter width: "))
    area = width * lenght
    print("Plot area: ", area)
