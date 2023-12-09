cmnStr = "Core Python"
'''
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
'''
#Comparing Strings
s1 = "Box"
s2 = "Boy"
if(s1==s2):
    print("Both are same")
else:
    print("Not same")
    
if s1<s2:
  print("S1 less then s2")
else:
    print('S1 greater than or equal to s2')
    
#Removing space  from a string
spaceString = "  This is core python   "

x = len(spaceString)
print(x)
print("Original String :: ", spaceString)

#Remove space from right side
rrs= spaceString.rstrip()
print("Revove Space from right side :: ", rrs, " Length :: ", len(rrs))

#Remove space from left side
rls= spaceString.lstrip()
print("Revove Space from left side :: ", rrs, " Length :: ", len(rls))

#Remove space from both side
ras = spaceString.strip()
print("Revove Space from left side :: ", ras, " Length :: ", len(ras))


