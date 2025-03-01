file_read = open('project file.txt','r')
print("File in Read mode - ")
print(file_read.read())
file_read.close()

file_write = open('project file.txt','w')
file_write.write("File in Write mode...")
file_write.write("Hi I am a Cr Of class 8")
file_write.close()

file_append = open('project file.txt','a')
file_append.write("\n File in Append mode...")
file_append.write("Hi I am Cr of class 8")
file_append.close()