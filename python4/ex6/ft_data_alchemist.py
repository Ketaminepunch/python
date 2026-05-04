# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_data_alchemist.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tino <tino@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/04 04:17:12 by tino              #+#    #+#              #
#    Updated: 2026/05/04 04:49:38 by tino             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random


def alchemy()->None:
	lst = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john', 'kevin', 'Liam']
	print(f"Initial list of players: {lst}")
	onlyCap=[x for x in lst if	x[0].isupper()]
	print("Capitalized Names only:",onlyCap)
	capitalLst=[x.capitalize() for x in lst]
	print("List with all names capitalized:",capitalLst)
	inventory ={name: random.randrange(10,1000) for name in capitalLst}
	print("\nDictionary with Scores:",inventory)
	mean=sum(inventory.values())/len(lst)
	print(f"The mean score is: {mean:.2f}")
	highScore={name: x for name, x in inventory.items() if x > mean}
	print(f"High scores: {highScore}")
if __name__ == "__main__":
	alchemy()
