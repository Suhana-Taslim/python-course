import random

def rock_paper_scissors():
    print(" Lets play rock,paper, scissors!")
    choices = ["rock", "paper", "scissors"]

    while True:
        user = input("your turn (rock,paper,scissors): ").lower()

        if user == "exit":
            print("Bye!! Thanks for playing")
            break
        if user not in choices:
            print("please chose rock,paper,scissors.\n")
            continue

        computer = random.choice(choices)
        print("computer choose:",computer)

        if user == computer:
            print("it's a tie\n")
        elif(user == "rock" and computer == "scissors") or \ (user == "paper" and computer == "rock") or \ (user == "scissors" and computer == "paper"):
            print("")

