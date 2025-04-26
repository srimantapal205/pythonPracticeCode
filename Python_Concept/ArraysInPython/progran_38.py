#Matrix multiplication /// Incomplete Program

import sys
from numpy import *

#Accept number of rows and column of matrix in to r1 c1
r1, c1 = [int(a) for a in input(" Enter First matrix row and column :: ").split("")]

#Accept number of rows and column of matrix in to r2 c2
r2, c2 = [int(a) for a in input(" Enter Second matrix row and column :: ").split("")]

#Test the condition if c1 != r2, then multiplication is not possible 
if c1 != r2:
    print("Multiplication is not possible :: ")
    sys.exit()

#Accept first matrix elements as string into str1
str1 = input('Enter first matrix element :: \n')
#convert str1 into a matrix