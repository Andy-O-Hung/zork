from random import *

# Weapon parent class
class Weapon(object):
	
	# Class constructor
	# Initializes variables that are common to all weapons	
	def __init__(self):
		self.name = ""
		self.attackMod = 0
		self.uses = 0
	
	# Getter methods 

	# Returns weapon name
	def getName(self):
		return self.name

	# Returns weapon attack modifier
	def getMod(self):
		return self.attackMod

	# Returns weapon use count
	def getUses(self):
		return self.uses

	# Setter methods

	# Sets weapon use count
	def setUses(self, useCount):
		self.uses = useCount


# HersheyKiss class
# This class is a child of the weapon parent class
class HersheyKiss(Weapon):
	
	# Parent constructor override
	def __init__(self):
		super(HersheyKiss, self).__init__()
		self.name = "HersheyKiss"
		self.attackMod = 1
		self.uses = 5000000

# SourStraw class
# This class is a child of the weapon parent class
class SourStraw(Weapon):
	
	# Parent constructor override
	def __init__(self):
		super(SourStraw, self).__init__()
		self.name = "SourStraw"
		self.attackMod = uniform(1, 1.75)
		self.uses = 2

# ChocolateBar class
# This class is a child of the weapon parent class
class ChocolateBar(Weapon):
	
	# Parent constructor override
	def __init__(self):
		super(ChocolateBar, self).__init__()
		self.name = "ChocolateBar"
		self.attackMod = uniform(2, 2.4)
		self.uses = 4

# NerdBomb class
# This class is a child of the weapon parent class
class NerdBomb(Weapon):
	
	# Parent constructor override
	def __init__(self):
		super(NerdBomb, self).__init__()
		self.name = "NerdBomb"
		self.attackMod = uniform(3.5, 5)
		self.uses = 1


