#A lambda that returns even numbers from the list
#A lambda function that returns even numbers from a list
lst = [16,14,12,13,19,91,61,56,64,25,75,85,88,99,90,12,17,61,85]
evenLst = list(filter(lambda x: (x%2 == 0), lst))
print(evenLst)