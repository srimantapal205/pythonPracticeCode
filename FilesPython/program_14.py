#A python program to create a bynary file  file and store a few record
#create cities.bin file with cites name
#take the size as 20 bytes
reclen = 20

#open the file in wb mode as binary file
with open('cites.bin', 'wb') as f:
    #write data in to the file
    n = int(input('How many entrise ? :: '))
    
    for i in range(n):
        city = input('Enter city name :: ')
        #find the length of the city
        ln = len(city)
        
        #increase city name to 20 chars
        #by adding remaing space
        city = city + (reclen - ln)*' '
        #convert city name in to byte string
        city = city.encode()
        #write the city name into the filr
        f.write(city)

