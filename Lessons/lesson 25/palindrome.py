def is_palindrome_number(number):
    return number == number[::-1]

def start_game():
    print("🎉Welcome to the number Palimdrome game!!")
    print("A Palindrome number reads the same word forward and backward!")

    while True:
        number = input("🔢Enter a number to check(or type 'exit' to quit)")

        if number.lower()== "exit":
            print("Thanks for playing !! Keep Playing Have fun with numbers")
            break

        if not number.isdigit():
            print("Please enter *numbers only* No letters or symbols")
            continue

        if is_palindrome_number(number):
            print(f"✅Awesome!! {number} is  palindrome🥳\n")
        else:
            print(f"❌Oops!! {number} is not a palindrome.Try Again...\n")

start_game()