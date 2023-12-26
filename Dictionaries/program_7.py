#A python program  to find the number of occurrences of each letter in a string using dictionary
#Find how many times each letter is repeated in a string
#Take a string with some letters
strValue ="Moon"

#take a empty string
dictValue = {}

#store into dict each letter as key and its
#numbers of occurances as value 
for x in strValue:
    dictValue[x] = dictValue.get(x, 0) + 1

#display key and value pairs:
for k, v in dictValue.items():
    print('Key = {}\t, Its Occurrences = {}'.format(k, v))



