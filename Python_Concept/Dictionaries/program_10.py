#A python program to convert a string into key-value pairs and store them into dictionary
#converting a string into a dictionary
#take a string

strValue ='Vijay=23,Ganesh=20,Lakshmi=19,Nikhil=22'

#break the string at ','and then at '=' 
#store it in a list
lst =[]
for x in strValue.split(','):
    y = x.split('=')
    lst.append(y)
    print(lst)

#convert the list into dictionary 'd' but this 'd' will have both name and age as string
d = dict(lst)
print(d)

#create a new dictionary d1 with name as string and age as integer
d1={}
for k, v in d.items():
    d1[k] = int(v)

#display the final dictionary
print(d1)



