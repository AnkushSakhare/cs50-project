import random

# Global choices list
choices = ["rock", "paper", "scissors"]

# Function to display game rules
def show_rules():
    print("\n--- Rock, Paper, Scissors Rules ---")
    print("- Rock beats Scissors")
    print("- Scissors beats Paper")
    print("- Paper beats Rock")
    print("- If both players choose the same, it's a tie\n")

# Get user choice with validation
def get_user_choice():
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while choice not in choices:
        print("Invalid choice. Try again.")
        choice = input("Enter rock, paper, or scissors: ").lower()
    return choice

# Get computer's random choice
def get_computer_choice():
    return random.choice(choices)

# Determine winner
def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

# Player vs. Computer game round
def play_user_vs_computer():
    user = get_user_choice()
    computer = get_computer_choice()
    print(f"You chose: {user}")
    print(f"Computer chose: {computer}")
    print(determine_winner(user, computer))

# Player vs. Player game round
def play_player_vs_player():
    print("\n--- Player 1 ---")
    player1 = get_user_choice()
    print("\n" * 50)  # Clear screen simulation

    print("--- Player 2 ---")
    player2 = get_user_choice()
    print(f"Player 1 chose: {player1}")
    print(f"Player 2 chose: {player2}")
    result = determine_pvp_winner(player1, player2)
    print(result)

# Determine PvP winner
def determine_pvp_winner(p1, p2):
    if p1 == p2:
        return "It's a tie!"
    elif (p1 == "rock" and p2 == "scissors") or \
         (p1 == "paper" and p2 == "rock") or \
         (p1 == "scissors" and p2 == "paper"):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

# Ask if user wants to quit
def ask_to_quit():
    answer = input("Do you want to play again? (yes/no): ").lower()
    while answer not in ["yes", "no"]:
        print("Please enter 'yes' or 'no'.")
        answer = input("Do you want to play again? (yes/no): ").lower()
    return answer == "no"

# Game mode selection
def choose_mode():
    print("\nSelect Game Mode:")
    print("1. Player vs Computer")
    print("2. Player vs Player")
    print("3. Show Rules")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ").strip()
    return choice

# Main game loop
def main():
    print("Welcome to Rock, Paper, Scissors!")

    while True:
        mode = choose_mode()

        if mode == "1":
            play_user_vs_computer()
        elif mode == "2":
            play_player_vs_player()
        elif mode == "3":
            show_rules()
        elif mode == "4":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")
            continue

        if ask_to_quit():
            print("Goodbye!")
            break

# Run the game
if __name__ == "__main__":
    main()
