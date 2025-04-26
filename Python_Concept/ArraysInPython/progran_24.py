#Python program to perform some mathematical operation on a numpy array
from numpy import *

#Create a array using numpy array()
arr = array([90.5, 80.4 ,70.3, -60, -50, -40, 30, 20, 10])
print('Original Array :: ', arr)

#Do arithmetic operations on the elements of the array
addArray = arr+5
print('After adding 5 :: ', addArray)

subsArray = arr - 3
print('After Subtracting 3 :: ', subsArray)

multArray = arr * 4
print('After multiplying with 5 :: ', multArray)

divdArray = arr/5
print('After dividing with 5 :: ', divdArray)

modulusArray = arr%5
print('After Modulus with 5 :: ', modulusArray)

#Use the array expressions
exprArray = (arr+5)**2-5
print("Expressions Value :: ", exprArray)

#Do some math function
sinArray = sin(arr)
print("Sin values :: ", sinArray)

cosArray = cos(arr)
print('Cos Values :: ', cosArray)

tanArray = tan(arr)
print('Tan values :: ', tanArray)

bigestElement = max(arr)
print('Bigest value :: ', bigestElement)

smallElement = min(arr)
print("Smallest element :: ",smallElement)

totalSum = sum(arr)
print("Sum of all element :: ", totalSum)

avgElemnt = mean(arr)
print("Avarage all elements :: ", avgElemnt)

