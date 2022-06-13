import random

user_action = input("Enter your choice (r, p, s): ")
possible_actions = ["r", "p", "s"]
if user_action not in possible_actions:
  print("That is an invalid selection. Please try again")
computer_action = random.choice(possible_actions)
# print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
# evaluate action equality first, to reduce number of cases and simplify rest of elif blocks
if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "r":
    if computer_action == "s":
        print("Rock crushes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_action == "p":
    if computer_action == "r":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_action == "s":
    if computer_action == "p":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock crushes scissors! You lose.")


# If the two players choose the same “character” it’s a tie, and the game repeats
# Rock beats Scissors
# Paper beats Rock
# Scissors beats Paper
# You have been tasked to create a simple version of this game with Python. 
# In your version, one player will be controlled by the computer and the other player controlled by you - 
# the user (i.e CPU vs Player). 

# You should make use of the inbuilt Python module random and its choice method.

# Instructions:

# Create a new Python file and call it main.py. Inside it you'll create your game.
# Create a list to store all possible options:
# "R" for "rock", 
# "P" for "paper", 
# "S" for "scissors".
# When the program is run, ask the user to pick an option between "R", "P" or "S"
# If user input is invalid (not amongst our options), print an error, and ask for their input again (should be a loop)
# Use the `choice` function from the inbuilt Python `random` module to make a choice for CPU player(computer).
# Print both player's moves in the format: `Player (Rock) : CPU (Paper)`
# Check both player's moves: 
# If there is a winner, print the winner, and the program ends. 
# If it's a tie (the computer and player pick the same move), restart the game from step 3