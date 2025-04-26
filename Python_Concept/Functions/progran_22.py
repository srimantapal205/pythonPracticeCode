#A python program to access global varible inside a function and modify it
a = 1 #This is Global varible
def modGVFun():
    global a #this is global varible
    print( 'a == :: ', a, ' # Access global varible using global keyword' )
    a = 2 # modify the global varible value
    print('a == :: ', a, ' # Modify the global varible value')

modGVFun()
print('a == :: ',a, ': Present global varible value outside the function' )