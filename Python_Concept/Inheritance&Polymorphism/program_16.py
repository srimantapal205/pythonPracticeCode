#A python program to call a method that does not apper the object passed to the method
#duck typing example - v2

#dog class contain bark method
class Dog:
    def bark(self):
        print('Bow, wow')

#Duck class contains talk() method
class Duck:
    def talk(self):
        print('Quack Quack')

#Human class call contains talk() method
class Human:
    def talk(self):
        print('Hello hi!')

#this method accept an object and talk() method
def call_talk(obj):
    obj.talk()

#call call_talk() method and pass an object
#depending on type of object, talk() is exexuted 
x = Duck()
call_talk(x)

x = Human()
call_talk(x)

x = Dog()
call_talk(x) #error occurs in this call

        
        
        
        