file1 = open('Coding.txt','r')
file2 = open('Coding.txt','w')

for line in file1.readlines():
    if not (line.startswith('I')):

        print(line)

        file2.write(line)

file2.close()
file1.close()