#A python program to understand the keyword arguments of a function.
def grocery(item, price):
    '''To display the given arguments'''
    print('Item = %s '%item)
    print('Price  = %.2f '%price)

#Call the grocery() and pass 2 argument
grocery(item='Suger', price=50.75) #Keyword argument
grocery(price=150.75, item='Oil' )# Keyword arguments 