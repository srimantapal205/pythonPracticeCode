import sys
n = len(sys.argv) # n is number of arguments
args = sys.argv #args list contains arguments
print("No. of command line argument: ", n)
print("The arg are: ", args)
# Convert args into integers and add them
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
sum = num1 + num2

print("Sum:", sum)
