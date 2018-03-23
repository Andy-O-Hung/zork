from Neighborhood import *
from Player import *
from random import *

class Game(object):

	def __init__(self):	
		
		self.hood = Neighborhood()
		self.player1 = Player()
		self.turn = 0
		self.state = 0

	def run(self):

		print("\nWelcome to your monster infested neighborhood\n")
		print("The size of the neighborhood is: %d x %d\n" % (self.hood.getHeight(), self.hood.getWidth()))
		print("These are the houses in the neighborhood: ")
		self.printMap();
	
	def printMap(self):
		i = 1
		for x in range(self.hood.getHeight()):
			for y in range(self.hood.getHeight()):
				print("  %d  " % i)
				i += 1
			 

