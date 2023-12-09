#A python program to access the characters of a string using for loop
strTxt = "Core Python"

#access each letter using for loop
for i in strTxt:
    print(i, end='')
print()

#access in reverce order
for i in strTxt[:: -1]:
    print(i, end=' ')

