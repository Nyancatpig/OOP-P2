'''
File: oopmain.py
Description: A brief description of this Python module.
Author: Bailey Csortan
StudentID: 110409234
EmailID: csoby001
This is my own work as defined by the University's Academic Misconduct Policy.
'''

from abc import ABC, abstractmethod


class Laboratory():
    '''Laboratory class, owns other classes'''
    def __init__(self, potions, herbs, catalysts):
        self.__potions = potions
        self.__herbs = herbs
        self.__catalysts = catalysts
    
    def mixPotion(self, name, type, stat, primaryIngredient, secondaryIngredient):
        '''Creates potion from recipe sent from alchemist'''
        # If output is extreme potion
        if type == "Extreme":
                # If primary ingredient is in laboratory
                if primaryIngredient in self.__herbs or primaryIngredient in self.__catalysts:
                    # If secondary ingredient is in laboratory
                    if secondaryIngredient in self.__potions:
                        
                        # Remove ingredients
                        if primaryIngredient in self.__herbs:
                            self.__herbs.remove(primaryIngredient)
                        elif primaryIngredient in self.__catalysts:
                            self.__catalysts.remove(primaryIngredient)
                        self.__potions.remove(secondaryIngredient)

                        # Add potion
                        newReagent = Reagent(primaryIngredient, 0)
                        newPot = Potion(name, stat)
                        newPotion = ExtremePotion(name, stat, newReagent, newPot)
                        self.__potions.append(newPotion)

                # If ingredients are not present        
                    else:
                        raise ValueError(f"{secondaryIngredient} is not currently a valid potion in the Laboratory!")
                else:
                    raise ValueError(f"{primaryIngredient} is not currently a valid ingredient in the Laboratory!")
                
        # If output is super potion
        elif type == "Super":
            # If primary ingredient is in laboratory
            if primaryIngredient in self.__herbs:        
                # If secondary ingredient is in laboratory
                if secondaryIngredient in self.__catalysts:

                    # Remove ingredients
                    self.__herbs.remove(primaryIngredient)
                    self.__catalysts.remove(secondaryIngredient)

                    # Add potion
                    #newPotion = SuperPotion(name, stat, Herb(primaryIngredient, 0, False), Catalyst(secondaryIngredient, 0, 0))
                    newHerb = Herb(primaryIngredient, 0, False)
                    newCatalyst = Catalyst(secondaryIngredient, 0, 0)
                    newPotion = SuperPotion(name, stat, newHerb, newCatalyst)
                    self.__potions.append(newPotion)

            # If ingredients are not present           
                else:
                        raise ValueError(f"{secondaryIngredient} is not currently a valid potion in the Laboratory!")
            else:
                raise ValueError(f"{primaryIngredient} is not currently a valid ingredient in the Laboratory!")
                            

        print(f"Alchemist mixed {name}, using {primaryIngredient} and {secondaryIngredient}")

    def addReagent(self, reagent, amount):
        pass

