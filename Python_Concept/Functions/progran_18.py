#A python program to understand the  use of default arguments in a function
#Default arguments pass
def grocery(item, price=50.50):
    '''To display the given arguments'''
    print('Item == %s' %item)
    print('Price == %.2f' %price)
    
#Call grocery() and pass arguments
grocery(item='Suger', price=75.50) #pass 2 arguments    
grocery(item='Suger') #default value for price is used   
