#A python program to implement multiple inheritance using base class
#Multiple Inheritance
class Father:
    def height(self):
        print('Height is 6.0 foot')
class Mother:
    def color(self):
        print('Color is brown')

class Child(Father, Mother):
    pass

c = Child()
print('Child\'s inherited qualites ::')

c.color()
c.height()