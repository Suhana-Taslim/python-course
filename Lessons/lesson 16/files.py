file = open('Coding.txt','r')
print(file.read())
file.close()

file = open('Coding.txt','r')
print("\n Read in parts\n")
print(file.read(15))
file.close()

file = open('Coding.txt','a')
file.write("Hi~ I am Suhana Taslim.")
file.close()