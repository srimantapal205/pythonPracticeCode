#Apython program to handle IOError produced by open() function
#example of IOError
#accept a filename
try:
    fname = input("Enter file name :: ")
    f = open(fname, 'r')
except IOError:
    print('File not found :: ', fname)
else:
    n = len(f.readlines())
    print(fname,'has', n, 'lines')
    f.close