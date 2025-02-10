# Dice Game
print("Welcome to the Dice Game!")

# Importing the random module
import random as r

# Define dice roll function
def dice_roll():
    dice1 = r.randint(1, 6)
    dice2 = r.randint(1, 6)
    return print(f"Your dice roll is {dice1},{dice2}")


# Define dice game
def dice_game():
    game_play = input("Would you like to play the dice game? (yes/no): ").lower()
    if game_play == "yes":
        print("Great! Let's play!")
    elif game_play == "no":
        print("That's okay! Maybe next time!")
        exit()
    else:
        print("Invalid input! Please try again!")
        dice_game()

# Call dice game function
while True:
    dice_game()
    dice_roll()
