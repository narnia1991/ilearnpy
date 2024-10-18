import random
import os
import time


def cls():
    os.system("cls" if os.name == "nt" else "clear")


def roll_dice():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll


value = roll_dice()


# get number of players
while True:
    players = input("Enter number of players (2-4):")
    if players.isdigit():
        players = int(players)
        if 1 <= players <= 4:
            break
        else:
            print("Game can only be played with 2 - 4 players")
    else:
        print("Invalid, try again")


max_score = 50
player_scores = [0 for _ in range(players)]
prev_roll = 0

while max(player_scores) < max_score:
    for player_idx in range(players):
        cls()

        for index, score in enumerate(player_scores):
            print(f"Player{index+1}: {score}", end="; ")

        print("\nPrevious roll: ", prev_roll)
        print("\nPlayer", player_idx + 1, "turn has started!\n")

        should_roll = input(
            "WOuld you like to roll? Press any key to continue or (Q)uit\n"
        )

        if should_roll.lower() == "q":
            quit()

        value = roll_dice()
        prev_roll = value

        if value == 1:
            print("You rolled a 1! Turn Done.\n")
            player_scores[player_idx] = 0
            time.sleep(0.75)

        else:
            print("rolling: ", end="")
            player_scores[player_idx] += value
            print("...", end="", flush=True)
            time.sleep(0.7)
            print(value)
            time.sleep(0.5)


max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print(f"Player {winning_idx+1} won!!! Score is {max_score}")
