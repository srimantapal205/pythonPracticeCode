#A python program to unpickle Emp class objects
import program_11 as emp
import pickle

#Open the file to reade object
f = open('emp.dat', 'rb')

print('Employees details :: ')
while True:
    try:
        #read object from file f
        obj = pickle.load(f)
        #display the contents of employee obj
        obj.display()

    except EOFError:
        print('End of file reached:: ')
        break

#close file
f.close()
         