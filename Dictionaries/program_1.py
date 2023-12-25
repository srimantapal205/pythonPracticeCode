#Apython program to create a dictonary with employee details and retrive the value upon given key 
#Create a dictonary  with key value pairs
'''
Create a dictionary with  employee detail . 
here 'name' is key and 'Chandra' is value
'Id' is a key and 200 is its value
'Salary is key and 9080.50is its value

'''
dictValue = {'id':200 , 'name':'Chandra', 'salary':9080.50}
print(type(dictValue))

#access value by given key::
print('Name of the Employee :: ',dictValue['name'])
print('Id of the Employee :: ',dictValue['id'])
print('Salary of the Employee :: ',dictValue['salary'])
