#To find the power value of a number when it is raised t a particuler power and using add_ argument()
import argparse

#call the ArgumentParser()
parser = argparse.ArgumentParser()

#Add the arguments to the parseer
parser.add_argument('num', nargs=2)

#Retrive the arguments into the args object
args = parser.parse_args()

#Find the power value
#args.num represent the list
x = args.num[0]
y = args.num[1]
print("Numbers = ", x)
print("Its Power = ", y)

#Convert the arguments into float and then find power
result = float(x)**float(y) # Numbers =  1.5 Its Power =  2

print("The result = ", result) #The result =  2.25


