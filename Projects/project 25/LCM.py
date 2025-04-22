import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

print("🎮LCM Game Type 'exit' to quit")

while True:
    x = input("First Number: ")
    if x.lower() == 'exit': break
    y = input("Secod Number: ")
    if y.lower() == 'exit': break

    if x.isdigit() and y.isdigit():
        a, b = int(x), int(y)
        print(f"LCM of {a} and {b} is {lcm(a, b)}\n")
    else:
        print("Numbers only, please\n")

print("Bye You're an LCM Hero~ \n")