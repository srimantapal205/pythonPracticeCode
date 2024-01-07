#A python program to access all the instance varibles of both the base class in multiple inheritance.
#when super classes have constructors  -v2
class A(object):
    def __init__(self):
        self.a = 'a'
        print(self.a)
        super().__init__()

class B(object):
    def __init__(self):
        self.b = 'b'
        print(self.b)
        super().__init__()

class C(A,B):
    def __init__(self):
        self.c = 'c'
        print(self.c)
        super().__init__()
        

x = C()
