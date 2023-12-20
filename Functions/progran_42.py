#A generator that returns characters from A to C 
def strGen():
    yield 'A'
    yield 'B'
    yield 'C'
#Call the generator function from A to C
g = strGen()
print(next(g)) #Display A
print(next(g)) #Display A
print(next(g)) #Display A
print(next(g)) #Error