#Python program to randomly access a record from a binary file
#reading city name  based on record number

#take record length 20 character
reclen = 20
#open the file in bunary node for reading
with open('cites.bin', 'rb') as f:
    n = int(input('Enter record number ::'))
    #move file pointer to the end of n-1 th record 
    f.seek(reclen * (n-1))
    #get the n th record with 20 chars
    strTxt = f.read(reclen)
    #convert the byte string into ordinary string
    print(strTxt.decode())
    
    
    