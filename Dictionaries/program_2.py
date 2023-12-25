#A python program to retrive key an key-value pairs from a dictoniary

#Dictionary methods
#Create a dictionart with employee details
dictValue = {'id':200 , 'name':'Chandra', 'salary':9080.50}

#print entire dictionary 
print(dictValue)

#display only keys
print('Key in dict :: == ', dictValue.keys()) # dict_keys(['id', 'name', 'salary'])

#display the key-values
print('Values in dict :: == ', dictValue.values()) #dict_values([200, 'Chandra', 9080.5])

#display both key and value pairs as tuples
print('Item in dict :: == ', dictValue.items()) # dict_items([('id', 200), ('name', 'Chandra'), ('salary', 9080.5)])

