from Neighborhood import *
from Player import *
from random import *

# This is the Game class, which will be running the game logic
class Game(object):

	# Class constructor
	# Initializes variables
	def __init__(self):	
		
		# Neighborhood class instantiation
		self.hood = Neighborhood()
		# Get neighborhood grid, where house objects are located
		self.grid = self.hood.getGrid()
		# Instance of class player, which is the current player
		self.player1 = Player()
		# The variables turn and state are used to keep track of the player's 
		# current state
		self.turn = 0
		self.state = 0
	
	# This function will run the game
	def run(self):

		print("\nWelcome to your monster infested neighborhood\n")		

		self.state = 1
	
		# Run the game until game is finished
		# The game will finish when there is no monsters or 
		# the player dies 
		while(self.state != 0):

			# Print the neighborhood dimensions and the number of houses
			print("The size of the neighborhood is: %d x %d\n" % (self.hood.getHeight(), self.hood.getWidth()))
			print("There are %d houses in it.\n" % (self.hood.getHeight() * self.hood.getWidth()))

			# Prints the neighborhood map
			self.printMap();
			# Attemp to gather correct house coordinates from user
			try:
				print("Type the x coordinate of the house you would like to enter!\n")
				xHouse = int(raw_input())
				# Error catching
				# If the x coordinate if less than 0 or bigger than the grid size
				if (xHouse > self.hood.getHeight() or xHouse < 1):
					# Then raise value error
					raise ValueError
				print("Type the y coordinate of the house you would like to enter!\n")
				yHouse = int(raw_input())
				# Error catching
				# If the y coordinate if less than 0 or bigger than the grid size
				if (yHouse > self.hood.getWidth() or yHouse < 1):
					# Then raise value error
					raise ValueError
				# If coordinates are correct, proceed to house
				print("\nEntering house with coordinates %d x %d!\n" % (xHouse, yHouse))
				# Call enterHouse() function to enter the house, providing the house
				# coordinates within the grid as parameters
				self.enterHouse(xHouse, yHouse)		
	 		
			# Error handling
			# If coordinates are incorrect, do not attempt to enter house
			# Instead, print error message
			except ValueError:
				print "\nPlease enter correct coordinates\n"

	# Helper function
	# Prints the house coordinates to the screen
	def printMap(self):

		print("These are the coordinates of the houses in the neighborhood:\n")
		# Loop through the grid 2D array and print the coordinates of every house
		for x in range(self.hood.getHeight()):
			print("| "),
			for y in range(self.hood.getWidth()):
				# We add 1 to the coordinates, just so we don't start on 0
				# This makes it more undestandable for the user
				print("%d x %d  |" % ((x+1),(y+1))),
			print "\n"

	# Game Logic when player is inside the house
	def enterHouse(self, xHouse, yHouse):
		# Declaration of local variables
		inTheHouse = True
		houseEntered = self.grid[xHouse - 1][yHouse - 1]
		numMonsters = houseEntered.getNumMonsters()
	
		# Check number of NPCs in the house, which could be 0
		# If there is no monsters and no people in the house,
		# then exit the house
		if (len(houseEntered.getNpcs()) == 0):		
			print "This house is empty! Exiting!!"
			return
		# If there are NPCs, then proceed
		else:
			# Execute until players exits house
			while(inTheHouse):
				try:
					# Checks for total number of monsters in the neighborhood
					# If there is none, then the game is over and we exit the house
					# and the game. User wins
					if (self.hood.getMonsterCount() == 0):
						print("There are no more monsters!\n")
						print("You've won!\n")
						inTheHouse = False
						self.state = 0
						return
					NPCNum = 1
					print "You have found some creatures in the house!\n\nThis is a list of them:\n"
					# Print to the screen the list of NPC's in the house, assigning each an index
					# which starts from 1 (again, not 0 for user friendliness) and will be used by
					# player to select who to approach
					for x in houseEntered.getNpcs():
						print("%s (%d)" % (x.getName(), NPCNum))
						NPCNum += 1
					print "\n"
					print "Who would you like to approach? (Enter NPC index to approach or 0 to leave the house)\n"
					
					NPCIndex = int(raw_input())
					# The player will input 0 to exit house
					if (NPCIndex == 0):
						return
					# Check user input for possible errors
					# If the input is less than 0 or greater than the number
					# of NPCs in the house, an error will be raised
					elif (NPCIndex > NPCNum - 1 or NPCIndex < 1):
						raise ValueError
					
					print "\n"
					# If user input is correct, then approach NPC
					print("You decided to approach %s\n" % houseEntered.getNpcs()[NPCIndex - 1].getName())
					
					# If the NPC approached is a person, then player gains +1 health
					if (houseEntered.getNpcs()[NPCIndex - 1].getName() == "Person"):
						self.player1.setHealth(self.player1.getHealth() + 1)
						# Player is notified
						print("+1 health! Your health: %d\n" %self.player1.getHealth())
						
					# If NPC is not a person, then its monster
					# Therefore, player must fight
					else:
						print "Get ready to fight!\n"
						fighting = 1
						
						# Fighting logic of the game
						while (fighting == 1):
						
							# Checks for total number of monsters in the neighborhood
							# If there is none, then the game is over and we exit the house
							# and the game. User wins
							if (self.hood.getMonsterCount() == 0):
								print("There are no more monsters!\n")
								print("You've won!\n")
								fighting = 0
								inTheHouse = False
								self.state = 0
								return
							
							# Prints a list of all the weapons that the users has, 
							# and it shows how many uses each has left
							print "It's your turn to attack. These are your weapons:\n"
							WeaponNum = 1
							for x in self.player1.getInventory():
								print("%s. Uses left: %d (%d)" % (x.getName(), x.getUses() ,WeaponNum))
								WeaponNum += 1
							print "\n"
							# Same principle as the NPC approach
							print "What weapon would you like to use? Press 0 to get out of the house.\n"
							weaponIndex = int(raw_input())
							print ""
							# If player enter 0, then it will exit the house
							if(weaponIndex == 0):
								print("Getting out of this house.\n")
								return;
							# Checking user input for erros
							# If the user entered a number lower than 1 or greater than
							# the number of weapons available, the raise error
							elif(weaponIndex > WeaponNum - 1 or weaponIndex < 1):
								raise ValueError 
							# If weapons has no uses, then player can't attack and loses their turn
							elif(self.player1.getInventory()[weaponIndex-1].getUses() == 0):
								print "That weapon has no uses left! Sorry, you lost your opportunity to attack\n"
						
							# Fight against a Zombie
							if (houseEntered.getNpcs()[NPCIndex - 1].getName() == "Zombie" and self.player1.getInventory()[weaponIndex-1].getUses() > 0):
								# Notify player of it's opponent's health 
								print("You're attacking Zombie using %s!\n" % self.player1.getInventory()[weaponIndex-1].getName())
								print("Zombie has %d healthpoints\n" % houseEntered.getNpcs()[NPCIndex - 1].getHealth())
								damageDealt = 0
			
								# Calculate damage for attack with sour straw
								# Sour straws do extra damage to zombies
								if (self.player1.getInventory()[weaponIndex-1].getName() == "SourStraw"):

									print "It's really effective!\n"
									
									damageDealt = self.player1.getAttackValue()*self.player1.getInventory()[weaponIndex-1].getMod()*2

									houseEntered.getNpcs()[NPCIndex - 1].setHealth(houseEntered.getNpcs()[NPCIndex - 1].getHealth() - damageDealt)
									
									self.player1.getInventory()[weaponIndex-1].setUses(self.player1.getInventory()[weaponIndex-1].getUses() -1)
								
								# Calculate damage for any other weapon
								else:
					
									damageDealt = self.player1.getAttackValue()*self.player1.getInventory()[weaponIndex-1].getMod()

									houseEntered.getNpcs()[NPCIndex - 1].setHealth(houseEntered.getNpcs()[NPCIndex - 1].getHealth() - damageDealt)
									
									self.player1.getInventory()[weaponIndex-1].setUses(self.player1.getInventory()[weaponIndex-1].getUses() -1)
							
								# Notify player of the damage dealt to the zombie
								print("You dealt %d points of damage to Zombie!\n" %damageDealt)
								print("Your %s has now %d use(s)\n" % (self.player1.getInventory()[weaponIndex-1].getName(), self.player1.getInventory()[weaponIndex-1].getUses()))
							
								# If the zombie has less than 1 heath, it's dead. Notify player and observer (house in which is in)
								# This turns the Zombie into a person, and updates the total number of monsters in the neighborhood
								if(houseEntered.getNpcs()[NPCIndex - 1].getHealth() < 1):
									print("You defeated Zombie! It will turn into a person now!\n")
									houseEntered.killedMonster(NPCIndex - 1)
									break;
								# If zombie was not killed by attack, notify player of its health
								else:
									print("Zombie has %d healthpoints\n" % houseEntered.getNpcs()[NPCIndex - 1].getHealth())
							# Fight against a Vampire
							elif (houseEntered.getNpcs()[NPCIndex - 1].getName() == "Vampire" and self.player1.getInventory()[weaponIndex-1].getUses() > 0):
								# Notify player of it's opponent's health 
								print("You're attacking Vampire using %s!\n" % self.player1.getInventory()[weaponIndex-1].getName())
								print("Vampire has %d healthpoints\n" % houseEntered.getNpcs()[NPCIndex - 1].getHealth())
								damageDealt = 0
					
								# Calculate damage for attack with chocolate bar
								# Chocolate bars do extra damage to vampires
								if (self.player1.getInventory()[weaponIndex-1].getName() == "ChocolateBar"):

									print "Vampire is not harmed by ChocolateBar!\n"

									self.player1.getInventory()[weaponIndex-1].setUses(self.player1.getInventory()[weaponIndex-1].getUses() -1)
								
								# Calculate damage for any other weapon
								else:
					
									damageDealt = self.player1.getAttackValue()*self.player1.getInventory()[weaponIndex-1].getMod()

									houseEntered.getNpcs()[NPCIndex - 1].setHealth(houseEntered.getNpcs()[NPCIndex - 1].getHealth() - damageDealt)
									
									self.player1.getInventory()[weaponIndex-1].setUses(self.player1.getInventory()[weaponIndex-1].getUses() -1)
							
								# Notify player of the damage dealt to vampire
								print("You dealt %d points of damage to Vampire!\n" %damageDealt)
								print("Your %s has now %d use(s)\n" % (self.player1.getInventory()[weaponIndex-1].getName(), self.player1.getInventory()[weaponIndex-1].getUses()))
							
								# If the vampire has less than 1 heath, it's dead. Notify player and observer (house in which is in)
								# This turns the vampire into a person, and updates the total number of monsters in the neighborhood
								if(houseEntered.getNpcs()[NPCIndex - 1].getHealth() < 1):
									print("You defeated Vampire! It will turn into a person now!\n")
									houseEntered.killedMonster(NPCIndex - 1)
									break;
								# If vampire was not killed by attack, notify player of its health
								else:
									print("Vampire has %d healthpoints\n" % houseEntered.getNpcs()[NPCIndex - 1].getHealth())

							# Fight against a Ghoul
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

							# Fight against a Werewolf
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

							# After the player attacks, it's attacked
							# Notify the player about the attack
							print("You're under attack by %s! Watch out!\n" %houseEntered.getNpcs()[NPCIndex - 1].getName())
							damageReceived = houseEntered.getNpcs()[NPCIndex - 1].getAttack()
							print("%s has dealt %d points of damage!\n" %(houseEntered.getNpcs()[NPCIndex - 1].getName(), damageReceived))
			
							# Set players health after attack
							self.player1.setHealth(self.player1.getHealth() - damageReceived)
							
							# If player's health is under 1, then he/she has been defeated and the game is over
							if(self.player1.getHealth() < 1):
								print("Oh oh. The candy forces have defeated you! You weren't able to save your neighborhood.\n")
								print("There still are %d monsters in the neighborhood.\n" %self.hood.getMonsterCount())
								fighting = 0
								inTheHouse = False
								self.state = 0
								
							# If the player wasn't kiled by the attack, then show his/her health
							else:
								print("You have %d health points now!\n" %self.player1.getHealth())
				
				
				# Error handling for all possible user input errors catched above
				except ValueError:
					print("Incorrect input\n")
				
				
				
					
				
				
			

		
