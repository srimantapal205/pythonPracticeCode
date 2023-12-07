from numpy import *

# accept the number of rows and columns
r, c = [int(a) for a in input("Enter Row & Column :: ").split()]

# accept elements as a string
input_str = input("Enter matrix elements :: \n")

# convert the string into a matrix with size r x c
matrix_elements = reshape(matrix(input_str, (r, c)))

print("The original matrix :: ")
print(matrix_elements)

print("Print the Transpose matrix :: ")
transpose_matrix = matrix_elements.transpose()
print(transpose_matrix)
 
 
 
 #/// Incomplete Program 
