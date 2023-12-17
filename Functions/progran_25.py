#A function to display the group of string
def displayString(strlst):
    '''To display the list of strings'''
    for i in strlst:
        print(i)

#take a group of string from keyboard
print('Enter group of string seperated by comma:: ')
strListValue = [x for x in input().split(',')]

#call display() and pass the list od strings
displayString(strListValue)


    
    