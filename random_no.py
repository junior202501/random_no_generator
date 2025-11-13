import random
import sys

def generate_no() -> int:
    """Generates the secret number between 1 and 100."""
    return random.randint(1, 100)

MAX_ATTEMPTS = 10

def welcome_users():
    """Display a welcome message to the user"""
    print("\n" + "<" + "="*70 + ">")
    print("      Welcome to the Random Number Guessing Game!")
    print("<" + "="*72 + ">")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have **{{MAX_ATTEMPTS}}** attempts to guess it. Type 'Q' to quit at any time. Good luck!")
    print("<" + "="*70 + ">" + "\n")

def play_one_round():
    """Contains the core logic for a single game."""    
    
    secret_number = generate_no()
    attempts = 0 
    
    while attempts < MAX_ATTEMPTS: 
        attempts += 1
        remaining_attempts = MAX_ATTEMPTS - attempts
        
        prompt = f"Guess #{attempts} ({remaining_attempts} left): Enter a number between (1-100) or 'Q'): "
        choice_str = input(prompt).strip()
        
        if choice_str.lower() == "q":
            print("\nOk, bye for now!")
            sys.exit(0)

        try:
            guess = int(choice_str)
        except ValueError:
            print(":( Invalid input. Please enter a whole number or 'Q'.")
            attempts -= 1
            continue

            # Interactin with user based on input
        if not (1 <= guess <= 100):
            print(":/ Your guess must be between 1 and 100. Try again.")
            attempts -= 1 
            continue

        if guess == secret_number:
            print(f"\n **WHOOOAAAAA,FANTASTIC!** You got it right!")
            print(f"The secret number was {secret_number} and it took you only **{attempts}** guesses.")
            return
        elif guess < secret_number:
            print("Whoops, Too Low. Guess higher.")
        else:
            print("Whoops, Too High. Guess lower.")

    print("\n **GAME OVER!** I'm sorry but you ran out of attempts.")
    print(f"The secret number was: **{secret_number}**.")

def run_game_loop():
    """Manages the continuous play structure."""
    welcome_users()
    
    while True:
        play_one_round()
        
        play_again = input("\nDo you want to play again? You might win this time (Y/N): ").strip().lower()
        if play_again not in ('y', 'yes'):
            print("\nThanks for playing btw! Goodbye.")
            break

run_game_loop()