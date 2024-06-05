import sys
import os
import random 
from enum import Enum

def play_RPS():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3
        
    PLAYER_SCORE = 0
    COMPUTER_SCORE = 0
    GAME_TIED = 0

    print("".center(40, "_"))
    print("ROCK_PAPER_SCISSORS".center(40, "_"))
    print("".center(40, "_"))

    PLAYER_CHOICE = int((input("Enter Your Turn: \n 1 -> ROCK \n 2 -> PAPER\n 3 -> SCISSORS \n\n")))
    
    if (PLAYER_CHOICE not in [1,2,3]):
        print("Enter a number betweeen 1 and 3.")
        return play_RPS()

    
    print("".center(40, "_"))
    
    # Computer Choice: 
    COMPUTER_CHOICE = int(random.choice("123")) 

    print("Player chose " + str(RPS(PLAYER_CHOICE)).replace('RPS.', '') + " .")
    print("python chose " + str(RPS(COMPUTER_CHOICE)).replace('RPS.', '') + " .")

    # Better way of doing it: 
    if PLAYER_CHOICE == 1 and COMPUTER_CHOICE == 3:
        PLAYER_SCORE += 1
        print("YOU WIN!")
        print("PLAYER Choice: " + str(PLAYER_CHOICE) + ": 🤘")
        print("Computer Choice: " + str(COMPUTER_CHOICE) + ": ✂️")
    elif PLAYER_CHOICE == 2 and COMPUTER_CHOICE == 1:
        PLAYER_SCORE += 1
        print("YOU WIN!")
        print("PLAYER Choice: " + str(PLAYER_CHOICE) + "-> 📃")
        print("Computer Choice: " + str(COMPUTER_CHOICE) + ": 🤘")
    elif(PLAYER_CHOICE == 3 and COMPUTER_CHOICE == 2):
        PLAYER_SCORE += 1
        print("YOU WIN!")
        print("PLAYER Choice: " + str(PLAYER_CHOICE) + "-> ✂️")
        print("Computer Choice: " + str(COMPUTER_CHOICE) + ": 🤘")
    elif( PLAYER_CHOICE == COMPUTER_CHOICE):
        print("TIE!")
        GAME_TIED += 1
        print(PLAYER_CHOICE)
        print(COMPUTER_CHOICE)
    else:
        COMPUTER_SCORE += 1
        print("🐍 Wins!")
        print(PLAYER_CHOICE)
        print(COMPUTER_CHOICE)
        
    print("\nPlay Again?")
    while True:
        play_again = input("\n Y for YES or\n Q for QUIT\n")
        if play_again.lower() not in ["y", "q"]:
            os.system('cls||clear')
            continue
        else:
            break

    if play_again.lower() == "y":
        os.system('cls||clear')
        return play_RPS()
    else:    
        print("\n🥳🥳🥳🥳🥳")
        print("Thank you for playing ! \n")
        print("SCORES".center(40, "-")) 
        print("\n Player Score: " + str(PLAYER_SCORE) 
            + "\n Python Score: " + str(COMPUTER_SCORE)
            + "\n Games Tied: " + str(GAME_TIED))
        print("".center(40, "-")) 
        sys.exit("Bye! 👋")
                                   
                

play_RPS()           
        
        
        
        