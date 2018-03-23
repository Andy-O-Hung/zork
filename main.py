from Player import *
from Neighborhood import *

def main():

	# Testing number 2
		
	testHood = Neighborhood()
	print "This is the test hood: "
	print testHood.getMonsterCount()

	# End of testing number 2
	
'''
	print("hello")
	testNpc = Npc()
	print("testNpc health: %f" % testNpc.getHealthPoints())
	
	testPerson =  Person()
	print("testPerson custom function test: %s" % testPerson.asdf())
	print("testPerson health: %f" % testPerson.getHealthPoints())
	print("testPerson name: %s" % testPerson.getName())
	print("testPerson vul. len.: %d" % testPerson.getLengthVulnerability())
	#this is how you create an instance of a Hershey weapon, since its in folder
	#which has a class HersheyKisses.
	
	testWeapon = HersheyKisses.HersheyKisses()
	print("testWeapon hershey: %d" % testWeapon.getAmount())
	
	testPlayer = Player()
	print("testPlayer atk: %d" % testPlayer.getAttackValue())
'''

#This checks if this file is named main.
if __name__ == "__main__":
	main()
