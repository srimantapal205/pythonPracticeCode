#A python program to understand keyword varible argument
def dispaly(frag, **kwargs):
    '''To display given values'''
    print('Formal arguments :: ', frag)
    
    for x, y in kwargs.items(): #item() will give pairs of items
        print('key = {} , value = {}'.format(x,y))

#call function display()
#Pass 1 formal arguments and 2 keyword arguments 
dispaly(5, rno=10)
print()
#Pass 1 formal arguments and 4 keyword argument
dispaly(6, rno=11, name='Prakash')
    
    