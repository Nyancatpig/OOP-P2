'''
File: ooptest.py
Description: A brief description of this Python module.
Author: Bailey Csortan
StudentID: 110409234
EmailID: csoby001
This is my own work as defined by the University's Academic Misconduct Policy.
'''

import oopmain

tower = oopmain.Laboratory([], ["Irit", "Avantoe", "Irit", "Avantoe"], ["Eye of Newt", "Eye of Newt"])
magnificus = oopmain.Alchemist(45, 60, 82, 85, 34, 27, tower)
# print(magnificus.getLaboratory().__doc__)

# leshy = oopmain.Alchemist(103, 35, 66, 75, 34, 56, tower)
# print(leshy.getLaboratory().__doc__)

# magnificus.mixPotion("Extreme Attack")
# magnificus.mixPotion("Super Attack")
# magnificus.mixPotion("Extreme Attack")
# magnificus.mixPotion("Extreme Attack")

print(f"Array Contains: {len(magnificus.getLaboratory()._Laboratory__potions)} ---------------------------------------------")
magnificus.mixPotion("Super Attack")
print(f"Array Contains: {len(magnificus.getLaboratory()._Laboratory__potions)} ---------------------------------------------")
magnificus.mixPotion("Super Attack")
print(f"Array Contains: {len(magnificus.getLaboratory()._Laboratory__potions)} ---------------------------------------------")
magnificus.mixPotion("Extreme Attack")
print("Potions Mixed!!!!")
print(f"Array Contains: {len(magnificus.getLaboratory()._Laboratory__potions)} ---------------------------------------------")
magnificus.drinkPotion(magnificus.getLaboratory()._Laboratory__potions[0])
print(f"Array Contains: {len(magnificus.getLaboratory()._Laboratory__potions)} ---------------------------------------------")