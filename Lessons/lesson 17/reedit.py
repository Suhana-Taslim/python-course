new_file = open('momo1.txt','x')
new_file.close()

import os
print("Checking if momo1 file exists or not...")
if os.path.exists("momo1.txt exists"):
    os.remove("momo1.txt")
else:
    print("The file does not exist")

momo = open("momo.txt","w")
momo.write("Hi I am Momo And I am a cat of 2 years Age I am White in color")
momo.close()

os.remove('momo1.txt')
