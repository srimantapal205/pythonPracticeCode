#Python program to retrive elements from a matrix and display them
#take a nested list
mat = [[1,2,3],[4,5,6],[7,8,9]]

print('Display the list a it is :: ')
print(mat)
print()

print('Display row by row')
for r in mat:
    print(r)
print()

print('Display is column in row 0 :: ')
for c in mat[0]:
    print(c)
print()

print('Display is column in row 1 :: ')
for c in mat[1]:
    print(c)
print()

print('Display is column in row 2 :: ')
for c in mat[2]:
    print(c)
print()

print('Display all elements using for ::')
for r in mat:
    for c in r:
        print(c, end=' ')
    print()
print()

print('Display all elements using for :: ')
for i in range(len(mat)):
    for j in range(len(mat[i])):
        print('%d' %mat[i][j], end=' ')
    print()

