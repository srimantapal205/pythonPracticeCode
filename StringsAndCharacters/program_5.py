#Find first occurance to find the sub string in the given string using index()
mainStr = input('Enter main string :: ')
subStr = input('Enter sub string :: ')

#find position of sub in main string
#Search 0 to last character in str
try:
    n = mainStr.index(subStr, 0, len(subStr))
except ValueError:
    print('Sub string not found')
else:
    print('Sub string found at {} position'.format(n+1))
    