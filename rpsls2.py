import math
import random

while True:
    name = raw_input('Please chooses rock-paper-scissors-lizard-Spock: ')
    if name != ['rock' or "Spock" or "scissors" or "paper" or "lizard"]:
        name = raw_input('Please chooses rock-paper-scissors-lizard-Spock: ')
    break
print "Player chooses ", name

def name_to_number(name):
    
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        name = raw_input('Please chooses rock-paper-scissors-lizard-Spock: ')
    quit()
    

name_to_number(name)

def number_to_name(number):
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        print "Please input a valid number"
    return number_to_name(number)

player_number = name_to_number(name)
computer_number = random.randrange(0,5)
computer_choice = number_to_name(computer_number)
print "Computer chooses " + computer_choice
difference = ((player_number - computer_number)%5)

if difference ==1 or difference ==2:
    print "Player wins!"
elif difference ==3 or difference==4:
    print "Computer wins!"
else:
    print "Player and Computer tie!"

        
        
        