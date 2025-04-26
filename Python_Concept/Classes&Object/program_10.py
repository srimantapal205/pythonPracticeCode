#A python program to create a Bank class where diposit and withdrawals can be handle by using instance  mehthods
#A class handle diposit and withdrawl in a bank
import sys
class Bank:
    '''Bank related transations'''
    #to initialize name and balance instance vars
    def __init__(self, name, balance = 0.0) -> None:
        self.name = name
        self.balnce = balance
    
    #to add diposit amount to balance
    def deposit(self, amount):
        self.balnce +=amount
        return self.balnce
    
    #to deduct withdrawl amount from balance
    def withdraw(self, amount):
        if amount > self.balnce:
            print('Balance amount is less, so no withdrawl.')
        else:
            self.balnce -= amount
        return self.balnce
    
#Using the bank class 
#Create an account with the given name and balance 0.0
name = input('Bank Name :: ')
b= Bank(name)

#repeat continusly till choice is  'e' or 'E'
while(True):
    print('d - Deposit, \t w - Withdrawl, \t e - Exit')
    choice = input('Your choice :: ')
    
    if choice == 'e' or choice == 'E':
        sys.exit()
    
    #Amount for deposit or withdraw
    amt =int(input('Enter your amount :: '))
    
    #do the transction 
    if choice == 'd' or choice == 'D':
        print('Balance after diposit :: ', b.deposit(amt))
    elif choice == 'w' or choice == 'W':
        print('Balance after withdrawl :: ', b.withdraw(amt))
    
    
    