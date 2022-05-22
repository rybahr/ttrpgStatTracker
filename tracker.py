################################################################
#DISCLAIMER
#This code is not guaranteed in anyway and presented as is. Using it could have adverse effects on your system.
#Any modifications you perform upon it may have unintended consequences when the script is run
#
#Be sure to have the accompanying text file in the same directory as this script.
#adjust the file path on line 57 to match the location
#
#Script assumes either melee or spell action taken on a turn with a healing option for any secondary actions.
#Script also assumes combat ends at end of full turn currently
###############################################################

#global imports
import csv

#class for entry of player/enemy
class Creature:
    #definition
    def __init__(self, name="", damageOutput=0, damageTotal=0, healingOutput=0, healingTotal=0, actionType="", attacksMade=0, attacksHit=0, spellSlotLevel=0):
        self.name = name
        self.damageOutput = damageOutput
        self.damageTotal = damageTotal
        self.healingOutput = healingOutput
        self.healingTotal = healingTotal
        self.actionType = actionType
        self.attacksMade = attacksMade
        self.attacksHit = attacksHit
        self.spellSlotLevel = spellSlotLevel

    #def set values
    def setName(self, name):
        self.name = name

    def setdamageOutput(self, damageOutput):
        self.damageOutput = damageOutput
    def setdamageTotal(self, damageTotal):
        self.damageTotal += damageTotal

    def sethealingOutput(self, healingOutput):
        self.healingOutput = healingOutput

    def sethealingTotal(self, healingTotal):
        self.healingTotal += healingTotal

    def setactionType(self, actionType):
        self.actionType = actionType

    def setattacksMade(self, attacksMade):
        self.attacksMade = attacksMade
    def setattacksHit(self, attacksHit):
        self.attacksHit = attacksHit

    def setspellSlotLevel(self, spellSlotLevel):
        self.spellSlotLevel = spellSlotLevel

############################################################
#main method to handle the primary looping logic and variables
def main():

    #open text file to write data to for storage, change the filepath here to match your set up
    data = open('/home/rbahr/8/combat.txt', 'a')

    #write handler
    writer = csv.writer(data)

    #list to hold all creatures to be tracked
    creatures = []
    #variable for adding creatures
    addCreature = "Y"
    #variables for combat
    combat = "N"
    round = 1

    #code to allow for single text file to be used to store multiple combat sessions by separating with a combat title
    combatTitle = input("Name of Combat Scenario?: ")
    writer.writerow([combatTitle])

    #generates creature objects with default values assigned per the class defined above
    while addCreature == "Y":
        name = input("Enter creatures name: ")
        c = Creature(name)
        creatures.append(c)
        choice = input("Add another creature? (Y/N)? \n")
        if choice == "Y":
            print(c.name)
            continue
        if choice == "N":
            break
        else:
            print("Y or N only")
            continue

    #while loop to keep looping through creatures sequentially and upping round counter
    print("Starting Combat \n")
    while combat == "N":

        for c in creatures:
            combatRound(c, round, writer)
        #end combat
        combat = input("End Combat? (Y/N)")
        if combat == "Y":
            break
        if combat == "N":
            round += 1
            continue
    data.close()
############################################################
#secondary method called to run individual round logic for creature
def combatRound(c, round, writer):
    print(c.name + "'s Turn")
    action = input("(W)eapon or (S)pell? ")

    #weapon damage logic
    if action == "W":
        c.setactionType(action)
        attacksMade = input("Attacks Made: ")
        hits = input("Attacks Hit: ")
        damage = input("Damage Dealt: ")
        c.setattacksMade(attacksMade)
        c.setattacksHit(hits)
        c.setdamageOutput(damage)
        c.setdamageTotal(int(damage))
        #sets spell slot used to 0
        #c.setspellSlotLevel(0)
        #healing check
        heal = input("Healing? ")
        if heal == "Y":
            healing = input("Amount: ")
            c.sethealingOutput(healing)
            c.sethealingTotal(int(healing))
        if heal == "N":
            healing = 0
            c.sethealingOutput(healing)
            c.sethealingTotal(int(healing))
    #spell damage logic
    if action == "S":
        c.setactionType(action)
        slot = input("Spell Slot Used?: ")
        c.setspellSlotLevel(slot)
        hits = input("Spell Hits: ")
        c.setattacksHit(hits)
        spellDamage = input("Damage: ")
        c.setdamageOutput(spellDamage)
        c.setdamageTotal(int(spellDamage))
        #healing check
        heal = input("Healing? (Y/N)")
        if heal == "Y":
            healing = input("Amount: ")
            c.sethealingOutput(healing)
            c.sethealingTotal(int(healing))
        if heal == "N":
            healing = 0
            c.sethealingOutput(healing)
            c.sethealingTotal(int(healing))
    #turn summary, writes all data to the text file
    row = [round, c.name, c.actionType, c.attacksMade, c.attacksHit, c.spellSlotLevel, c.damageOutput, c.damageTotal, c.healingOutput, c.healingTotal]
    #validation check to ensure all values assigned appropriately
    #print(row)
    writer.writerow(row)
    print("\n")

############################################################

main()