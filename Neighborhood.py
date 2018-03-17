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
	
	# Getter methods
	
	# Returns the height of the grid
	def getHeight():
		return self.gridHeight

	# Returns the width of the grid	
	def getWidth():
		return self.gridWidth

	# Helper methods
		
	# This function will populate the grid with houses
	def populateGrid():

		# List variable declaration
		g = []		
		
		for x in range(0, self.gridHeight):
			g.append([])
			for y in range(0, self.gridWidth):
				tempHouse = House()
				tempHouse.add_observer(self)
				a[x].append(tempHouse)
