# Import the necessary files 
# Note that not all classes are imported. This is because only the necessary ones are imported 
# into the main, and then the other ones are imported into the other classes when necessary
from Player import *
from Neighborhood import *
from Game import *

# The main method of the game.
def main():

	# Basic welcome message to greet the user
	print "Welcome to ZORK"

	# Creates an instance of the game class, and calls its run function
	currGame = Game()
	currGame.run()

#This checks if this file is named main.
if __name__ == "__main__":
	main()
