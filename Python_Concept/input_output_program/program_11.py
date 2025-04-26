#Accepting 3 number separated by space.
var_1, var_2, var_3 = [int(x) for x in input("Enter three numbers: ").split(' ')]

# Calculating and printing the sum of the three numbers
print("Sum =", var_1 + var_2 + var_3)
