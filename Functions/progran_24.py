#A python program to accept a group of numbers and find their total average.
#a function to find total and avarage 
def calculate(lstValue):
    '''To find the total and avarage'''
    n = len(lstValue)
    total_sum = 0
    for i in lstValue:
        print(i)
        total_sum += i
    avgValue = total_sum / n
    return total_sum, avgValue

#Take group of interger from keyboard
lst = [int(x) for x in input("Enter a group of numbers separated by space: ").split()]

# call calculate() and pass the list
x, y = calculate(lst)
print('Total Sum :: ', x) 
print('Avarage value :: ', y) 


