print("🎈Welcome to the prime number checker🎈\n")
print("😊 Let's see if your number is prime or not \n")

num = int(input("Enter a Number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(f"🥲Oh No!! {num} is not a prime number")
            break
        else:
            print(f"Yayyy!! {num} is a Prime number")
    else:
        print("Numbers less than 2 are not prime")

print("Thanks for playing Keep learning and exploring")