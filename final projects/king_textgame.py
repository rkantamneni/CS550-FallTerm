#Rule Quest
#by Revant Kantamneni
#October 6, 2017
#On my honor

#Sources
#Took the error checking from the demo game
#Introduction to Programming in Java Book


#A simulator where you rule over your kingdom. You must look over the army, money, religon, and your population approval to ensure a good reign. When any one factor becomes too big or too small, you loose the throne and could possibly die.
#I use fucntions, if functions, while loops, and inputs.

import sys
import math
import random
import time
import os
from random import randint

#Factors of you kingdom/rule . They are variables
money=50
army=50	
religion=50
population=50
years=0
x=0
y=0

#Prints your stats
def prin():
	print()
	print("Money: "+str(money)+ "      Population/Approval: "+str(population))
	print("Religion: "+str(religion)+ "   Army: "+str(army))
	print("You have ruled for "+str(years)+" years.")
	print()

#Makes sure answer is yes or no
def check(choice,a,b):
	while choice!=a and choice!=b:
		print()
		choice = input('Please choose '+a+' or '+b+': ')
	return choice

#Introduction as a fucntion using inputs
def intro():
	print("Welcome to RULE QUEST!")
	time.sleep(1.2)
	print("A medieval ruling simulator")
	time.sleep(1.2)
	name = input('What is your name? ')
	print('Hello there '+name+'!')
	king = input('Would you like to be the ruler of this realm? (yes/no) ')
	while king!=('yes'):
		print("Are you sure?")
		king = input('Would you like to be the ruler of this realm? (yes/no) ')
	else:
		time.sleep(1.2)
		print('All bow down to out all our mighty ruler, '+name)
		print()

#Rules Prinst statements to say rules. Using sleep to pause
def rules():
	time.sleep(2.0)
	print('There are 4 areas which you must manage to have a succesful rule')
	time.sleep(1.2)
	print('-Money')
	time.sleep(1.2)
	print('-Army')
	time.sleep(1.2)
	print('-Religion')
	time.sleep(1.2)
	print('-Population Approval')
	time.sleep(1.2)
	print()
	print('The decisions you will soon make will affect these categories.')
	time.sleep(1.2)
	print("Don't get any of them too high (100+) or too low (below 0)")
	time.sleep(2.5)
	print()
	print("Answer 'yes' or 'no' for each question.")
	print()
	print("Try to see how long you can sustain your rule for.")

#Game I define global variables which will apply everywhere in the code.  I use a list here also. 
#I take a random item from the list. Then I print it and take a user input. If the user input is yes or no, the four factors get
# affected. If something else in inputted, it checks if it's yes or no.
#All five of the following fucntions have the same premise. I could've created a one function with randomness but I wanted to do specifics.
def moneyf():
	global money
	global army
	global religion
	global population
	global years
	money1 = ["Miner Milton: Some gold has been found. Should we dig deeper? Answer(yes/no): ", 
			"King's Guard Garry: A fire started in the castle. Should we save the treasury first? Answer(yes/no): ",
			"General Gary: We need new shields. Answer: ",
			"Peasant Perry: The price of grain is too high. You should decrease it. Answer(yes/no): ",
			"High Priest Henry: We must have a parade dedciated to you for increasing your popularity. Answer(yes/no): ",
			"Doctor Dave: You should finance new infirmaries for the troops and people. Answer(yes/no): "]
	mon=random.choice(money1)
	m = input(mon)
	m = check(m,'yes','no')
	if m == 'yes':
		if mon==money1[0]:
			money+=15
			population-=20
		elif mon==money1[1]:
			population-=15
		elif mon==money1[2]:
			army+=15
			money-=15
		elif mon==money1[3]:
			money-=15
			population+=15
		elif mon==money1[4]:
			religion+=20
			money+=10
		elif mon==money1[5]:
			religion+=10
			money-=20
			population+=10
	if m == 'no':
		if mon==money1[0]:
			money+=10
		elif mon==money1[1]:
			money-=20
		elif mon==money1[2]:
			army-=15
			population+=15
		elif mon==money1[3]:
			population-=20
			money+=15
		elif mon==money1[4]:
			population-=10
			money+=15
			religion-=15
		elif mon==money1[5]:
			population-=15
			religion-=15
			army-=15
	years+=1
	prin()
#I use the prin function to print all the factors after they've been affected


