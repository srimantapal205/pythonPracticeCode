#A python program using filter()  to filter out the even number from the list
#filter() function that returns even numbers from a list
def is_even(x):
    if x%2 == 0:
        return True
    else:
        return False

# List of numbers
lst = [10,50,21,89,75,65,32,12,11,23,29,71,46,55]

#call filter() with is_even and lst

lst1 = list(filter(is_even, lst))

print(lst1)


