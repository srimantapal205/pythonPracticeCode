#A python Program to search for the position of a string in a given group of string
#Search for a string in a group of string

mainStr =[]
#Accept how may string
np = int(input("How many strings ? :: "))

#append strings to array
for i in range(np):
    print("Enter a string :: ", end=" ")
    mainStr.append(input())
#Original Array
print(mainStr)

#Ask for the string search
ser = input("Enter string for search :: ")

#linear search or sequntial search
flag = False

for i in range(len(mainStr)):
    if ser == mainStr[i]:
        print("Founf at : ", i+1)
        flag = True

if flag==False:
    print("Item Not found")
