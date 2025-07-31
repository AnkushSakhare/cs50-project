import random


def main():
    choices = ["rock", "paper", "scissors"]
    user = input("choose rock, paper, or scissors: ").lower()
    games = random.choice(choices)

    print(f"game choice:{games} ")
    if user == game:
        print("It's a tie!")
    elif (user == "rock" and game == "scissors")
    or \ (user == "paper" and game == "rock")
    or \ (user == "scissors" and game == "paper"):
    
        print("You win!")
    else:
        print("you lose!")


def game():
    print("Type 'rock', 'paper', or 'scissors' to play. Type 'quit' to stop.")

    while True:
        user_choice = input("Your choice: ").lower()
        
        if user_choice == 'quit':
            print("Thanks for playing!")
            break
        if user_choice not in choices:
            print("Invalid choice. Try again.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (
            (user_choice == 'rock' and computer_choice == 'scissors') or
            (user_choice == 'paper' and computer_choice == 'rock') or
            (user_choice == 'scissors' and computer_choice == 'paper')
        ):
            print("You win!")
        else:
            print("You lose!")
