#A python program to copy an image file into another file
#copy an image into file
#open the files in binary mode
f1 = open('dog.jpeg', "rb")
f2 = open('new_dog.jpeg', 'wb')

#read bytes from f1 file and write in to f2 file
bytesCode = f1.read()
print(bytesCode)
f2.write(bytesCode)

#close file
f1.close()
f2.close()