# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_analytics.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tino <tino@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/02 01:44:24 by vsack             #+#    #+#              #
#    Updated: 2026/05/03 13:39:13 by tino             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


class Plant:
	def __init__(self, name: str, age: int, height: float) -> None:
		self._name = name
		self._age = 0
		self._height = 0.0
		self.set_age(age)
		self.set_height(height)

	@staticmethod
	def age_over_year(age):
		return age > 365

	@classmethod
	def anonymus(cls):
		return cls(name="unknown", age=0, height=0)

	def set_age(self, value: int) -> None:
		if value >= 0:
			self._age = value
		else:
			print(f"{self._name}: Error, age can't be negative")

	def set_height(self, value: float) -> None:
		if value >= 0:
			self._height = value
		else:
			print(f"{self._name}: Error, height can't be negative")

	def grow(self, increment: float, days: int) -> None:
		if increment > 0:
			self._height += increment * days
			self._age += days
		else:
			print("Growth increment must be positive")

	def show(self) -> None:
			print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")


class Flower(Plant):
	def __init__(self, name: str, age: int, height: float, color: str,) -> None:
		super().__init__(name, age, height)
		self._color = color
		self._blooming = False

	def bloom(self) -> None:
		self._blooming = True

	def grow(self, increment: float, days: int):
		super().grow()

	def show(self) -> None:
		super().show()
		print(f"Color: {self._color}")
		if self._blooming:
			print(f"The {self._name} is blooming beautifully!")
		else:
			print(f"The {self._name} is not blooming yet.")


class Tree(Plant):
	def __init__(self, name: str, age: int, height: float, trunk_diameter: int) -> None:
		super().__init__(name, age, height)
		self._thickness = trunk_diameter

	def shade(self) -> None:
		print(f"Tree {self._name} is now giving a shade of {self._height}cm long and {self._thickness}cm wide")

	def show(self) -> None:
		super().show()
		print(f"Trunk Diameter of {self._thickness}cm")


class Vegetable(Plant):
	def __init__(self, name: str, age: int, height: float, harvest_season: str, nutrition: int) -> None:
		super().__init__(name, age, height)
		self._season = harvest_season
		self._nutrition = nutrition

	def grow(self, increment: float, days: int) -> None:
		super().grow(increment, days)
		self._nutrition += 10

	def age(self) -> None:
		self._age += 1
		self._nutrition += 10

	def show(self) -> None:
		super().show()
		print(f"Harvest Season: {self._season}")
		print(f"Nutritional Value: {self._nutrition}")


class Seed(Flower):
	def __init__(self, name: str, age: int, height: float, color: str) -> None:
		super().__init__(name, age, height, color)
		self._seeds = 0


	def bloom(self):
		super().bloom()
		if self._blooming:
			self._seeds = round(self._height * 0.8)
	def grow(self, increment: float, days: int)-> None:
		super().grow()

	def show(self)->None:
		super().show()
		if self._blooming:
			print(f"Total Seeds: {self._seeds}")
		else :
			print(f"Seed Status: Growing (Flower must bloom)")

	@staticmethod
	def seed_potential(height:float)->int:
		return round(height*0.8)
if __name__ == "__main__":
	print("=== Seed Lifecycle Simulation ===")
	sunflower_seed = Seed("Sunflower", 1, 120.4, "Yellow")

	print("\n--- Pre-Bloom State ---")
	sunflower_seed.show()

	print("\n--- Triggering Bloom ---")
	sunflower_seed.bloom()

	print("\n--- Post-Bloom State ---")
	sunflower_seed.show()
