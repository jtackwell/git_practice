# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Jonathan Tackwell
# Creation Date: 5/27/2022
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()

def chooseCave():
    #used spaces instead of tabs in the line below
	cave = ''
	while cave != '1' and cave != '2': #this while statement is unecessary, delete line for simplicity.
		print('Which cave will you go into? (1 or 2)') #remove tabs
		cave = input()#remove tabs

	return caves #delete to simplifiy 

def checkCave(chosenCave):#I would delete this line entirely to simplfy the code
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(3)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave): #change "chosenCave" to "cave" to complete the comparison attempted here
		print('Gives you his treasure!')
	else:
		print 'Gobbles you down in one bite!'#syntax error line should be "print('Gobbles you down in one bite!')"

playAgain = 'yes'
 
while playAgain = 'yes' or playAgain = 'y': # should be '==' not '='
	displayIntro()

	caveNumber = choosecave() #change to "choosecave()" for simplicity
	checkCave(caveNumber)#delete this line for simplicity and clean up the logic
	
	print('Do you want to play again? (yes or no)')
	playAgain = input()
	if playAgain == "no":
		print("Thanks for planing")#typo "planing" to "playing"
