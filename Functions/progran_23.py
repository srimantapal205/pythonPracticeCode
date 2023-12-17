#A python program to get a copy of global varible into a function and work with it.
#Same name for global and local varible
a = 1 #this is global varible  
def smGLvarFun():
    a = 2 #this is local varible
    x= globals()['a'] #Get global vae into x
    print('Global var a = :: ', x)
    print('Local varible a = :: ', a)

smGLvarFun()
print('Global var a == :: ',a)


