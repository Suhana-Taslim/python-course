import random

class NumberGuessingGame:
    def __init__(self, lower=1, upper=100):
        self.secret_number = random.randint(lower, upper)

    def play(self):
        while (guess := int(input("Guess the number: "))) != self.secret_number:
            print("Too low" if guess < self.secret_number else "Too high")
        print("Congratulations! You've guessed the number.")

if __name__ == "__main__":
    NumberGuessingGame().play()
