# using command line arg to find the even number and print the sum of the even number
import sys
n = len(sys.argv)
print("Number of command line arg: ", n)
largs = sys.argv
print("The args are: ", largs)

#Read the command line arguments except the program name
args = sys.argv[1:]
print(args)

sum =0
#find sum of even number
for a in args:
    x = int(a)
    if x%2==0:
        print(x)
        sum+=x

print("Sum of even : ", sum)
