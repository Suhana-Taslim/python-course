number = int(input("enter a number:"))
binary = bin(number)[2:]
print("Binary is:",binary)

n = int(input("which bit number do you want to print? (1= first from left); "))

if 1 <= n <=len(binary):
    Bit binary[n-1]
    print("Thats a bit.\n",bit)
else:
    print("not a bit")
    break
