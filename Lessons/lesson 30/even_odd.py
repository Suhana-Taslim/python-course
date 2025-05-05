import random
print("Let's find the Odd numbers")
print("Odd numbers are end in 1, 3, 5, 7, 9.")

numbers = random.sample(range(1, 100),5)

print("\n look at these numbers:")
for num in numbers:
    print(num)

score = 0
for num in numbers:
    answer = input(f"\n Is {num} an odd number?(yes or no): ").lower()
    if (num % 2 == 1 and answer =="yes") or (num % 2==0 and answer == "no"):
        print("Correct!!")
        score += 1
    else:
        print("Oops That's not right.")
        if num % 2 == 1:
            print(f"{num} is ODD")
        else:
            print(f"{num} is EVEN")

print(f"\n All done You gor {score} out of 5 correct")