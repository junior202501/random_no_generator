import random
import sys

def generate_no() -> int:
    """Generates the secret number between 1 and 100."""
    return random.randint(1, 100)

def welcome_users():
    """Display a welcome message to the user"""
    print("\n" + "<" + "="*70 + ">")
    print("      Welcome to the Random Number Guessing Game!")
    print("<" + "="*72 + ">")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have **10** attempts to guess it. Type 'Q' to quit at any time. Good luck!")
    print("<" + "="*70 + ">" + "\n")

