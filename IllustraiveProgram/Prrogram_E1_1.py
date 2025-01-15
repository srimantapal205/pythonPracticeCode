'''
Write a program to prompt a user to enter his/her name and mailing address and display the entered information on the screen.
'''

name = input("Enter you Name : ")
address1 = input('Enter address line 1 : ')
address2 = input('Enter address line 2 : ')
address3 = input('Enter address line 3 : ')
city = input('Enter city name: ')
state = input('Enter State name: ')
pin = input('Enter Pin :')

print(f' Name: {name} \n Address: {address1} \n\t {address2}\n\t {address3} \n City : {city}\n State : {state}, {pin}')