def armyf():
	global money
	global army
	global religion
	global population
	global years
	army1 = ["Soldier Sam: We should attack the south and plunder their gold. Answer(yes/no): ",
			"Archer Adam: We need to build a moat around the castle. Answer(yes/no): ",
			"General Gary: We should decrease our presence in the towns. Answer(yes/no): ",
			"Banner Man Bob: We should put the symbol of our church on our banners. Answer(yes/no): ",
			"Arsenist Andy: May I join the army instead of going to jail? Answer(yes/no): ",
			"Warrior Will: Should we send an army to the south to aid our allies? Answer(yes/no): "]
	arm=random.choice(army1)
	a = input(arm)
	#army1.remove(arm)
	a = check(a,'yes','no')
	if a == 'yes':
		if arm==army1[0]:
			money+=20
			population-=10
			army+=15
		elif arm==army1[1]:
			army+=15
			money-=10
			population+=10
		elif arm==army1[2]:
			population+=10
			army-=10
			religion+=10
			money-=15
		elif arm==army1[3]:
			money+=10
			army+=15
			religion+=15
		elif arm==army1[4]:
			religion-=10
			money+=10
			army+=10
		elif arm==army1[5]:
			religion+=10
			money-=15
			army+=15
			population+=10
	if a == 'no':
		if arm==army1[0]:
			population+=10
			army-=10
			religion-=10
		elif arm==army1[1]:
			army-=15
			population-=10
		elif arm==army1[2]:
			army-=15
			population+=10
		elif arm==army1[3]:
			religion-=15
			army-=10
		elif arm==army1[4]:
			money-=10
			religion+=10
		elif arm==army1[5]:
			population+=15
			army-=10
	years+=1
	prin()


def religionf():
	global money
	global army
	global religion
	global population
	global years
	religion1 = ["High Priest Paul: The church has burned down. We should rebuild. Answer(yes/no): ",
				"Kevin the Knight: We should launch a crusade and find the holy grail. Answer(yes/no): ",
				"Pope Palmer: We must have mandatory attendence for service every week. Answer(yes/no): ",
				"Executioner Erik: We found some witches in the woods. Should we burn them? Answer(yes/no): ",
				"Cult of Calvin: Accept this cult and legitimize it. Answer(yes/no): ",
				"High Priestess Paulinha: We should make some offerings to the higher power. Answer(yes/no): "]
	relig = random.choice(religion1)
	r = input(relig)
	r= check(r,'yes','no')
	if r == 'yes':
		if relig==religion1[0]:
			religion+=15
			money-=20
			population+=15
		elif relig==religion1[1]:
			religion+=15
			money+=20
			population-=10
			army+=15
		elif relig==religion1[2]:
			population-=15
			religion+=15
		elif relig==religion1[3]:
			religion+=10
			population-=15
		elif relig==religion1[4]:
			religion-=20
			money+=20
		elif relig==religion1[5]:
			religion+=15
			money-=10
			population-=15
	if r == 'no':
		if relig==religion1[0]:
			religion-=20
			army+=15
		elif relig==religion1[1]:
			army-=15
			religion-=10
			population+=10
		elif relig==religion1[2]:
			population+=15
			religion-=15
		elif relig==religion1[3]:
			population+=10
			money+=10
			religion-=20
		elif relig==religion1[4]:
			population-=10
			religion+=20
		elif relig==religion1[5]:
			population+=15
			religion-=15
			money+=20
	years+=1
	prin()

def population_approvalf():
	global money
	global army
	global religion
	global population
	global years
	pop1 = ["Noble Ned: The population is eating too much. Adjust the price of bread. Answer(yes/no): ",
						"Engineer Erik: We should build aqueducts. Answer(yes/no): ",
						"Teacher Tim: We need to renovate the school. Answer(yes/no): ", 
						"Merchant Mike: We should start trading with the island nation of Samolot. Answer(yes/no): ",
						"Treasurer Travis: We should increase the taxes for all classes. Answer(yes/no): ",
						"King's Hand: We should enforce a curfew. Too much crime! Answer(yes/no): "]

	popuapp= random.choice(pop1)
	p = input(popuapp)
	p=check(p,'yes','no')
	if p == 'yes':

		if popuapp==pop1[0]:
			money+=20
			population-=15
		elif popuapp==pop1[1]:
			population+=20
			money-=20
		elif popuapp==pop1[2]:
			religion+=15
			money-=20
			army-=10
			population+=15
		elif popuapp==pop1[3]:
			money+=20
			population+=15
			army-=15
		elif popuapp==pop1[4]:
			population-=20
			money+=20
		elif popuapp==pop1[5]:
			religion+=10
			money+=10
			army-=19
			population-=15

	if p == 'no':
		if popuapp==pop1[0]:
			population+=5
			army-=10
			money-=10
		elif popuapp==pop1[1]:
			population-=20
		elif popuapp==pop1[2]:
			army+=15
			population-=20
		elif popuapp==pop1[3]:
			population-=5
			money-=15
		elif popuapp==pop1[4]:
			population+=15
			money-=15
			army-=15
		elif popuapp==pop1[5]:
			population+=10
			religion-=10
			army+=15
			money-=15
	years+=1
	prin()
	

