import random

def getattributescore():
    dice1 = random.randrange(1, 6)
    dice2 = random.randrange(1, 6)
    dice3 = random.randrange(1, 6)

    total = dice1 + dice2 + dice3
    return total

class PlayerCharacter():
    def __init__(self):
        self.strength = getattributescore()
        self.constitution = getattributescore()
        self.dexterity = getattributescore()
        self.intelligence = getattributescore()
        self.wisdom = getattributescore()
        self.charisma = getattributescore()
    """
    Functions to raise the values of the attributes
    """
    def addstrength(self, value):
        self.strength += value
        return self.strength

    def addconstitution(self, value):
        self.constitution += value
        return self.constitution
    
    def adddexterity(self, value):
        self.dexterity += value
        return self.dexterity

    def addintelligence(self, value):
        self.intelligence += value
        return self.intelligence
    
    def addwisdom(self, value):
        self.wisdom += value
        return self.wisdom

    def addcharisma(self, value):
        self.charisma += value
        return self.charisma
    
    """
    Functions to lower the values of the attributes
    """
    def removestrength(self, value):
        self.strength += value
        return self.strength

    def removeconstitution(self, value):
        self.constitution -= value
        return self.constitution
    
    def removedexterity(self, value):
        self.dexterity -= value
        return self.dexterity

    def removeintelligence(self, value):
        self.intelligence -= value
        return self.intelligence
    
    def removewisdom(self, value):
        self.wisdom -= value
        return self.wisdom

    def removecharisma(self, value):
        self.charisma -= value
        return self.charisma
    """
    Functions to view the attribute values individually
    """
    def viewstrength(self):
        return self.strength

    def viewconstitution(self):
        return self.constitution
    
    def viewdexterity(self):
        return self.dexterity

    def viewintelligence(self):
        return self.intelligence
    
    def viewwisdom(self):
        return self.wisdom

    def viewcharisma(self):
        return self.charisma