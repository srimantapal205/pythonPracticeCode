#A python program to create a list with employee data and then retrive a particuler employee data
#retrive employee details from a list
emp = [] #take an empty list
#Accept input into n
n= int(input('How many employee? '))

#Repat for n times
for i in range(n):
    
    print('Entet Id :: ', end='')
    emp.append(int(input()))
    
    print('Enter name :: ', end='')
    emp.append(input())
    
    print('Enter salary :: ', end='')
    emp.append(float(input()))
    
print('The list is crrated with employee data')
print(emp)
print()

id= int(input('Enter employee id :: '))
#Dispaly employee details upon taking id.
for i in range(len(emp)):
    if id == emp[i]:
        print('ID == :: {:d}, Name == :: {:s}, Salary == :: {:.2f}'.format(emp[i], emp[i+1], emp[i+2]))
        break
        


