#Create a python program to sort a group of program in alphabetical number
#sorting a group of string

mainStr = []
#accept how many sting
inp = int(input("How many strings ? "))

for i in range(inp):
    print("Enter string :: ", end="")
    mainStr.append(input())

#Print Original array
print(mainStr)

#sort the array
#mainStr.sort()
newString = sorted(mainStr)

for i in newString:
    print(i)
