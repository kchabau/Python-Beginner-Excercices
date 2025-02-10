import random as r

# Would you like to play function
def play():
    play_game = input("Would you like to play the Rock Paper Scissors Game? (yes/no): ").lower()
    if play_game == "yes":
        print("Great! Let's play!")
    elif play_game == "no":
        print("That's okay! Maybe next time!")
        exit()
    else:
        print("Invalid input! Please try again!")
        play()

# Define rock paper scissors game function
def game():
    while True:
        try:
            player = input("Rock, Paper, or Scissors? (r/p/s) ").lower()
            if player == "r":
                print("You chose Rock! 🪨")
            elif player == "p":
                print("You chose Paper! 📄")
            elif player == "s":
                print("You chose Scissors! ✄")
            else:
                print("Invalid input! Please try again!")
                continue

            computer = r.choice(["r", "p", "s"])
            computer_choice = {"r": "Rock 🪨", "p": "Paper 📄", "s": "Scissors ✄"}[computer]
            print(f"Computer chose {computer_choice}")

            if player == computer:
                print("It's a tie!")
            elif (player == "r" and computer == "s") or (player == "p" and computer == "r") or (player == "s" and computer == "p"):
                print("You win!")
            else:
                print("You lose!")
            break
        except ValueError:
            print("Invalid input! Please try again!")
            continue

# Call play function
while True:
    play()
    game()
    play_again = input("Would you like to play again? (yes/no): ").lower()
    if play_again == "no":
        print("That's okay! Maybe next time!")
        exit()
    elif play_again == "yes":
        print("Great! Let's play again!")
        game()
    else:
        print("Invalid input! Please try again!")