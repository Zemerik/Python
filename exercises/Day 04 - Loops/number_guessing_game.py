"""
Exercise 1: Number Guessing Game
Create a number guessing game where players get 5 attempts to guess a secret number between 1-20
"""

import random

def generate_secret_number():
    """Generate a random secret number between 1 and 20"""
    return random.randint(1, 20)


def get_user_guess():
    """Get and validate user's guess"""
    while True:
        try:
            guess = int(input("Enter your guess (1-20): "))
            if 1 <= guess <= 20:
                return guess
            else:
                print("Please enter a number between 1 and 20.")
        except ValueError:
            print("Please enter a valid number.")


def check_guess(guess, secret_number):
    """Check if the guess is correct, too high, or too low"""
    if guess == secret_number:
        return "correct"
    elif guess < secret_number:
        return "low"
    else:
        return "high"


def display_hint(result, attempts_left):
    """Display hint based on guess result"""
    if result == "correct":
        print("🎉 Congratulations! You guessed it!")
    elif result == "low":
        print(f"📈 Too low! Try a higher number. ({attempts_left} attempts left)")
    else:
        print(f"📉 Too high! Try a lower number. ({attempts_left} attempts left)")


def play_game():
    """Main game logic"""
    secret_number = generate_secret_number()
    max_attempts = 5
    attempts = 0
    
    print("=== Number Guessing Game ===")
    print(f"I'm thinking of a number between 1 and 20.")
    print(f"You have {max_attempts} attempts to guess it.")
    print()
    
    while attempts < max_attempts:
        attempts += 1
        attempts_left = max_attempts - attempts
        
        print(f"Attempt {attempts}/{max_attempts}")
        guess = get_user_guess()
        
        result = check_guess(guess, secret_number)
        display_hint(result, attempts_left)
        
        if result == "correct":
            print(f"You won in {attempts} attempts!")
            return True
        
        if attempts < max_attempts:
            print()
    
    print(f"\n😔 Game Over! The secret number was {secret_number}.")
    return False


def main():
    while True:
        play_game()
        
        play_again = input("\nWould you like to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break
        print("\n" + "="*30 + "\n")

if __name__ == "__main__":
    main() 