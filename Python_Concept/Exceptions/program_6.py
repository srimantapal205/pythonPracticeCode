#A python program to understand the effect of an exception
#An exception example
#open a file
f = open("myfile", "w")

#do some processing on the file
#accept a, b values, store the result of a/b into the file
a,b = [int(x) for x in input("Enter two number :: ").split()]
c = a/b
f.write("writeing %d into myfile "%c) 

#close the file
f.close()
print("File closed")

#1st time
#Enter two number :: 10 2
#File closed

#2nd Time
#Enter two number :: 10 0
#Traceback (most recent call last):
#   ZeroDivisionError: division by zero