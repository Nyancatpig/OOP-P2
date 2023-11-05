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
    def __init__(self):
        self.__potions = []
        self.__herbs = []
        self.__catalysts = []
    
    def mixPotion(self, name, type, stat, primaryIngredient, secondaryIngredient):
        pass

    def addReagent(self, reagent, amount):
        pass

class Alchemist():
    '''Alchemist class, character with actions'''
    def __init__(self, attack, strength, defense, magic, ranged, necromancy, laboratory):
        self.__attack = attack
        self.__strength = strength
        self.__defense = defense
        self.__magic = magic
        self.__ranged = ranged
        self.__necromancy = necromancy
        self.__laboratory = laboratory
        self.__recipes = {}

    def getLaboratory(self):
        '''Gets the laboratory variable'''
        return self.__laboratory

    def getRecipes(self):
        '''Gets the recipes'''
        return self.__recipes

    def mixPotion(self, recipe):
        pass

    def drinkPotion(self, potion):
        pass

    def collectReagent(self, reagent, amount):
        pass

    def refineReagents(self):
        pass

class Potion():
    '''Potion class, base for all potions'''
    def __int__(self, name, stat, boost):
        self.__name = name
        self.__stat = stat
        self.__boost = boost
    
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
    def __init__(self, name, stat, boost, herb, catalyst):
        super().__init__(name, stat, boost)
        self.__herb = herb
        self.__catalyst = catalyst

    def calculateBoost(self):
        pass

    def getHerb(self):
        '''Gets the herb variable'''
        return self.__herb
    
    def getCatalyst(self):
        '''Gets the catalyst variable'''
        return self.__catalyst
    
class ExtremePotion(Potion):
    '''Extreme Potion class, potion but extreme'''
    def __init__(self, name, stat, boost, reagent, potion):
        super().__init__(name, stat, boost)
        self.__reagent = reagent
        self.__potion = potion

    def calculateBoost(self):
        pass

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
        super().__init__(name, potency, grimy)
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
    def __innit__(self, name, potency, quality):
        super().__init__(name, potency)
        self.__quality = quality

    def refine(self):
        pass

    def getQuality(self):
        '''Gets the quality variable'''
        return self.__quality