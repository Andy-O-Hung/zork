from random import *

#This is the class for this weapon
class HersheyKisses(object):
	
	def __init__(self):
		self.name = "HersheyKisses"
		self.amount = 10000
		self.mod = 1

	def getName(self):
		return self.name

	def getAmount(self):
		return self.amount

	def getMod(self):
		return self.mod
