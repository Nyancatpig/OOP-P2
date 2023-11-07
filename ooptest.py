'''
File: ooptest.py
Description: A brief description of this Python module.
Author: Bailey Csortan
StudentID: 110409234
EmailID: csoby001
This is my own work as defined by the University's Academic Misconduct Policy.
'''

import oopmain

# tower = oopmain.Laboratory(herbs=["Irit", "Avantoe", "Irit", "Avantoe"], catalysts=["Eye of Newt", "Eye of Newt"])
# magnificus = oopmain.Alchemist(45, 60, 82, 85, 34, 27, tower)
# print(magnificus.getLaboratory().__doc__)

# leshy = oopmain.Alchemist(103, 35, 66, 75, 34, 56, tower)
# print(leshy.getLaboratory().__doc__)

# magnificus.mixPotion("Extreme Attack")
# magnificus.mixPotion("Super Attack")
# magnificus.mixPotion("Extreme Attack")
# magnificus.mixPotion("Extreme Attack")

# print(f"Array Contains: {len(magnificus.getLaboratory()._Laboratory__potions)} ---------------------------------------------")
# magnificus.mixPotion("Super Attack")
# print(f"Array Contains: {len(magnificus.getLaboratory()._Laboratory__potions)} ---------------------------------------------")
# magnificus.mixPotion("Super Attack")
# print(f"Array Contains: {len(magnificus.getLaboratory()._Laboratory__potions)} ---------------------------------------------")
# magnificus.mixPotion("Extreme Attack")
# print("Potions Mixed!!!!")
# print(f"Array Contains: {len(magnificus.getLaboratory()._Laboratory__potions)} ---------------------------------------------")
# magnificus.drinkPotion(magnificus.getLaboratory()._Laboratory__potions[0])
# print(f"Array Contains: {len(magnificus.getLaboratory()._Laboratory__potions)} ---------------------------------------------")

irit = oopmain.Herb("Irit", 5, True)
avantoe = oopmain.Catalyst("Avantoe", 5, True)
eyeOfNewt = oopmain.Catalyst("Eye of Newt", 5, 4)
superAttack = oopmain.SuperPotion("Super Attack", "Attack", irit, avantoe)
# tower = oopmain.Laboratory(potions=[superAttack], herbs=[irit, avantoe, irit, avantoe], catalysts=[eyeOfNewt, eyeOfNewt])
tower = oopmain.Laboratory(potions=[superAttack])
magnificus = oopmain.Alchemist(45, 60, 82, 85, 34, 27, tower)
magnificus.collectReagent(irit, 6)
magnificus.collectReagent(avantoe, 6)
magnificus.collectReagent(eyeOfNewt, 6)
print(f"Array Contains: {len(magnificus.getLaboratory()._Laboratory__potions)} ---------------------------------------------")
print(f"Array Contains: {len(magnificus.getLaboratory()._Laboratory__herbs)} ---------------------------------------------")
print(f"Array Contains: {len(magnificus.getLaboratory()._Laboratory__catalysts)} ---------------------------------------------")
magnificus.refineReagents()
magnificus.mixPotion("Super Attack")
magnificus.mixPotion("Extreme Attack")
magnificus.mixPotion("Super Attack")
magnificus.mixPotion("Extreme Attack")
# print(f"Array Contains: {len(magnificus.getLaboratory()._Laboratory__potions)} ---------------------------------------------")
# magnificus.drinkPotion(magnificus.getLaboratory()._Laboratory__potions[0])
# magnificus.drinkPotion(magnificus.getLaboratory()._Laboratory__potions[0])
# magnificus.drinkPotion(magnificus.getLaboratory()._Laboratory__potions[0])