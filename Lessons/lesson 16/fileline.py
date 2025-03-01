file = open('Coding.txt','r')
print("Reading first line...")
print(file.readline())
file.close()

file = open('Coding.txt','r')
print("Reading Multiple lines...")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

file = open('Coding.txt','r')
print("Looping throught the lines...")
for line in file:
    print(line)
file.close()