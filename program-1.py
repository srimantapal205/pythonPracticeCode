#Fundamental Data Type

# int 
# float
# bool
# str
# list
# tuple
# set
# dict
#Class  Costom Type

#Specialized Data Type

print(2+6)
print(2-6)
print(2*6)
print(2/6)

print(type(2+6))
print(type(2-6))
print(type(2*6))
print(type(2/6))

print(2 ** 3) #Power of number
print(5 // 4) # Division with int value
print(5 % 4) #Modulo

# Math Functions

print(round(3.1))
print(round(3.9))
print(abs(-30))

# Operato Precedence

print((10*10) + 2**2)

print(bin(5))
print(int('0b101',2))

# Varible in diffrent case
test_case = 1,
_test_case = 2
testCase = 3

# constants
PI =3.14

#String

print(type('Hi'))
username = 'superuser'
password = 'supuruser1234'

long_string = '''
    WOW
    0 0
    ---
'''
print(long_string)

str1 = 'Hello'
str2 = 'World'

fullString = str1 + ' ' + str2

print(fullString)


#Built-in functions & Methods

quote =  'to be or not to be'
print(len(quote)) 
print(quote.capitalize())
print(quote.upper())
print(quote.replace('be', 'me'))

#Booleans

# bool can be True or False
print(bool(1))
print(bool(0))

fb_name = "Sri"
fb_age = 50
fb_rel_status = "Single"
fb_rel_status = 'it\'s complicated'

print(fb_rel_status)

# birth_year= input('What year ware you born: ')
# get_current_age = 2023 - int(birth_year)
# print(f'Your Age is :  {get_current_age}')

#Create a python program  for password checker
 
#input('JayJay')
#input('secret')

#print(f'User Name: {}  and you password {*******} is {6} character')

# username2 = 'JayJay'
# passw = 'secret'

username2 = input('Enter user name: ')
passw = input('Enter your password: ')

getPassLenth = len(passw)
hiddenPass = '*' * getPassLenth

print(f'The User Name Is : {username2} \nThe Password is : {hiddenPass} & Password length is {getPassLenth}')




