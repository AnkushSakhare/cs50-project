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

# to create a game.
def get_game():
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

# to find the result of the game.
def get_result(player 1,player 2):

    Determines the winner of rock, paper, scissors.

    Args:
        player 1 = choices of player 1('rock', 'paper', or 'scissors')
        player 2 = choices of player 2('rock', 'paper', or 'scissors')

    returns:
        str: Result of the game('player 1 wins', 'player 2 wins', or 'Tie')

    reules = {
        'rock': 'scissors',
        'scissors': 'paper',
        'scissors': 'scissors'
    }

    if player 1 == player 2:
        returns "Tie"
    elif rules[player 1] == player 2:
        returns "player 1 wins"
    else:
        returns "player 2 wins"

def get_rules():
    print("rock, paper, scissors Ruls")
    print("- rock beats scissors")
    print("- scissors beats paper")
    print("- paper beats rock")
    print("- If both players choose the same, It's a tie")

def get_play():
    return input("choose rock, paper, or  scissors: ").lower()

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors")
    or \ (user == "scissors" and computer == "paper")
    or \ (user == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "You lose!"

def get_rules():
    user = get_play()
    if user not in ["rock", "paper", "scissors"]:
        print("Invalid input.")
        return
    computer = get_computer_play()
    print(f"computer chose:{computer}")
    print(determine_winner(user, computer))

def play():
    user = get_user_choice()
    computer = get_computer_choice()

    print(f"you chose: {user}")
    print(f"computer chose: {computer}")

    print(determine_winner(user, computer))

def get_user_choice():
    choice = input("Enter your choice (rock, paper, scissors): ").lower()

    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice")
        choice = input("Enter rock, paper, or scissors: ").lower()
    return choice
def get_player_vs_player():
    



def get_quit():
    answer = input("Do you want to play again? (yes/no): ").lower()
    while answer not in["yes" or "no"]:
        print("please enter 'yes' or 'no'")
        answer = input("Do you want to play again? (yes/no): ").lower()
    return answer == "no"
