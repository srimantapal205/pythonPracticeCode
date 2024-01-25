#A python program to handle the zeroDeivisionError Example
#An exception handling example
try:
    f= open("divisionFile.txt", "w")
    a, b = [int(x) for x in input("Enter two number:: ").split()]
    c = a/b
    f.write("Write %d in myfile" %c)

except ZeroDivisionError:
    print("Division by zero happend")
    print("Please do not enter 0 in input")

finally:
    f.close()
    print("File Closed")