from Observer import Observable
from random import *

#Parent class, which extends the observable class
class Npc(Observable):
	
	def __init__(self):
		Observable.__init__(self)
		self.name = ""
		self.attackStrength = 0
		self.healthPoints = 0
		self.vulnerability = []
		self.weakness = "None" 
		
	def getHealthPoints(self):
		return self.healthPoints
		
	def getAttack(self):
		return self.attackStrength
		
	def getName(self):
		return self.name
		
	def getWeakness(self):
		return self.weakness
		
	def getLengthVulnerability(self):
		return len(self.vulnerability)
		
	def getVulnerability(self):
		return self.vulnerability
		
#child person
class Person(Npc):
	#Overriding 
	def __init__(self):
		super(Person,self).__init__()
		self.name = "Person"
		self.attackStrength = -1
		self.healthPoints = 100
		#maybe dont need a False statement for hurtable
	#random test function	
	def asdf(self):
		return "swag"

class Zombie(Npc):
	def __init__(self):
		super(Zombie, self).__init__()
		self.name = "Zombie"
		self.attackStrength = randint(0, 10)
		self.healthPoints = randint(50, 100)
		self.vulnerability = ["HersheyKisses", "SourStraws", "ChocolateBars", "NerdBombs"]
		self.weakness = "SourStraws"

class Vampire(Npc):
	def __init__(self):
		super(Vampire, self).__init__()
		self.name = "Vampire"
		self.attackStrength = randint(10, 20)
		self.healthPoints = randint(100, 200)
		self.vulnerability = ["HersheyKisses", "SourStraws", "NerdBombs"]
		
class Ghoul(Npc):
	def __init__(self):
		super(Vampire, self).__init__()
		self.name = "Ghoul"
		self.attackStrength = randint(15, 30)
		self.healthPoints = randint(40, 80)
		self.vulnerability = ["HersheyKisses", "SourStraws", "ChocolateBars", "NerdBombs"]
		self.weakness = "NerdBombs"
		
class Werewolf(Npc):
	def __init__(self):
		super(Werewolve, self).__init__()
		self.name = "Werewolf"
		self.attackStrength = randint(0, 40)
		self.healthPoints = 200
		self.vulnerability = ["HersheyKisses", "NerdBombs"]
		
		
		
		
		
		
		
		
