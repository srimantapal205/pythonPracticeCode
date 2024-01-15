#A python program to develop an interface that connect to any database 
#abastract class work like an interface
from abc import *
class MyClass(ABC):
    @abstractmethod
    def connect(self):
        pass
    def disconnect(self):
        pass

#this is sub class 
class oracle(MyClass):
    def connect(self):
        print('Connecting to oracle database.....')
    
    def disconnect(self):
        print('Disconnect to oracle database.....')

#this is another subclass
class SyBase(MyClass):
    def connect(self):
        print('Connecting to Sybase.....')
    def disconnect(self):
        print('Disconnect to Sybase.....')

class Database:
    #accept Database name
    dbName = input('Enter database name :: ')
    
    #convert the string to global class
    className = globals()[dbName]
    
    #Create an new object to that class
    x = className()
    
    #call the connect() and disconnect() method
    x.connect()
    x.disconnect()