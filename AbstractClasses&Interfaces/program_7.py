#A python program which contain a Printer interface and it's hsub class to send text to any printer
#An interface to send text to any printer

from abc import *

#create an interface
class Printer(ABC):
    @abstractmethod
    def printit(self, text):
        pass
    @abstractmethod
    def disconnect(self):
        pass

#this is sub class for IBM Printer
class IBM(Printer):
    def printit(self, text):
        print(text)
    def disconnect(self):
        print('Printing completed on IBM printer')

#this is sub class for  EPson Printer
class Epson(Printer):
    def printit(self, text):
        print(text)
    def disconnect(self):
        print('Printing completed on Epson printer')
    
class UsePrinter:
    # Accept printer as a string from the configuration file
    with open("config.txt","r") as file:
        printer_class_name = file.readline().strip()
        
        # Convert the string into a class name
        printer_class = globals()[printer_class_name]
        
        # Create an object of that class
        printer_object = printer_class()
        
        # Call the printit() and disconnect() methods
        printer_object.printit("Hello, this is a test text.")
        printer_object.disconnect()



     