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

