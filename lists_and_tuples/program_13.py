#A Python program to add two matrices and display the sum matrix using list
#take a matrix one with 3 row and 4 column
m1 =[[1,2,3,0],
       [4,5,6,0],
       [7,8,9,0]]

#take matris 2 with 3 row and 4 column
m2 = [[1,2,3,4],
        [1,0,1,0],
        [2,-1,-2,1]]

#Display matrix 
def displayMatrix(mat):
    for i in range(3):
        for j in range(4):
            print('%d'%mat[i][j], end=' ')
        print()

print('Display matrix - 1 :: == ')
displayMatrix(m1)
print()

print('Display matrix - 2 :: == ')
displayMatrix(m2)

#Take matrix three with 3 rows and 4 cols and initialize with all 0s 
m3 = [4*[0] for i in range(3)] #repete 0s  for 3 times

#add the corresponding elements of m1 and m2 and store in to m3
for i in range(3):
    for j in range(4):
        m3[i][j]= m1[i][j]+m2[i][j]
        
#display the third matrix using for loop
# for i in range(3):
#     for j in range(4):
#         print('%d '%m3[i][j], end='' )
#     print()

print()
print('Display new matrix after addition == ')
displayMatrix(m3)


