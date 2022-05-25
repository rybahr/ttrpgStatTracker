################################################################
#DISCLAIMER
#This code is not guaranteed in anyway and presented as is. Using it could have adverse effects on your system.
#Any modifications you perform upon it may have unintended consequences when the script is run
#
#Be sure to have the accompanying text file in the same directory as this script.
#adjust the file path on line 61 to match the location
#
#Script assumes either melee or spell action taken on a turn with a healing option for any secondary actions.
#Script also assumes combat ends at end of full turn currently
###############################################################

#global imports
import csv
import sys
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
    data = open('combat.txt', 'a')

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
        choice = input("Add another creature? (Y/N): ")
        choice = validationYesNo(choice)
        if choice == "Y":
            continue
        if choice == "N":
            break

    #while loop to keep looping through creatures sequentially and upping round counter
    print("\nStarting Combat \nRound ", round)
    while combat == "N":

        for c in creatures:
            combatRound(c, round, writer)
        #end combat after all creatures have had a turn in the round
        combat = input("\nEnd Combat? (Y/N): ")
        combat = validationYesNo(combat)
        if combat == "Y":
            break
        if combat == "N":
            round += 1
            print("\nRound ", round)
            continue

    data.close()

    #Logic to start a 'new' combat session or end program entirely
    cont = input("\nStart new combat? (Y/N): ")
    cont = validationYesNo(cont)
    if cont == "Y":
        main()
    if cont == "N":
        print("\nEnding program")

############################################################
#secondary method called to run individual round logic for creature
def combatRound(c, round, writer):
    print("\n", c.name + "'s Turn")
    action = input("(W)eapon or (S)pell? ")
    action = validationWS(action)
    #weapon damage logic and validation
    if action == "W":
        c.setactionType(action)

        attacksMade = input("# of Attacks Made: ")
        validationNum(attacksMade)
        c.setattacksMade(int(attacksMade))

        hits = input("# of Attacks Hit: ")
        validationNum(hits)
        c.setattacksHit(int(hits))

        damage = input("Damage Dealt: ")
        validationNum(damage)
        c.setdamageOutput(int(damage))
        c.setdamageTotal(int(damage))

        #healing check
        heal = input("Healing? (Y/N): ")
        heal = validationYesNo(heal)
        if heal == "Y":
            healing = input("Amount: ")
            validationNum(healing)
            c.sethealingOutput(int(healing))
            c.sethealingTotal(int(healing))
        if heal == "N":
            healing = 0
            c.sethealingOutput(int(healing))
            c.sethealingTotal(int(healing))

    #spell damage logic
    if action == "S":
        c.setactionType(action)
        slot = input("Spell Slot Used?: ")
        validationNum(slot)
        c.setspellSlotLevel(int(slot))

        attacksMade = input("# of Spell Attacks Made: ")
        validationNum(attacksMade)
        c.setattacksMade(int(attacksMade))

        hits = input("# of Spell Hits: ")
        validationNum(hits)
        c.setattacksHit(int(hits))

        spellDamage = input("Damage: ")
        validationNum(spellDamage)
        c.setdamageOutput(int(spellDamage))
        c.setdamageTotal(int(spellDamage))

        #healing check
        heal = input("Healing? (Y/N): ")
        heal = validationYesNo(heal)
        if heal == "Y":
            healing = input("Amount: ")
            validationNum(healing)
            c.sethealingOutput(int(healing))
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

############################################################
#Input Validation for numerics

def validationNum(input):
    try:
        output = int(input)
        return output
    except Exception as e:
        print("Please enter integers only \n")
        print(e)
        print("\nEnding program")
        sys.exit()
        quit()

############################################################
#Input Validation for Y/N

def validationYesNo(input):
    try:
        input1 = input.upper()
        if input1 in ['Y','N']:
            return input1
        #else:
         #   print("\n Please enter 'Y','y','N', or 'n' only \n")
    except Exception as e:
        print(e)
        print("\nEnding program")
        sys.exit()
        quit()
    else:
        print("Please enter 'Y','y','N', or 'n' only \n")
        print("\nEnding program")
        sys.exit()
        quit()

############################################################

#Input Validation for Weapon or Spell

def validationWS(input):

    try:
        if input in {'W','w','S','s'}:
            output = input.upper()
            return output
    except Exception as e:
        print(e)
        print("\nEnding character's round")
    else:
        print("Please enter 'W','w','S', or 's' only \n")
        print("\nEnding character's round")

############################################################

main()
