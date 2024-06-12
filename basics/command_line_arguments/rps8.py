import sys
import os
import random
from enum import Enum


def rps(name="Alexander"):
    GAME_COUNT = 0
    PLAYER_SCORE = 0
    COMPUTER_SCORE = 0
    GAME_TIED = 0

    def play_RPS():
        nonlocal name
        nonlocal PLAYER_SCORE
        nonlocal COMPUTER_SCORE
        nonlocal GAME_TIED

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        print("".center(40, "_"))
        print("ROCK_PAPER_SCISSORS".center(40, "_"))
        print("".center(40, "_"))

        PLAYER_CHOICE = int((input(f"\n {name}, please enter.. \n 1 -> ROCK \n 2 -> PAPER\n 3 -> SCISSORS \n\n")))

        if (PLAYER_CHOICE not in [1, 2, 3]):
            print(f"{name}, please enter a number between 1 and 3.")
            return play_RPS()

        print("".center(40, "_"))

        # Computer Choice: 
        COMPUTER_CHOICE = int(random.choice("123"))

        print(f"\n{name}, chose {str(RPS(PLAYER_CHOICE)).replace('RPS.', '')}")
        print(f"\nPython chose {str(RPS(COMPUTER_CHOICE)).replace('RPS.', '')}.\n")

        def decide_winner(PLAYER_CHOICE, COMPUTER_CHOICE):
            nonlocal name
            nonlocal PLAYER_SCORE
            nonlocal COMPUTER_SCORE
            nonlocal GAME_TIED

            # Better way of doing it:
            if PLAYER_CHOICE == 1 and COMPUTER_CHOICE == 3:
                PLAYER_SCORE += 1
                return f"{name}, YOU WIN!"
            elif PLAYER_CHOICE == 2 and COMPUTER_CHOICE == 1:
                PLAYER_SCORE += 1
                return f"{name}, YOU WIN!"
            elif PLAYER_CHOICE == 3 and COMPUTER_CHOICE == 2:
                PLAYER_SCORE += 1
                return f"{name}, YOU WIN!"
            elif PLAYER_CHOICE == COMPUTER_CHOICE:
                GAME_TIED += 1
                return "TIE!"
            else:
                COMPUTER_SCORE += 1
                return "🐍 Wins!"

        game_result = decide_winner(PLAYER_CHOICE, COMPUTER_CHOICE)
        print(game_result)

        nonlocal GAME_COUNT
        GAME_COUNT += 1

        print(f"\n Game Count: {GAME_COUNT}")
        print(f"\n {name}'s Score:{PLAYER_SCORE}")
        print(f"\n Computer Score:{COMPUTER_SCORE}")
        print(f"\n Game Tied:{GAME_TIED}")

        print(f"\n {name}, would you like to play Again?")

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
            sys.exit(f"Bye {name}! 👋")

    return play_RPS


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides Personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name"
        , required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()
