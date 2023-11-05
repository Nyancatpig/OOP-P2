'''
File: oopmain.py
Description: A brief description of this Python module.
Author: Bailey Csortan
StudentID: 110409234
EmailID: csoby001
This is my own work as defined by the University's Academic Misconduct Policy.
'''

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
        '''Gets the recipes '''
        return self.__recipes

    def mixPotion(self, recipe):
        pass

    def drinkPotion(self, potion):
        pass

    def collectReagent(self, reagent, amount):
        pass

    def refineReagents(self):
        pass