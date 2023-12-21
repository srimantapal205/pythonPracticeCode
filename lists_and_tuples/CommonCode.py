#Connection of two lists
x = [10,20,30,40,50]
y = [100,110,120]
neLst = x+y
print(neLst)

#Repetition of list
nlst = [10,20,30,40,50,60,70,80,90,100]
print(nlst * 2)

#Membership in list
a = 110
print(a in nlst) #check if a is member of x

#Aliasing and cloning lists
m = [10,20,30,40,50]
n=m # m is aliased as y
print(m) #will display [10,20,30,40,50]
print(n) #will display [10,20,30,40,50]
m[1] = 99 #modify 1st element in x
print(m) #will display [10,99,30,40,50]
print(n) #will display [10,99,30,40,50]

a = [10,20,30,40,50]
b=a[:] # x is cloned as y
print(a) #will display [10,20,30,40,50]
print(b) #will display [10,20,30,40,50]
a[1]=99
print(a) #will display [10,99,30,40,50]
print(b) #will display [10,99,30,40,50]

