# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plot_area.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vsack <vsack@student.42vienna.com>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/01 19:26:57 by vsack             #+#    #+#              #
#    Updated: 2026/05/08 21:26:42 by vsack            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plot_area() -> None:
    lenght = int(input("Enter lenght: "))
    width = int(input("Enter width: "))
    area = width * lenght
    print("Plot area: ", area)
