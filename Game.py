from Neighborhood import *
from Player import *
from random import *

#Game class that will be running the game logic.
class Game(object):

	#Initilization of the game.
	def __init__(self):	
		
		self.hood = Neighborhood()
		self.grid = self.hood.getGrid()
		self.player1 = Player()
		self.turn = 0
		self.state = 0
	
	#The function that will be used to run the game.
	def run(self):

		print("\nWelcome to your monster infested neighborhood\n")		

		self.state = 1
	
		#Run the game until game is finished.
		while(self.state != 0):

			print("The size of the neighborhood is: %d x %d\n" % (self.hood.getHeight(), self.hood.getWidth()))
			print("There are %d houses in it.\n" % (self.hood.getHeight() * self.hood.getWidth()))

			#Prints the map
			self.printMap();
			try:
				print("Type the x coordinate of the house you would like to enter!\n")
				xHouse = int(raw_input())
				if (xHouse > self.hood.getHeight() or xHouse < 1):
					raise ValueError
				print("Type the y coordinate of the house you would like to enter!\n")
				yHouse = int(raw_input())
				if (yHouse > self.hood.getWidth() or yHouse < 1):
					raise ValueError
				print("\nEntering house with coordinates %d x %d!\n" % (xHouse, yHouse))
				self.enterHouse(xHouse, yHouse)		
	 
			except ValueError:
				print "\nPlease enter correct coordinates\n"

	#Prints the house coordinates to the screen.
	def printMap(self):

		print("These are the coordinates of the houses in the neighborhood:\n")
		for x in range(self.hood.getHeight()):
			print("| "),
			for y in range(self.hood.getWidth()):
				print("%d x %d  |" % ((x+1),(y+1))),
			print "\n"

	#Game Logic when player is inside the house.
	def enterHouse(self, xHouse, yHouse):

		inTheHouse = True
		houseEntered = self.grid[xHouse - 1][yHouse - 1]
		numMonsters = houseEntered.getNumMonsters()
	
		if (len(houseEntered.getNpcs()) == 0):		
			print "This house is empty! Exiting!!"
			return
		else:
			while(inTheHouse):
				try:
					#Checks if the game has ended
					if (self.hood.getMonsterCount() == 0):
						print("There are no more monsters!\n")
						print("You've won!\n")
						inTheHouse = False
						self.state = 0
						return
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
					elif (NPCIndex > NPCNum - 1 or NPCIndex < 1):
						raise ValueError
					
					print "\n"
					print("You decided to approach %s\n" % houseEntered.getNpcs()[NPCIndex - 1].getName())
					
					if (houseEntered.getNpcs()[NPCIndex - 1].getName() == "Person"):
						self.player1.setHealth(self.player1.getHealth() + 1)
						print("+1 health! Your health: %d\n" %self.player1.getHealth())
						
					else:
						print "Get ready to fight!\n"
						fighting = 1
						
						#Fighting logic of the game.
						while (fighting == 1):
						
							#Checks if the game has ended
							if (self.hood.getMonsterCount() == 0):
								print("There are no more monsters!\n")
								print("You've won!\n")
								fighting = 0
								inTheHouse = False
								self.state = 0
								return
							
							#Ask the user what weapon to use.
							print "It's your turn to attack. These are your weapons:\n"
							WeaponNum = 1
							for x in self.player1.getInventory():
								print("%s. Uses left: %d (%d)" % (x.getName(), x.getUses() ,WeaponNum))
								WeaponNum += 1
							print "\n"
							print "What weapon would you like to use? Press 0 to get out of the house.\n"
							weaponIndex = int(raw_input())
							print ""
							if(weaponIndex == 0):
								print("Getting out of this house.\n")
								return;
							elif(weaponIndex > WeaponNum - 1 or weaponIndex < 1):
								raise ValueError 
							
							elif(self.player1.getInventory()[weaponIndex-1].getUses() == 0):
								print "That weapon has no uses left! Sorry, you lost your opportunity to attack\n"
						
							#Logic for if NPC is a Zombie
							if (houseEntered.getNpcs()[NPCIndex - 1].getName() == "Zombie" and self.player1.getInventory()[weaponIndex-1].getUses() > 0):
								print("You're attacking Zombie using %s!\n" % self.player1.getInventory()[weaponIndex-1].getName())
								print("Zombie has %d healthpoints\n" % houseEntered.getNpcs()[NPCIndex - 1].getHealth())
								damageDealt = 0

								if (self.player1.getInventory()[weaponIndex-1].getName() == "SourStraw"):

									print "It's really effective!\n"
									
									damageDealt = self.player1.getAttackValue()*self.player1.getInventory()[weaponIndex-1].getMod()*2

									houseEntered.getNpcs()[NPCIndex - 1].setHealth(houseEntered.getNpcs()[NPCIndex - 1].getHealth() - damageDealt)
									
									self.player1.getInventory()[weaponIndex-1].setUses(self.player1.getInventory()[weaponIndex-1].getUses() -1)

								else:
					
									damageDealt = self.player1.getAttackValue()*self.player1.getInventory()[weaponIndex-1].getMod()

									houseEntered.getNpcs()[NPCIndex - 1].setHealth(houseEntered.getNpcs()[NPCIndex - 1].getHealth() - damageDealt)
									
									self.player1.getInventory()[weaponIndex-1].setUses(self.player1.getInventory()[weaponIndex-1].getUses() -1)
							
								print("You dealt %d points of damage to Zombie!\n" %damageDealt)
								print("Your %s has now %d use(s)\n" % (self.player1.getInventory()[weaponIndex-1].getName(), self.player1.getInventory()[weaponIndex-1].getUses()))
							
								if(houseEntered.getNpcs()[NPCIndex - 1].getHealth() < 1):
									print("You defeated Zombie! It will turn into a person now!\n")
									houseEntered.killedMonster(NPCIndex - 1)
									break;
								else:
									print("Zombie has %d healthpoints\n" % houseEntered.getNpcs()[NPCIndex - 1].getHealth())
								
							#Logic for if NPC is a Vampire
							elif (houseEntered.getNpcs()[NPCIndex - 1].getName() == "Vampire" and self.player1.getInventory()[weaponIndex-1].getUses() > 0):
								print("You're attacking Vampire using %s!\n" % self.player1.getInventory()[weaponIndex-1].getName())
								print("Vampire has %d healthpoints\n" % houseEntered.getNpcs()[NPCIndex - 1].getHealth())
								damageDealt = 0

								if (self.player1.getInventory()[weaponIndex-1].getName() == "ChocolateBar"):

									print "Vampire is not harmed by ChocolateBar!\n"

									self.player1.getInventory()[weaponIndex-1].setUses(self.player1.getInventory()[weaponIndex-1].getUses() -1)
									
								else:
					
									damageDealt = self.player1.getAttackValue()*self.player1.getInventory()[weaponIndex-1].getMod()

									houseEntered.getNpcs()[NPCIndex - 1].setHealth(houseEntered.getNpcs()[NPCIndex - 1].getHealth() - damageDealt)
									
									self.player1.getInventory()[weaponIndex-1].setUses(self.player1.getInventory()[weaponIndex-1].getUses() -1)
							
								print("You dealt %d points of damage to Vampire!\n" %damageDealt)
								print("Your %s has now %d use(s)\n" % (self.player1.getInventory()[weaponIndex-1].getName(), self.player1.getInventory()[weaponIndex-1].getUses()))
							
								if(houseEntered.getNpcs()[NPCIndex - 1].getHealth() < 1):
									print("You defeated Vampire! It will turn into a person now!\n")
									houseEntered.killedMonster(NPCIndex - 1)
									break;
								else:
									print("Vampire has %d healthpoints\n" % houseEntered.getNpcs()[NPCIndex - 1].getHealth())

							#Logic for if NPC is a Ghoul
							elif (houseEntered.getNpcs()[NPCIndex - 1].getName() == "Ghoul" and self.player1.getInventory()[weaponIndex-1].getUses() > 0):
								print("You're attacking Ghoul using %s!\n" % self.player1.getInventory()[weaponIndex-1].getName())
								print("Ghoul has %d healthpoints\n" % houseEntered.getNpcs()[NPCIndex - 1].getHealth())
								damageDealt = 0

								if (self.player1.getInventory()[weaponIndex-1].getName() == "NerdBomb"):

									print "It's SUPER effective!\n"
									
									damageDealt = self.player1.getAttackValue()*self.player1.getInventory()[weaponIndex-1].getMod()*5

									houseEntered.getNpcs()[NPCIndex - 1].setHealth(houseEntered.getNpcs()[NPCIndex - 1].getHealth() - damageDealt)
									
									self.player1.getInventory()[weaponIndex-1].setUses(self.player1.getInventory()[weaponIndex-1].getUses() -1)

								else:
					
									damageDealt = self.player1.getAttackValue()*self.player1.getInventory()[weaponIndex-1].getMod()

									houseEntered.getNpcs()[NPCIndex - 1].setHealth(houseEntered.getNpcs()[NPCIndex - 1].getHealth() - damageDealt)
									
									self.player1.getInventory()[weaponIndex-1].setUses(self.player1.getInventory()[weaponIndex-1].getUses() -1)
							
								print("You dealt %d points of damage to Ghoul!\n" %damageDealt)
								print("Your %s has now %d use(s)\n" % (self.player1.getInventory()[weaponIndex-1].getName(), self.player1.getInventory()[weaponIndex-1].getUses()))
							
								if(houseEntered.getNpcs()[NPCIndex - 1].getHealth() < 1):
									print("You defeated Ghoul! It will turn into a person now!\n")
									houseEntered.killedMonster(NPCIndex - 1)
									break;
								else:
									print("Ghoul has %d healthpoints\n" % houseEntered.getNpcs()[NPCIndex - 1].getHealth())

							#Logic for if NPC is a Werewolf
							elif (houseEntered.getNpcs()[NPCIndex - 1].getName() == "Werewolf" and self.player1.getInventory()[weaponIndex-1].getUses() > 0):
								print("You're attacking Werewolf using %s!\n" % self.player1.getInventory()[weaponIndex-1].getName())
								print("Werewolf has %d healthpoints\n" % houseEntered.getNpcs()[NPCIndex - 1].getHealth())
								damageDealt = 0

								if (self.player1.getInventory()[weaponIndex-1].getName() == "ChocolateBar"):

									print "Werewolf is not harmed by ChocolateBar!\n"

									self.player1.getInventory()[weaponIndex-1].setUses(self.player1.getInventory()[weaponIndex-1].getUses() -1)

								elif (self.player1.getInventory()[weaponIndex-1].getName() == "SourStraw"):
								
									print "Werewolf is not harmed by SourStraw!\n"

									self.player1.getInventory()[weaponIndex-1].setUses(self.player1.getInventory()[weaponIndex-1].getUses() -1)
	
								else:
					
									damageDealt = self.player1.getAttackValue()*self.player1.getInventory()[weaponIndex-1].getMod()

									houseEntered.getNpcs()[NPCIndex - 1].setHealth(houseEntered.getNpcs()[NPCIndex - 1].getHealth() - damageDealt)
									
									self.player1.getInventory()[weaponIndex-1].setUses(self.player1.getInventory()[weaponIndex-1].getUses() -1)
							
								print("You dealt %d points of damage to Werewolf!\n" %damageDealt)
								print("Your %s has now %d use(s)\n" % (self.player1.getInventory()[weaponIndex-1].getName(), self.player1.getInventory()[weaponIndex-1].getUses()))
							
								if(houseEntered.getNpcs()[NPCIndex - 1].getHealth() < 1):
									print("You defeated Werewolf! It will turn into a person now!\n")
									houseEntered.killedMonster(NPCIndex - 1)
									break;
								else:
									print("Werewolf has %d healthpoints\n" % houseEntered.getNpcs()[NPCIndex - 1].getHealth())

							print("You're under attack by %s! Watch out!\n" %houseEntered.getNpcs()[NPCIndex - 1].getName())
							damageReceived = houseEntered.getNpcs()[NPCIndex - 1].getAttack()
							print("%s has dealt %d points of damage!\n" %(houseEntered.getNpcs()[NPCIndex - 1].getName(), damageReceived))
			
							self.player1.setHealth(self.player1.getHealth() - damageReceived)
							
							if(self.player1.getHealth() < 1):
								print("Oh oh. The candy forces have defeated you! You weren't able to save your neighborhood.\n")
								print("There still are %d monsters in the neighborhood.\n" %self.hood.getMonsterCount())
								fighting = 0
								inTheHouse = False
								self.state = 0
								
							else:
								print("You have %d health points now!\n" %self.player1.getHealth())
				
				
				except ValueError:
					print("Incorrect input\n")
				
				
				
					
				
				
			

		
