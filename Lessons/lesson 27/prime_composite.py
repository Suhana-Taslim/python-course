print("🎈Prime Or Composite checker (1 to 3000)🎈")
num = int(input("Enter a number between 1 and 3000: "))

if num < 1 or num > 3000:
    print("Please Enter a number between 1 and 3000")
elif num == 1:
    print("1 is neither prime nor composite")
else:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is COMPOSITE")
            break
        else:
            print(f"{num} is Prime Number")