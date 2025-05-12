print("welcome to the swappping game!!")
print("let's swap 2 numbers magically")


num1 = input("enter the first number: ")
num2 = input("enter the second number")

print(f"\n before swapping : num1 = {num1}, num2 = {num2}")
print("swapping the numbers...")


temp = num1
num1 = num2
num2 = temp

print(f"After swapping : num1 = {num1}, num2 = {num2}")
print("ta-daa the numbers have been swapped")