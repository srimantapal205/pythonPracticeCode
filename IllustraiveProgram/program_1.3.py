# R-1.3 Write a short Python function, minmax (data), that takes a sequence of three or more numbers, and returns the smallest and largest numbers, in the form of a tuple of length o Do not use the built-in functions min or max in implementing your solution.

def minmax(data):
    smallest = largest = data[0]

    for num in data[1:]:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    return (smallest, largest)


print(minmax([3, 6, 9, 11, 5]))
print(minmax([8, 4, 1, 2, 9]))
print(minmax([1, 2, 3, 15, 5]))
