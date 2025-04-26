#Polymorphism
#Duck typing Philosophy of python

#Apython program to invoke a method on an object without knowing the type of object.
#duck typing example

#Duck class contains talk() methods
class Duck:
    def talk(self):
        print('Quack Quack!')

#Human class contains talk() method
class Human:
    def talk(self):
        print('Hello, hi !')

#this method accept an object and calls talk() method 
def call_talk(obj):
    obj.talk()

#call call_talk() method and pass an object
#depending on type of object, talk() method is executed
x = Duck()
call_talk(x)

x = Human()
call_talk(x)


