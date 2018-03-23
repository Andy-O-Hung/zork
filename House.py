from Npc import *
from Observer import *
from random import *

# House class, which extends both the observable and the observer class
# It observes all NPCs living within it, and it's also observed
# by the neighborhood class, which keeps track of the amount of total monsters
class House(Observer, Observable):
	
	# Class constructor
	def __init__(self):
		Observable.__init__(self)
		Observer.__init__(self)
		self.numberOfNpcs = randint(0, 10)
		self.npcList = self.generateNpcs(self.numberOfNpcs)
		self.numberOfMonsters = self.countMonsters(self.npcList)
	
	# Getter functions
	
	# Returns list of NPCs in the house
	def getNpcs(self):
		return self.npcList

	# Returns number of monsters in the house
	def getNumMonsters(self):
		return self.numberOfMonsters

	# Helper functions

	# This function will generate a given number of random monster
	# that will be in a certain house
	def generateNpcs(self, number):
		
		npcs = []

		# For loop that will run once for every monster
		for x in range(number):
			choose = ["Person", "Zombie", "Vampire", "Ghoul", "Werewolf"]
			rand = randint(0,4)		

			if choose[rand] == "Person":
				tempPerson = Person()
				tempPerson.add_observer(self)
				npcs.append(tempPerson)
	
			elif choose[rand] == "Zombie":
				tempZombie = Zombie()
				tempZombie.add_observer(self)
				npcs.append(tempZombie)
			
			elif choose[rand] == "Vampire":
				tempVampire = Vampire()
				tempVampire.add_observer(self)
				npcs.append(tempVampire)
				
			elif choose[rand] == "Ghoul":
				tempGhoul = Ghoul()
				tempGhoul.add_observer(self)
				npcs.append(tempGhoul)
				
			elif choose[rand] == "Werewolf":
				tempWerewolf = Werewolf()
				tempWerewolf.add_observer(self)
				npcs.append(tempWerewolf)
				
		# Return the list of monster in the house
		return npcs

	# This function will count the number of monsters (ignoring people) in
	# a house, provided a list of NPCs
	def countMonsters(self, npcs):
		
		# Variable that will hold the monster count
		monsterCount = 0

		# Will loop through the Npc list checking for monsters
		for x in npcs:
			if x.getName() != "Person":
				monsterCount += 1

		return monsterCount
		
	# This function will replace a monster with a person
	# It will be called when a monster is killed
	def killedMonster(self, monsterIndex):
		del self.npcList[monsterIndex]
		self.numberOfMonsters = self.numberOfMonsters - 1
		tempPerson = Person()
		tempPerson.add_observer(self)
		self.npcList.append(tempPerson)
		self.update()

	# Update method
	def update(self):
		self.updateAll()








