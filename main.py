from Npc import *
#import all the classes inside the Weapons folder
from Weapons import *

def main():
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
	

#This checks if this file is named main.
if __name__ == "__main__":
	main()
