import math

def start_game():
    print("🎮Welcome to the GCD game for kids!🎮\n")
    print("GCD means the Greatest Common divisor of two numbers\n")
    print("Let's find the biggest number that divides both!!\n")

    while True:
        num1 = input("Enter the first number (or type 'exit' to quit) : ")
        if num1.lower() == 'exit':
            print("Thanks for playing you are a math star 🌟")

        num2 = input("Enter the second number:")
        if num2.lower() == 'exit':
            print("Thanks for playing Keep Rocking numbers!!")
            break

        if not num1.isdigit() or not num2.isdigit():
            print("PLease enter numbers only ! no letters or symbols\n")
            continue

        a = int(num1)
        b = int(num2)
        gcd = math.gcd(a,b)

        print(f"✅ The GCD of {a} and {b} is: {gcd}\n")

start_game()