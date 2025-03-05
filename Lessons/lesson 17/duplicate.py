# creating the output file
outputFile = open('UpdatedFile.txt',"w")

#reading the input file
inputFile = open('repeated.txt',"r")

#holds lines already seen
lines_seen_so_far = set()
print("Eliminating duplicate lines...")
#iterating each line in the file
for line in inputFile:

    #checking if line is unique
    if line not in lines_seen_so_far:

        #write unique lines in output file
        outputFile.write(line)

        #adds unique lines to lines_seen_so_far
        lines_seen_so_far.add(line)

inputFile.close()
outputFile.close()