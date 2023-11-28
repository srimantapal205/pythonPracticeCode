#Write a pyhon program to create an interger type array

import array
a = array.array('i', [1,2,3,4,5])
print('The array elements are:: ')
for element in a:
    print(element)