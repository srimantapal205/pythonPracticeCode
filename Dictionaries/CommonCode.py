dic = [{'id':1, 'name':'x'}, {'id':2, 'name':'y'}]
print(type(dic))

dictValue = {'id':200 , 'name':'Chandra', 'salary':9080.50}
n = len(dictValue)
print(n)
#modify a single key value
dictValue['salary']= 10500.75
print(dictValue)

#insert a new key value 
dictValue['dept']='Financ'
print(dictValue)

#delete a key-value pair
del dictValue['id']
print(dictValue)

#To test the key is available in dictionary or not
print('dept' in dictValue) #True
print('gender' in dictValue) #False


