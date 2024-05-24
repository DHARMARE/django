file = open("file1.txt","r")
data = file.read(20) # reads single line, the first one
print("Data: ",data)
pos = file.tell()
print("pos of cursor: ",pos)

pos = file.seek(0,0)
data = file.read(10)
print("Data after repositioning cursor: ",data)
file.close()