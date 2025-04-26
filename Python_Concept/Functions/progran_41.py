#A python program to create a generator that returns a sequnce of numbers from x to y
#Generator that returns sequence from x to y

def cretGen(x, y):
    while x<=y:
        yield x
        x+=1
#Fill generator object with 5 to 10
g = cretGen(5, 10)
#display all numbers ::
for i in g:
    print(i, end=" ")


