from Observer import Observable
from random import *
class Npc(Observable):
	
	def __init__(self):
		Observable.__init__(self)
		self.attackStrength = 0
		self.healthPoints = 0
	def getHealthPoints(self):
		return self.healthPoints
		

class Person(Npc):
	def __init__(self):
		super(Person, self).__init__()
		self.attackStrength = -1
		self.healthPoints = 100
		self.hurtable = False
		
	def asdf(self):
		return "swag"


