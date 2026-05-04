# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_command_quest.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tino <tino@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/03 21:59:45 by vsack             #+#    #+#              #
#    Updated: 2026/05/04 01:03:00 by tino             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


def main()->None:
	print("=== Command Quest ===")
	print("Program Name:", sys.argv[0])
	i = 1
	total = len(sys.argv)
	if total == 1:
		print("No arguments provided!")
	else:
		print(f"Arguments received: {total - 1}")
		while i < total:
			print(f"Argument {i}: {sys.argv[i]}")
			i += 1


if __name__ == "__main__":
	main()
