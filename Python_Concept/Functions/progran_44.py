#A python program that uses the function of employee module and calculate gross and neet salary of an employee
#using employee module to calculate gross and net salary of an employee
from employee import*

#calculate gross salary of employee by taking basic
basic = float(input('Enter basic salary :: '))

#calculate gross salary of employee by taking basic 
gross = basic+da(basic)+hra(basic)
print('Your gross salary :: {:10.2f}'.format(gross))

#Calculate net salary
net = gross - pf(basic) - itax(gross)
print('Your net salary is :: {:10.2f}'.format(net))