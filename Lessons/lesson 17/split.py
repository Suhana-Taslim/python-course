with open('momo.txt','w')as file:
    file.write("Hi I am Momo And I am a Cat.")
file.close()

with open('momo.txt','r')as file:
    data = file.readlines()
    print("Words in this file are...")
    for line in data:
        word = line.split()
        print(word)
file.close()