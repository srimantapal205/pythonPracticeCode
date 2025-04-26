#A python program to prove that only one class constractor is vailable to sub class in multiple inheritance
#When super class hhave constractor
class A(object):
    def __init__(self):
        self.a = 'a'
        print(self.a)

class B(object):
    def __init__(self):
        self.b ='b'
        print(self.b)

class C(A,B):
    def __init__(self):
        self.c = 'c'
        print(self.c)
        super().__init__()

#access the super class instance vars from c
o = C()
