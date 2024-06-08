import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 10  # Set the number of attempts

    for attempt in range(1, attempts + 1):
        # Ask the user to guess the number
        guess = int(input(f"Attempt {attempt}/{attempts}: Take a guess: "))
        
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job! You guessed the number in {attempt} attempts.")
            break
    else:
        print(f"Sorry, you've used all {attempts} attempts. The number was {secret_number}.")

if __name__ == "__main__":
    number_guessing_game()
