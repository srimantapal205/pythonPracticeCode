# Apyhon program using the special __name__ varible

#python program to dispaly a message . save this as one.py

def display():
    print('Hello python!')

if __name__=='__maun__':
    display() #call display function
    print('this code is run as program')
else:
    print('This code is run as a module')