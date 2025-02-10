# Number Guessing Game

import random as r

# Define would you like to play function
def play():
    play_game = input("Would you like to play the Number Guessing Game? (yes/no): ").lower()
    if play_game == "yes":
        print("Great! Let's play!")
    elif play_game == "no":
        print("That's okay! Maybe next time!")
        exit()
    else:
        print("Invalid input! Please try again!")
        play()

# Define number guessing game function
def number_guessing_game():
    number = r.randint(1, 10)
    guess = None
    number_of_guesses = 0
    while guess != number:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            print("You get 3 tries!")
            number_of_guesses += 1
            if guess < number:
                print("Too low! Try again!")
            elif guess > number:
                print("Too high! Try again!")
            else:
                print(f"Congratulations! You guessed the number in {number_of_guesses} tries!")
                break
            if number_of_guesses == 3:
                print(f"Sorry! You've run out of tries! The number was {number}!")
                break
        except ValueError:
            print("Invalid input! Please try again!")
            continue

# Call play function
while True:
    play()
    number_guessing_game()
    play_again = input("Would you like to play again? (yes/no): ").lower()
    if play_again == "no":
        print("That's okay! Maybe next time!")
        exit()
    elif play_again == "yes":
        print("Great! Let's play again!")
        number_guessing_game()
    else:
        print("Invalid input! Please try again!")
        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again == "no":
            print("That's okay! Maybe next time!")
            exit()
        elif play_again == "yes":
            print("Great! Let's play again!")
        else:
            print("Invalid input! Please try again!")
            exit()