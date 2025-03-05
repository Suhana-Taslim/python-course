file = open('Project.txt','r')
print(file.read())
file.close()

file = open('Project.txt','r')
print("\n Read in parts\n")
print(file.read(8))
file.close()

file = open('Project.txt','a')
file.write("  \nHi I am Sheru and I am the elder brother of momo.")
file.close()