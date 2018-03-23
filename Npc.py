from Observer import Observable
from random import *

# Parent class, which extends the observable class
class Npc(Observable):
	
	# Class constructor
	# Initializes variables that are common to all NPC's	
	def __init__(self):
		Observable.__init__(self)
		self.name = ""
		self.attackStrength = 0
		self.healthPoints = 0
		self.vulnerability = []
		self.weakness = "None" 
	
		
	# Getter methods

	# Returns NPC's name
	def getName(self):
		return self.name

	# Returns health points of NPC	
	def getHealth(self):
		return self.healthPoints
		
	# Returns NPC's attack strength
	def getAttack(self):
		return self.attackStrength

	# Returns NPC's weakness	
	def getWeakness(self):
		return self.weakness
		
	# Returns the number of vulnerabilities of NPC
	def getLengthVulnerability(self):
		return len(self.vulnerability)
		
	# Returns a list of all NPC's vulnerabilities
	def getVulnerability(self):
		return self.vulnerability

	# Setter methods 
	
	# Set NPC's health 
	def setHealth(self, health):
		self.healthPoints = health

		
# Person class
# This class is a child of the Npc parent class
class Person(Npc):

	# Parent constructor override 
	def __init__(self):
		super(Person,self).__init__()
		self.name = "Person"
		self.attackStrength = -1
		self.healthPoints = 100
		#maybe dont need a False statement for hurtable
	#random test function	
	def asdf(self):
		return "swag"

# Zombie class
# This class is a child of the Npc parent class
class Zombie(Npc):

	# Parent constructor override 
	def __init__(self):
		super(Zombie, self).__init__()
		self.name = "Zombie"
		self.attackStrength = randint(0, 10)
		self.healthPoints = randint(50, 100)
		self.vulnerability = ["HersheyKisses", "SourStraws", "ChocolateBars", "NerdBombs"]
		self.weakness = "SourStraws"

# Vampire class
# This class is a child of the Npc parent class
class Vampire(Npc):

	# Parent constructor override 
	def __init__(self):
		super(Vampire, self).__init__()
		self.name = "Vampire"
		self.attackStrength = randint(10, 20)
		self.healthPoints = randint(100, 200)
		self.vulnerability = ["HersheyKisses", "SourStraws", "NerdBombs"]

# Ghoul class
# This class is a child of the Npc parent class		
class Ghoul(Npc):

	# Parent constructor override 
	def __init__(self):
		super(Ghoul, self).__init__()
		self.name = "Ghoul"
		self.attackStrength = randint(15, 30)
		self.healthPoints = randint(40, 80)
		self.vulnerability = ["HersheyKisses", "SourStraws", "ChocolateBars", "NerdBombs"]
		self.weakness = "NerdBombs"

# Werewolf class
# This class is a child of the Npc parent class		
class Werewolf(Npc):

	# Parent constructor override 
	def __init__(self):
		super(Werewolf, self).__init__()
		self.name = "Werewolf"
		self.attackStrength = randint(0, 40)
		self.healthPoints = 200
		self.vulnerability = ["HersheyKisses", "NerdBombs"]
		
		
		
		
		
		
		
		
