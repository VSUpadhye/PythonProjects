import random

def guess_number():
    number = random.randint(1, 100)
    print("Welcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100.")

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    attempts = 0
    if difficulty == 'easy':
        attempts = 10
        print("You have 10 attempts remaining.")
    elif difficulty == 'hard':
        attempts = 5
        print("You have 5 attempts remaining.")
    else:
        attempts = 1

    guess = 0
    while attempts > 0 and guess != number:
        guess = int(input("Make a guess: "))
        if number < guess:
            print("Too high.")
        elif number > guess:
            print("Too low.")
        else:
            print(f"You got it! The answer was {guess}.")
        attempts -= 1
        if guess != number and attempts != 0:
            print(f"You have {attempts} attempts remaining.")
    if attempts == 0 and number != guess:
        print(f"You've run out of guesses! The correct answer was {number}.")
    goAgain = "yes"
    while goAgain == "yes":
        print("\n" * 20)
        guess_number()
        goAgain = input("Type 'yes' to go again, otherwise type 'no': ")

guess_number()