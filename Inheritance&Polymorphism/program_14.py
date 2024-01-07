#A python program to understand the order of execution of methods in several base class accroding to MRO.
#Multiple inheritance with several classes

class A(object):
    def method(self):
        print('X class method')
        super().method()

class B(object):
    def method(self):
        print('B class method')
        super().method()

class C(object):
    def method(self):
        print('C class method')

class X(A, B):
    def metthod(self):
        print('X class method')
        super().method()

class Y(B, C):
    def method(self):
        print('Y class method')
        super().method()

class P(X, Y, C):
    def method(self):
        print('P class method')
        super().method()

p = P()
p.method()
print(P.mro())
# [<class '__main__.P'>, 
# <class '__main__.X'>, 
# <class '__main__.A'>, 
# <class '__main__.Y'>, 
# <class '__main__.B'>, 
# <class '__main__.C'>, 
# <class 'object'>]