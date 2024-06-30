import random

print("Welcome to the Guessing Game!")
print("Try to guess the number I am thinking of between 1 and 100.")

# Generating random number
number = random.randint(1, 100)  

guess = None  

while guess != number:
    try:
        guess_str = input("Enter your guess: ")
        
        # converting input to integer
        guess = int(guess_str)  

        if guess < 1 or guess > 100:
            print("Guess a number between 1 and 100.")
            continue  

        if guess < number:
            print("Too low, try again.")
        elif guess > number:
            print("Too high, try again.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue 

print(f"Congratulations! You guessed the number {number} correctly!")
