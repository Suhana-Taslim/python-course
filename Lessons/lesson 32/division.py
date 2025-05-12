print("Lets do easy division")

a = int(input("Big Number: "))
b = int(input("Small Number: "))

if b == 0:
      print("Cant divide by zero")
else:
      count = 0
      while a >= b:
            a = a - b
            count = count + 1

print("^_^ Answer is:")
print("Times = ",count)
print("left =",a)