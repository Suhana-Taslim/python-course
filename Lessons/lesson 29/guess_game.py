import random

def guess_game():
    print("Welcome to the number gueesing game:")
    print("I'm thinking of a number between 1 and 20")

    number = random.randint(1, 20)

    while True:
        guess = input("Take a guess:")

        if not guess.isdigit():
            print("Please enter a number\n")
            continue

        guess = int(guess)

        if guess < 1 or guess > 20:
            print("Pick a number from 1 to 20")
        elif guess < number:
            print("Too low. Try again.\n")
        elif guess > number:
            print("You Got it Great Job !!")
            break

guess_game()