import pytest
import random
from project import determine_winner, determine_pvp_winner, get_computer_choice


# Test user vs computer logic
@pytest.mark.parametrize("user, computer, expected", [
    ("rock", "scissors", "You win!"),
    ("paper", "rock", "You win!"),
    ("scissors", "paper", "You win!"),
    ("rock", "rock", "It's a tie!"),
    ("rock", "paper", "Computer wins!"),
])
def test_determine_winner(user, computer, expected):
    assert determine_winner(user, computer) == expected

# Test player vs player logic
@pytest.mark.parametrize("p1, p2, expected", [
    ("rock", "rock", "It's a tie!"),
    ("rock", "scissors", "Player 1 wins!"),
    ("paper", "scissors", "Player 2 wins!"),
])
def test_determine_pvp_winner(p1, p2, expected):
    assert determine_pvp_winner(p1, p2) == expected

# Test computer random choice returns valid result
def test_get_computer_choice():
    assert get_computer_choice() in ["rock", "paper", "scissors"]
