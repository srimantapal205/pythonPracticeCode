# A pyhon program to search for city in the file and display the record number that contains the  city name.
#Search the city name in the file

import os
#take record length as 20 characters
reclen = 20 

#find size of the file 
size = os.path.getsize('cites.bin')
print('Size of the file : {} byts'.format(size))

#find the number of records in the file
n = int(size/reclen)
print('No. of record  = {}'.format(n))

#open the file in binary mode for reading 
with open('cites.bin', 'rb') as f:
    cityName = input('Enter city name :: ')
    #convert name in to binary string 
    cityName = cityName.encode()
    #position represent the position of file pointer 
    position = 0
    
    #found becomes true if city is found in the file 
    found = False
    
    #repeat for n record in the file
    for i in range(n):
        #place the file pointer at position
        f.seek(position)
        #read 20 characters
        cstr = f.read(20)
        #if found
        if cityName in cstr:
            print('Found at record no : ', (i+1))
            found = True
        #go to the next record
        position += reclen

    if not found:
        print('City not found')

