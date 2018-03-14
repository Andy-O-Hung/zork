from Npc import *
from Weapons import *
def main():
	print("hello")
	test =  Person()
	print(test.asdf())
	print(test.getHealthPoints())
	testNpc = Npc()
	print(testNpc.getHealthPoints())
	testWeapon = HersheyKisses.HersheyKisses()
	print(testWeapon.getAmount())

if __name__ == "__main__":
	main()
