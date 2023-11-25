#To find sum of to given numbers
import argparse

#Create ArgumentParser class object 
parser = argparse.ArgumentParser(description="This program calculates the sum of two given numbers")

#Add two arguments with the names num1 and num2 and type of float
parser.add_argument("num1", type=float, help="Input the first number : " )
parser.add_argument("num2", type=float, help="Input the second number :" )

#Retrive the arguments passed to the program
args = parser.parse_args()

#convert the n1 and n2 values into float type then add them
result = float(args.num1) + float(args.num2) #5.5 5
print("Sum of two number : ", result) # Sum of two number :  10.5

