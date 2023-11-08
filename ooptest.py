'''
File: ooptest.py
Description: A brief description of this Python module.
Author: Bailey Csortan
StudentID: 110409234
EmailID: csoby001
This is my own work as defined by the University's Academic Misconduct Policy.
'''

import unittest
from oopmain import *

class TestAlchemy(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.herbs = []
        cls.catalysts = []
        cls.makeReagents(["Irit", "Kwuarm", "Cadantine", "Lantadyme", "Dwarf Weed", "Arbuck", "Avantoe"], "Herb", "True")
        cls.makeReagents(["Eye of Newt", "Limpwurt Root", "White Berries", "Potato Cactus", "Wine of Zamorak", "Blood of Orcus", "Ground Mud Rune", "Grenwall Spike", "Ground Miasma Rune"], "Catalyst", "0")    
        cls.superPotions = ["Super Attack", "Super Strength", "Super Defence", "Super Magic", "Super Ranging", "Super Necromancy"]
        cls.extremePotions = ["Extreme Attack", "Extreme Strength", "Extreme Defence", "Extreme Magic", "Extreme Ranging", "Extreme Necromancy"]

    @classmethod
    def makeReagents(cls, reagentsList, reagentType, variable):
        for reagent in reagentsList:
            reagentName = f"{reagentType.lower()}" + (''.join(reagent.split()))
            newReagent = F"{reagentType}('{reagent}', 2, {variable})"
            exec(f"cls.{reagentType.lower()}s.append({newReagent})")
            print(reagentName)

    def test_tower(self):
        tower = Laboratory()
        magnificus = Alchemist(45, 60, 82, 85, 34, 27, tower)

        ## Test reagent collecting
        for herb in self.herbs:
            # magnificus.collectReagent(herb, 1)
            magnificus.collectReagent(herb, 20)
            # magnificus.collectReagent(herb, 1)
        for catalyst in self.catalysts:
            # magnificus.collectReagent(catalyst, 1)
            magnificus.collectReagent(catalyst, 20)
            # magnificus.collectReagent(catalyst, 1)

        ## Test reagent refining
        magnificus.refineReagents()

        ## Test potion mixing
        print(f"Array Contains: {len(magnificus.getLaboratory()._Laboratory__potions)} ---------------------------------------------")
        for superPotion in self.superPotions:
            magnificus.mixPotion(superPotion)
            magnificus.mixPotion(superPotion)
        for extremePotion in self.extremePotions:
            magnificus.mixPotion(extremePotion)  
        print(f"Array Contains: {len(magnificus.getLaboratory()._Laboratory__potions)} ---------------------------------------------")

        ## Test potion drinking
        while len(magnificus.getLaboratory()._Laboratory__potions) > 0:
            magnificus.drinkPotion(magnificus.getLaboratory()._Laboratory__potions[0])
        print(f"Array Contains: {len(magnificus.getLaboratory()._Laboratory__potions)} ---------------------------------------------")

        
if __name__ == '__main__':
    unittest.main()

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

# irit = Herb("Irit", 5, True)
# avantoe = Catalyst("Avantoe", 5, True)
# eyeOfNewt = Catalyst("Eye of Newt", 5, 4)
# superAttack = SuperPotion("Super Attack", "Attack", irit, avantoe)
## tower = Laboratory(potions=[superAttack], herbs=[irit, avantoe, irit, avantoe], catalysts=[eyeOfNewt, eyeOfNewt])
# tower = Laboratory(potions=[superAttack])
# magnificus = Alchemist(45, 60, 82, 85, 34, 27, tower)
# magnificus.collectReagent(irit, 6)
# magnificus.collectReagent(avantoe, 6)
# magnificus.collectReagent(eyeOfNewt, 6)
# print(f"Array Contains: {len(magnificus.getLaboratory()._Laboratory__potions)} ---------------------------------------------")
# print(f"Array Contains: {len(magnificus.getLaboratory()._Laboratory__herbs)} ---------------------------------------------")
# print(f"Array Contains: {len(magnificus.getLaboratory()._Laboratory__catalysts)} ---------------------------------------------")
# magnificus.refineReagents()
# magnificus.mixPotion("Super Attack")
# magnificus.mixPotion("Extreme Attack")
# magnificus.mixPotion("Super Attack")
# magnificus.mixPotion("Extreme Attack")

# print(f"Array Contains: {len(magnificus.getLaboratory()._Laboratory__potions)} ---------------------------------------------")
# magnificus.drinkPotion(magnificus.getLaboratory()._Laboratory__potions[0])
# magnificus.drinkPotion(magnificus.getLaboratory()._Laboratory__potions[0])
# magnificus.drinkPotion(magnificus.getLaboratory()._Laboratory__potions[0])