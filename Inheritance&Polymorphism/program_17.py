#A python program to check the object tpe to know whether the method exit in the object or not.
#Strong type example 
#Dog class contains break() method
class Dog:
    def bark(self):
        print('Bow , wow')
        
#Duck class contains talk() method
class Duck:
    def talk(self):
        print('Quack, Quack !')

#Human class contains talk() method
class Human:
    def talk(self):
        print('Hello, Hi !')

#this method accept an object and calls talk() method
def call_talk(obj):
    if hasattr(obj, 'talk'):
        obj.talk()
    elif hasattr(obj, 'bark'):
        obj.bark()
    else:
        print('Worng object passed.......')
  
#call call_talk() method and pass an object
#depending on type of object talk, talk() method is executed
x = Duck()
call_talk(x)

x = Human()
call_talk(x)

x = Dog()
call_talk(x)      





