# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_inventory_system.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tino <tino@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/04 02:03:48 by tino              #+#    #+#              #
#    Updated: 2026/05/04 03:33:34 by tino             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def parse_input()->None:
	i = 1
	j = 0
	size = len(sys.argv)
	inventory=dict()

	while i < size:
		arg = sys.argv[i]
		if arg.count(':')==1:
			parts = arg.split(':')
			name = parts[0].strip()
			raw_count=parts[1].strip()
			if name in inventory.keys():
				print(f"Redundant item '{name}' - discarding")
				i += 1
				continue
			try:
				quantity = int(raw_count)
				inventory[name]=quantity
			except ValueError as e:
				print(f"Quantity error for '{name}': {e}")
		else:
			print("Format Error too many or no ':'")
		i+=1
	print(f"Got inventory {inventory}")
	print(f"Item List {inventory.keys()}")
	totalQuant=sum(inventory.values())
	print(f"Total quantity of the {len(inventory)} items is {totalQuant}")
	maxidx = 0
	minidx = 0
	min=list(inventory.values())[0]
	max=list(inventory.values())[0]

	while j<len(inventory):
		idxlist =list(inventory.keys())[j]
		valueidx= list(inventory.values())[j]
		ratio=float(valueidx/totalQuant)
		if min > valueidx:
			min = valueidx
			minidx=j
		print(f"Item {idxlist} represents {ratio * 100:.1f}%")
		if valueidx > max:
			max = valueidx
			maxidx=j
		j+=1
	print(f"The most abundent item is {list(inventory.keys())[maxidx]} with {list(inventory.values())[maxidx]}")
	print(f"The least abundent item is {list(inventory.keys())[minidx]} with {list(inventory.values())[minidx]}")
	inventory.update({"Milk":12})
	print(inventory)
if __name__ == "__main__":
	parse_input()
