#A python program to create our own exception and raise it when needed.
#Create our won class as a sub class to Exception class:
class MyException(Exception):
    def __init__(self, args):
        self.msg = args
        
#Write code where exception may raise
#to raise the exception, use raise statemen

def check(dict):
    for k, v in dict.items():
        print('Name = {:15s} Banance: {:10.2f}'.format(k,v))
        if(v <= 2000):
            raise MyException('Balance amount is less in the account of ' +k)

#our own exception is handel using try and except blocks
bank = {'Raj':5000.00, 'Vani':8900.52, 'Ajay':1500.21}
try:
    check(bank)
except MyException as me:
    print(me)