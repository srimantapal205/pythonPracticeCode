#Python program to overload greater than(>) operator to make it act on class object.
#overloading > operator
class Ramayan:
    def __init__(self, pages):
        self.pages = pages
    
    def __gt__(self, other):
        return self.pages > other.pages

class Mahabharat:
    def __init__(self, pages):
        self.pages = pages

b1 = Ramayan(1000)
b2 = Mahabharat(1500)

if(b1>b2):
    print('Ramayan has more pages')
else:
    print('Mahabharat has more pages')