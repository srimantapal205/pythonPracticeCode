#Create a python program  to calculate the gross salary and net salary of a employee

#to calculate dearness allowance
def da(basic):
    '''da is 80% of basic salary'''
    da = basic*80/100
    return da 

#to calculate the house rent allowance 
def hra(basic):
    '''hra is 15% of basic salary'''
    hra = basic*15/100
    return hra

#to calculate of provident fund amount
def pf(basic):
    '''pf is 12% of basic salary'''
    pf = basic*12/100
    return pf

#to calculate the income tax payable by employee
def itax(gross):
    '''tax is calculate a 10% on gross '''
    tax =gross*0.1
    return tax

#This is the mai program 
#calculate te grosse salary of employee by taking basic
basic = float(input('Enter basic Salary :: '))

#Calculate gross salary
gross = basic+da(basic)+hra(basic)
#calculate the net salary
net = gross - pf(basic) - itax(gross)
pf = pf(basic)
taxAmount = itax(gross)
print('Your gross salary :: {:10.2f}'.format(gross))
print('Provident fund amount :: {:10.2f}'.format(pf))
print('Provident fund amount :: {:10.2f}'.format(taxAmount))
print('The net salary is :: {:10.2f}'.format(net))

