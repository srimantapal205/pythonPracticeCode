cmnStr = "Core Python"

for i in cmnStr:print(i, end=" ")
print('\n')

for i in cmnStr[::-1]:print(i, end="")
print('\n')

for i in cmnStr[0:9:1]:print(i, end="")
print('\n')

for i in cmnStr[:9:2]:print(i, end="")
print('\n')

for i in cmnStr[2:4:1]:print(i, end="")
print('\n')

for i in cmnStr[2::]:print(i, end="")
print('\n')

for i in cmnStr[:4:]:print(i, end="")
print('\n')

for i in cmnStr[:-4:]:print(i, end="")
print('\n')

for i in cmnStr[:-4:-2]:print(i, end="")
print('\n')

for i in cmnStr[1:-4:2]:print(i, end="")
print('\n')

for i in cmnStr[-1::-1]:print(i, end="")
print('\n')

for i in cmnStr[::-1]:print(i, end="")
print('\n')

#Repeating text
print(cmnStr * 2)

s = cmnStr[5:7]*3
print(s)

#Concatenation String
str1 ="Core"
spc = " "
str2 = " Python"

print(str1+spc+str2)