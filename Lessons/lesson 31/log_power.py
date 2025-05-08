import math

print("let's see how numbers grow...")
print("number\tlog2(n)\tn^2")
print("." * 25)

for n in range(1, 11):
    log_value = round(math.log2(n), 2)
    square = n ** 2
    print(f"{n}\t{log_value}\t\t{square}")