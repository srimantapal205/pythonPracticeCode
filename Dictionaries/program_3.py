#A python program to create dictionay and find the sum of the value
#Enter the dictionary entries from keyboard
dictValue = eval(input('Enter elements in {} :: ')) #{'A':10,'B':20, 'Anil':30}

#find the sum of values
s = sum(dictValue.values())

print('Some of values in the dictionary :: ',s) #Display sum   60