def all_factor():
	global money
	global army
	global religion
	global population
	global years
	global x
	global y
	directions=["west","east","north","south"]
	all_factor1=["Would you like to marry the princess of the south? Answer: ",
				"King's Hand: Would you like to go on a hunt? Answer(yes/no): ",
				"Merchant Mike: The nobility would like to make a large donation and improve all aspects of the realm. Answer(yes/no): ",
				"Plague Doctor: The plague has come. Answer(yes/no): "]
	factor = random.choice(all_factor1)
	af = input(factor)
	af = check(af,'yes','no')
	if af == 'yes':
		if factor==all_factor1[0]:
			money+=10
			religion+=10
			population+=10
			army+=10
			years+=1
			prin()
		elif factor==all_factor1[1]:
			print('You got mauled by the boar. You died.')
			y=10
		elif factor==all_factor1[2]:
			print("The donation of gold and wepaonary was a bomb. You and your castle blew up. ")
			y=10
		elif factor==all_factor1[3]:
			print("Everyone's is dead. Including you.")
			y=10

	if af == 'no':

		if factor==all_factor1[0]:
			print("Okay then.")
		elif factor==all_factor1[1]:
			print("King's Hand: Goodbye.")
		elif factor==all_factor1[2]:
			print("It was a trap. You avoided it!")
		elif factor==all_factor1[3]:
			print("Everyone's is dead. Including you.")

#This death fucntion prints the multiple ways to die when one of your factors gets too high or too low.
def death():
	global x
	global money
	global army
	global religion
	global population
	global years
	#if lived longer than x years you die
	if (money>100 or money<0) or (army>100 or army<0) or (religion>100 or religion<0) or (population>100 or population<0):
		moneyd=["You had too much money and gold in your kingdom. Smaug the Dragon came and took it all. You died.", "There was no money left in the kingdom. There was a mutiny and you were fed to the dogs."]
		armyd=["You gave the army too much power. General Gary staged a coup, took your throne, and burned you on a stake.", "The army had no power and was insufficiently equipped. The northerners ransacked the entire kingdom and threw you into a dungeon. You get beheaded."]
		religiond=["People's faith had risen so much that they prayed for wealth and well-being all the time. The nobility take all power and exile you.", "No one is pious and everyone questions your rule. You get overthrown by your subjects and they dissect your body for scientific needs."]
		populationd=["Your subjects liked you so much that they asssinated you in your sleep and turned you into a god.", "Nobody liked you and everybody left the kingdom."]
		if money>60:
			print(moneyd[0])
		elif money<0:
			print(moneyd[1])
		elif army>60:
			print(armyd[0])
		elif army<0:
			print(armyd[1])
		elif religion>60:
			print(religiond[0])
		elif religion<0:
			print(religiond[1])
		elif population>100:
			print(populationd[0])
		elif population<0:
			print(populationd[1])
		x=10
	else:
		z=1

#You could end up becoming a parent for a child. The child gets assigned a random and/or age from a list
#I use time.sleep a lot so I the player can read the previously displayed information. 
def child():
	child=["boy", "girl"]
	c = random.choice(child)
	print("Congrats! You're a parent of a " + c)
	time.sleep(1.5)

	if c=="boy":
		bname=["Alex", "Henry", "William", "Francis", "Paul"]
		print("His name is "+random.choice(bname))
		time.sleep(1.5)
		print("He lives to the tender age of "+str(randint(5,13)))
		prin()
		time.sleep(4.0)

	else:
		gname=["Elizabeth", "Mary", "Josephine", "Paula", "Francesca"]
		print("Her name is "+random.choice(gname))
		print("...")
		time.sleep(2.0)
		print(random.choice(gname)+ " gets snatched away by kidnappers.")
		prin()
		time.sleep(4.0)

#Main function with all fucntions. I randomly pick a fucntion until the player dies and the program enters the death fucntion
# I have would you like to play again if statement where I set all the variables back to their initial states. IF the player says no, the program ends 
def start1():

	global money
	global army
	global religion
	global population
	global years
	global z
	prin()
	print()
	money=50
	army=50	
	religion=50
	population=50
	years=0
	z=1
	while (z == 1):
		global x
		global y
		x = randint(1,6)
		death()
		if x == 10 or y==10:
			break
			time.sleep(3.5)
			os.system('clear')
		elif x==1:
			moneyf()
			time.sleep(3.5)
			os.system('clear')
		elif x == 2:
			armyf()
			time.sleep(3.5)
			os.system('clear')
		elif x == 3:
			religionf()
			time.sleep(3.5)
			os.system('clear')
		elif x == 4:	
			population_approvalf()
			time.sleep(3.5)
			os.system('clear')
		elif x==5:
			all_factor()
			time.sleep(3.5)
			os.system('clear')
		elif x==6:
			child()
			time.sleep(3.5)
			os.system('clear')
	print()

	ag = input("Would you like to play again? ")

	if check(ag,'yes','no') == "yes":
		os.system('clear')
		y=0
		x=0
		religion=army=population=money=50
		years=0
		start1()
	elif check(ag,'yes','no') == "no":
		print("Thanks for playing!")
	time.sleep(2.0)

intro()
rules()
time.sleep(3.0)
start1()


