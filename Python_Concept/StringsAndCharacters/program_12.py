#Create a python to find the no of character in the string.
mainStr = input("Enter a string :: ")
i = 0
for s in mainStr:
    print(mainStr[i], end="")
    i+=1
print('\n No of characters :: ', i)
