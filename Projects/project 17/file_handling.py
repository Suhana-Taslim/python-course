with open('Codingal.txt','w') as file:
    file.write("Hi I am Penguviii i am doing my projects right now.")
file.close()

with open('Codingal.txt','r') as file:
    data = file.readlines()
    print("Words in the file are....")
    for line in data:
        word = line.split()
        print(word)
file.close()