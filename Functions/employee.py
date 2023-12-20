#Save this code as employee.py

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