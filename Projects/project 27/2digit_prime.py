import math

print("All 2 Digit Prime numbers are\n")
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

for num in range(10, 100):
    if is_prime(num):
        print(num, end=' ')
