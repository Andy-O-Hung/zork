from Neighborhood import *
from Player import *
from random import *

class Game(object):

	def __init__(self):	
		
		self.hood = Neighborhood()
		self.grid = self.hood.getGrid()
		self.player1 = Player()
		self.turn = 0
		self.state = 0

	def run(self):

		print("\nWelcome to your monster infested neighborhood\n")		

		self.state = 1
	
		while(self.state != 0):

			print("The size of the neighborhood is: %d x %d\n" % (self.hood.getHeight(), self.hood.getWidth()))
			print("There are %d houses in it.\n" % (self.hood.getHeight() * self.hood.getWidth()))
			self.printMap();
			try:
				print("Type the x coordinate of the house you would like to enter!\n")
				xHouse = int(raw_input())
				if (xHouse > self.hood.getHeight()):
					raise ValueError
				print("Type the y coordinate of the house you would like to enter!\n")
				yHouse = int(raw_input())
				if (yHouse > self.hood.getWidth()):
					raise ValueError
				print("\nEntering house with coordinates %d x %d!\n" % (xHouse, yHouse))
				self.enterHouse(xHouse, yHouse)		
	 
			except ValueError:
				print "\nPlease enter correct coordinates\n"

	def printMap(self):

		print("These are the coordinates of the houses in the neighborhood:\n")
		for x in range(self.hood.getHeight()):
			print("| "),
			for y in range(self.hood.getWidth()):
				print("%d x %d  |" % ((x+1),(y+1))),
			print "\n"

	def enterHouse(self, xHouse, yHouse):

		inTheHouse = True
		houseEntered = self.grid[xHouse - 1][yHouse - 1]
		numMonsters = houseEntered.getNumMonsters()
	
		if (len(houseEntered.getNpcs()) == 0):		
			print "This house is empty! Exiting!!"
			return
		else:
			while(inTheHouse):
				NPCNum = 1
				print "You have found some creatures in the house!\n\nThis is a list of them:\n"
				for x in houseEntered.getNpcs():
					print("%s (%d)" % (x.getName(), NPCNum))
					NPCNum += 1
				print "\n"
				print "Who would you like to approach? (Enter NPC index to approach or 0 to leave the house)\n"
				NPCIndex = int(raw_input())
				if (NPCIndex == 0):
					return
				print "\n"
				print("You decided to approach %s\n" %houseEntered.getNpcs()[NPCIndex - 1].getName())
				
				if (houseEntered.getNpcs()[NPCIndex - 1].getName() == "Person"):
					self.player1.setHealth(self.player1.getHealth() + 1)
					print("+1 health! Your health: %d\n" %self.player1.getHealth())
					
				else:
					print "Get ready to fight! These are your weapons:\n"
					WeaponNum = 1
					for x in self.player1.getInventory():
						print("%s. Uses left: %d (%d)" % (x.getName(), x.getUses() ,WeaponNum))
						WeaponNum += 1
					print "\n"
					print "What weapon would you like to use?\n"
					
				
				
			

		
