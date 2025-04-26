#Insert a sub string in a string in particuler position
strn = input("Enter a string :: ")
sub = input("Enter a substring :: ")
n = int(input("Enter position no :: "))

#Decrease n by 1 to insert a correct position
n-=1

#Find rhe number of characters in strn and sub
l1 = len(strn)
l2 = len(sub)

#take another sting as a list
str1=[]

#append 0 to n-1 characters from strn to str1
for i in range(n):
    str1.append(strn[i])

#Append sub string o strl
for i in range(l2):
    str1.append(sub[i])
    
#Appendthe remaining characters from strn to str1
for i in range(n, l1):
    str1.append(strn[i])

str1 =''.join(str1)

print(str1)