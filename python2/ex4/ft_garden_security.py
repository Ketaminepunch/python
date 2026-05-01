# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_security.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vsack <vsack@student.42vienna.com>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/01 22:42:02 by vsack             #+#    #+#              #
#    Updated: 2026/05/02 00:09:44 by vsack            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
	def __init__(self, name: str, age: int, height: float) -> None:
			self._name = name
			self._age = 0
			self._height = 0.0
			if age < 0:
				self.invalid_age()
			else:
				self._age = age
			if height < 0:
				self.invalid_height()
			else:
				self._height = height

	def get_height(self) -> float:
		return self._height

	def get_age(self) -> int:
		return self._age

	def set_age(self, value: int) -> None:
			if value < 0:
				self.invalid_age()
				print("Age update rejected")
			else:
				self._age = value
				print("Age updated:", value)

	def set_height(self, value: float) -> None:
		if value < 0:
			self.invalid_height()
			print("Height update rejected")
		else:
			self._height = value
			print("Height updated:", value)

	def show(self) -> None:
		print(
			f"Plant created: {self._name}: {self._height}cm, {self._age} days old\n")

	def invalid_height(self) -> None:
		print(f"{self._name}: Error, height can't be negative")

	def invalid_age(self) -> None:
		print(f"{self._name}: Error, age can't be negative")

	def show_state(self) -> None:
		print(f"Current state: {self._name}: {self._height}cm, {self._age} days old")


if __name__ == "__main__":
	print("=== GARDEN SECURITY SYSTEM ===")

	rose = Plant("Rose", 1, 22.54)
	rose.show()

	rose.set_height(-5.0)
	rose.set_age(-12)
	print()
	rose.set_height(123)
	rose.set_age(231)
	print()
	rose.show_state()
