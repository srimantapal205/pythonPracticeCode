#A Python program to use 'with' to open a file and read data from it
#Using with statement to open a file and read the data
with open('sample.txt', 'r') as f:
#    x = f.read()
#    print(x)
   for line in f:
        print(line)
    