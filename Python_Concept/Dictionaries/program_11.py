#A pyton function to accept a dictionary and display its element
#A function that take a dictionary as a parameter 

def fun(dictionary):
    for i, j in dictionary.items():
        print(i, ' -------- ', j)

#take a dictionary
d = {'a':'Apple', 'b':'Book', 'c':'Cook'}

#Call the function and pass the dictionary
fun(d)
