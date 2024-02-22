#A python program to handle the multiple exception
#example for two exceptions
#A function to find total and average of list elements
def avg(list):
    tot = 0
    for x in list:
        tot += x
    avg = tot / len(list)
    return tot, avg

# #call the avg() and pass the list
try:
    itm = input('Enter list of item :: ').split(',')
    lst = [int(num) for num in itm]
    t, a = avg(lst)
    print('Total: {}, Average :: {}'.format(t,a))
except TypeError:
    print('Type Error, Please provide numbers!  ')
except ValueError:
     print("Please enter valid numbers separated by commas.")
except ZeroDivisionError:
    print('ZeroDivisionError : Please do not give empty list. ')


