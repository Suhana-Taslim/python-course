print("Let's learn powers of 4")
print("Here are the powers of 4 from 0 to 10:\n")

for i in range(11):
    print(f"4^{i} = {4 ** i}")

print("\n time for a quick quiz")
answer = int(input("what is 4 to the power of 2?"))

if answer == 4 ** 2:
    print("correct 4^2 = 16")
else:
    print(f"oops the correct answer is {4 ** 2}")