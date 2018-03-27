from Player import *
from Neighborhood import *
from Game import *

#The main method of the game.
def main():

	print "Welcome to ZORK"

	#Calls the game class to start the game.
	currGame = Game()
	currGame.run()



#This checks if this file is named main.
if __name__ == "__main__":
	main()
