#A python program to access each element of a string forword and reverse order using while loop
strTxt = 'Core Python'
#Access each character using while loop
n= len(strTxt) # n = no. of chars in str

i = 0 #i = 0,1,,2... n-1
while i < n:
    print(strTxt[i], end= " ")
    i+=1

print() #put cursor in to next line

#access in reverse order
i = -1 #access in reverse order
while i >= -n:
    print(strTxt[i], end= " ")
    i-=1

print() #put cursor in to next line

i =1
while i <= n:
    print(strTxt[-i], end= " ")
    i += 1

    
 