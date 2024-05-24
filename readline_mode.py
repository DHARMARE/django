file = open("file1.txt","r")
data = file.readline() # reads single line, the first one
print(data)
file.close()

file = open("file1.txt","r")
data = file.readlines() #reads all the lines in the file but stores them in list format
print(data)
file.close()