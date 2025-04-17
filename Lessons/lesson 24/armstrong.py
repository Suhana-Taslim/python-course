import random

def is_armstrong(num):
    digits = [int(d) for d in str(num)]
    power = len(digits)
    return sum([d ** power for d in digits]) == num

def play_game():
    print("🎮 Welcome to the Armstrong Number Guessing Game!")
    print("Can You guess if the number is an armstrong number??")
    print("Type 'yes' or 'no'!!\n")

    for _ in range(5):
        number = random.randint(100, 999)
        print(f"🤔 Is {number} an Armstrong Number?") 
        answer = input("Your guess(yes/no): ").strip().lower()

        correct = is_armstrong(number)
        if (answer == 'yes' and correct) or (answer == 'no' and not correct):
            print("✅Correct \n")
        else:
            print(f"❌Oops!! the correct answer is {'yes' if correct else 'no'}.\n")

    print("🎉Game Over!! Great Job!")

play_game()