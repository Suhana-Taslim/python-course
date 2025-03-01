file_read = open('file.txt','r')
print("File in Read mode - ")
print(file_read.read())
file_read.close()

file_write = open('file.txt','w')
file_write.write("File in Write mode...")
file_write.write("Hi I am a Penguin I am 1.5 years old")
file_write.close()

file_append = open('file.txt','a')
file_append.write("\n File in Append mode...")
file_append.write("Hi I am a Penguin I am 1 year old")
file_append.close()