from House import *
from Observer import Observer
from random import *

# Neighborhood class, which extends the Observer class
class Neighborhood(Observer):

	# Class constructor
	def __init__(self):
		Observer.__init__(self)
		self.gridHeight = randint(3, 6)
		self.gridWidth = randint(3, 6)
		self.grid = populateGrid()
		self.numMonsters = 0
	
	# Getter methods
	
	# Returns the height of the grid
	def getHeight(self):
		return self.gridHeight

	# Returns the width of the grid	
	def getWidth(self):
		return self.gridWidth

	# Returns total number of monsters in neighborhood
	def getMonsterCount(self):
		return self.numMonsters

	# Helper methods
		
	# This function will populate the grid with houses
	def populateGrid(self):

		# List variable declaration
		g = []		
		
		for x in range(0, self.gridHeight):
			g.append([])
			for y in range(0, self.gridWidth):
				tempHouse = House()
				numMonsters += tempHouse.getNumMonsters()
				tempHouse.add_observer(self)
				g[x].append(tempHouse)

	def update(self):
		self.numMonster = self.numMonsters - 1
	
		
