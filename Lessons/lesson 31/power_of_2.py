print("Let's learn powers of 2 ")
print("Here are the powers of 2 from 0 to 10")

for i in range(11):
    print(f"2 ^ {i} = {2 ** i}")

print("\n Time for a quick quiz!!")
answer = int(input("what is 2 to the power of 3?"))

if answer == 2 ** 3:
    print("Correct answer 2^3 = 8")
else:
    print(f"Oops the correct answer is {2 ** 3}")