class Alchemist():
    '''Alchemist class, character with actions'''
    def __init__(self, attack, strength, defence, magic, ranged, necromancy, laboratory):
        self.__validateStat("attack", attack)
        self.__validateStat("strength", strength)
        self.__validateStat("defence", defence)
        self.__validateStat("magic", magic)
        self.__validateStat("ranged", ranged)
        self.__validateStat("necromancy", necromancy)

        self.__attack = attack
        self.__strength = strength
        self.__defence = defence
        self.__magic = magic
        self.__ranged = ranged
        self.__necromancy = necromancy
        self.__laboratory = laboratory
        self.__recipes = {
            "Super Attack": {"Herb": "Irit", "Catalyst": "Eye of Newt"},
            "Extreme Attack": {"Herb": "Avantoe", "Super Potion": "Super Attack"}
        }

    def __validateStat(self, attributeName, value):
        '''Check if variable isn't between 0 and 100'''
        if not (0 <= value <= 100):
            raise ValueError(f"Alchemist's {attributeName} must be between 0 and 100!")

    def getLaboratory(self):
        '''Gets the laboratory variable'''
        return self.__laboratory

    def getRecipes(self):
        '''Gets the recipes'''
        return self.__recipes

    def mixPotion(self, recipe):
        '''Sends potion recipe to laboratory'''
        # Get ingredients
        if recipe in self.__recipes:
            ingredientsList = list(self.__recipes[recipe].values())

            primary =  ingredientsList[0]
            secondary = ingredientsList[1]
        else:
            raise KeyError(f"There is no {recipe} potion recipe!") 
        
        # Get potion type and stat
        if "Super" in recipe:
            type = recipe[:-7]
            stat = recipe[6:]
        elif "Extreme" in recipe:
            type = recipe[:-7]
            stat = recipe[8:]
        else:
            raise NameError(f"The {recipe} is not a Super Potion or an Extreme Potion!") 
        
        self.__laboratory.mixPotion(recipe, type, stat, primary, secondary)

    def drinkPotion(self, potion):
        '''Drinks potion and adds status effect to alchemist'''
        if potion in self.__laboratory._Laboratory__potions:
            self.__laboratory._Laboratory__potions.remove(potion)

            # Add potion stats
            if potion.getStat() == "Attack":
                self.addPotionStat(potion, "_Alchemist__attack")
            if potion.getStat() == "Strength":
                self.addPotionStat(potion, "_Alchemist__strength")
            if potion.getStat() == "Defence":
                self.addPotionStat(potion, "_Alchemist__defence")
            if potion.getStat() == "Magic":
                self.addPotionStat(potion, "_Alchemist__magic")
            if potion.getStat() == "Ranging":
                self.addPotionStat(potion, "_Alchemist__ranged")
            if potion.getStat() == "Necromancy":
                self.addPotionStat(potion, "_Alchemist__necromancy")    
        return f"{potion.getName()}"
    
    def addPotionStat(self, potion, statName):
        '''A helper function for the drinkPotion function'''
        oldStat = getattr(self, statName)
        
        # Add to stat
        name = potion.getName()
        if "Super" in name:
            new_stat = oldStat + 10
            if new_stat > 100:
                new_stat = 100
            # Set variable instead of just the reference
            setattr(self, statName, new_stat)
            print(f"Alchemist drank {name}, their {name[6:]} has been increased from {oldStat} to {new_stat}")
        elif "Extreme" in name:
            new_stat = oldStat + 20
            if new_stat > 100:
                new_stat = 100
            # Set variable instead of just the reference
            setattr(self, statName, new_stat)
            print(f"Alchemist drank {name}, their {name[8:]} has been increased from {oldStat} to {new_stat}")
        else:
            raise NameError(f"The {potion} is not a Super Potion or an Extreme Potion!")
        

    def collectReagent(self, reagent, amount):
        pass

    def refineReagents(self):
        pass

class Potion():
    '''Potion class, base for all potions'''
    def __init__(self, name, stat):
        self.__name = name
        self.__stat = stat
        self.__boost = 0
    
    @abstractmethod
    def calculateBoost(self):
        pass

    def getName(self):
        '''Gets the name variable'''
        return self.__name
    
    def getStat(self):
        '''Gets the stat variable'''
        return self.__stat
    
    def getBoost(self):
        '''Gets the boost variable'''
        return self.__boost
    
    def setBoost(self, boost):
        '''Sets the boost variable'''
        self.__boost = boost

class SuperPotion(Potion):
    '''Super Potion class, potion but super'''
    def __init__(self, name, stat, herb, catalyst):
        super().__init__(name, stat)
        self.__herb = herb
        self.__catalyst = catalyst

    def calculateBoost(self):
        return 10

    def getHerb(self):
        '''Gets the herb variable'''
        return self.__herb
    
    def getCatalyst(self):
        '''Gets the catalyst variable'''
        return self.__catalyst
    
class ExtremePotion(Potion):
    '''Extreme Potion class, super potion but extreme'''
    def __init__(self, name, stat, reagent, potion):
        super().__init__(name, stat)
        self.__reagent = reagent
        self.__potion = potion

    def calculateBoost(self):
        return 20

    def getReagent(self):
        '''Gets the reagent variable'''
        return self.__reagent
    
    def getPotion(self):
       '''Gets the potion variable'''
       return self.__potion
    
class Reagent():
    '''Reagent class, an ingredient'''
    def __init__(self, name, potency):
        self.__name = name
        self.__potency = potency

    @abstractmethod
    def refine(self):
        pass

    def getName(self):
        '''Gets the name variable'''
        return self.__name
    
    def getPotency(self):
        '''Gets the potency variable'''
        return self.__potency
    
    def setPotency(self, potency):
        '''Sets the potency variable'''
        self.__potency = potency

class Herb(Reagent):
    def __init__(self, name, potency, grimy):
        super().__init__(name, potency)
        self.__grimy = grimy

    def refine(self):
        pass

    def getGrimy(self):
        '''Gets the grimy variable'''
        return self.__grimy
    
    def setGrimy(self, grimy):
        '''Sets the grimy variable'''
        self.__grimy = grimy

class Catalyst(Reagent):
    def __init__(self, name, potency, quality):
        super().__init__(name, potency)
        self.__quality = quality

    def refine(self):
        pass

    def getQuality(self):
        '''Gets the quality variable'''
        return self.__quality