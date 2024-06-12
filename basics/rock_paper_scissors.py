import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


print("".center(40, "_"))
print("ROCK_PAPER_SCISSORS".center(40, "_"))
print("".center(40, "_"))

player_choice = int(input("Enter Your Turn: \n 1 -> ROCK \n 2 -> PAPER\n 3 -> SCISSORS \n\n"))

# Make sure the user enters 1 -2 OR 3: 
if player_choice < 1 or player_choice > 3:
    sys.exit("Enter a number betweeen 1 and 3.")

# Computer Choice: 
computer_choice = int(random.choice("123"))

print("Player chose " + str(RPS(player_choice)).replace('RPS.', '') + " .")
print("python chose " + str(RPS(computer_choice)).replace('RPS.', '') + " .")

# Better way of doing it: 
if player_choice == 1 and computer_choice == 3:
    print("YOU WIN!")
    print("PLAYER Choice: " + str(player_choice) + "-> 🤘")
    print("Computer Choice: " + str(computer_choice) + "-> ✂️")
elif player_choice == 2 and computer_choice == 1:
    print("YOU WIN!")
    print("PLAYER Choice: " + str(player_choice) + "-> 📃")
    print("Computer Choice: " + str(computer_choice) + "-> 🤘")
elif (player_choice == 3 and computer_choice == 2):
    print("YOU WIN!")
    print("PLAYER Choice: " + str(player_choice) + "-> ✂️")
    print("Computer Choice: " + str(computer_choice) + "-> 🤘")
elif (player_choice == computer_choice):
    print("TIE!")
    print(player_choice)
    print(computer_choice)
else:
    print("🐍 Wins!")
    print(player_choice)
    print(computer_choice)
