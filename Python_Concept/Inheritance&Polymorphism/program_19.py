#Apython program to use addition operator to add the content of two object.
#using + operator on object
class BookX:
    def __init__(self, pages):
        self.pages =pages

class BookY:
    def __init__(self, pages):
        self.pages = pages

b1 = BookX(100)
b2 = BookY(150)

print(b1 + b2)

        
    
        
#  print(b1 + b2)
#TypeError: unsupported operand type(s) for +: 'BookX' and 'BookY'