#A lambda function to find the bigger number from 2 input.

max = lambda x, y : x if x > y else y #write lambda function
a, b = [int(n) for n in input('Enter two numbers :: ').split(' ')] #User input 
print('The bigger number is :: ', max(a, b)) #Call lambda function
