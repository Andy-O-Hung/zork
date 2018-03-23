from random import *
from Weapons import *

class Player(object):
	def __init__(self):
		self.health = randint(100, 125)
		self.attackValue = randint(10, 20)
		self.inventory = self.generateWeapons()
		
	def getHealth(self):
		return self.health
		
	def getInventory(self):
		return self.inventory
	
	def getAttackValue(self):
		return self.attackValue
	
	#REMOVE the continues when we implement the weapons
	def generateWeapons(self):
		weaponList = []
		tempKiss = HersheyKiss()
		weaponList.append(tempKiss)
		for x in range(9):
			choose = ["ChocolateBars", "NerdBomb", "SourStraws"]
			rand = randint(0,2)
			if choose[rand] == "ChocolateBars":
				tempBar = ChocolateBar()
				weaponList.append(tempBar)
				continue
			elif choose[rand] == "NerdBomb":
				tempBomb = NerdBomb()
				weaponList.append(tempBomb)
				continue
			elif choose[rand] == "SourStraws":
				tempStraw = SourStraw()				
				weaponList.append(tempStraw)
				continue
		return weaponList
		
	def setAttackValue(self, a):
		self.attackValue = a;
		
	def setHealth(self, a):
		self.health = a;
	
	
