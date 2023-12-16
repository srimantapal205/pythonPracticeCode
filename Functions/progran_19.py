#A python program to show varible length argument and it's use
def add(farg, *args):
    '''To add given numbers'''
    print('Formal Argumnt :: ', farg)
    sum=0
    for i in args:
        sum+=i
        print('Sum all numbers :: ', (farg + sum))

#Call add and pass arguments
add(10,20)
add(10,20,30,40,50,60)

