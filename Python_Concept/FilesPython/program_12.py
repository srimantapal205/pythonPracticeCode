#A python program to pickle Emp class object
#pickle - store Emp class object into emp.dat file
import program_11 as Emp
import pickle
 
#Open emp.dat file as a binary file for writing
f = open('emp.dat', 'wb')
n = int(input('How many employes?'))

for i in range(n):
    emp_id = input('Enter Emp Id :: ')
    empName = input('Enter Emp Name :: ')
    emp_sal = input('Enter Emp Salary :: ')

    #Create Emp class object.
    e = Emp.Emp(emp_id,empName,emp_sal)

    #store the object into the file f
    pickle.dump(e, f)

#close file
f.close()