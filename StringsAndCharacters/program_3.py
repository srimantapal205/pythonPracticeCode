#A program whether sub string is in main string or not
str1 = input('Enter main string :: ')
subStr = input("Enter sub string :: ")

if subStr in str1:
    print('Sub sting " {}" found in the main String :: {}'.format(subStr, str1))
else:
    print('"{}" Not found'.format(subStr))