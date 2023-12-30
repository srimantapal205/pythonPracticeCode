#Class Methods
#A pthon program to use class method to handle the common features of all the instance of Bird class
#Understanding class methods (@classmethod)
class Birds:
    #this is class varible
    wings = 2
    
    #this is class method
    @classmethod
    def fly(cls, name):
        print('{} flies {} wings'.format(name, cls.wings))
    
#display play information
Birds.fly('Sparrow')
Birds.fly('Pigeon')