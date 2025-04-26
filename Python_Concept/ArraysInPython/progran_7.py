#Write a program that helps to know the effect of slicing operation on an array
from array import *
x = array('i', [10,20,30,40,50,60,70,80,90])
#Crate array y with elements from 1st to 3 rd from x
y = x[1:4]
print(y)

#Create array y with elements from 0th till the last elements in x
y= x[0:]
print(y)

#Create array y with elements from 0th to 3rd from x
y=x[:4]
print(y)

#Create array y with last 4 elements from x
y=x[-4:]
print(y)

#Create y with last 4th element and with 3 [-4-(-1)=-3] elements to words right.
y = x[-4: -1]

#Create y with 0th to 7th elements from x stride 2 means after 0th element, retrive every 2nd element x
y=x[0:7:2]
print(y)