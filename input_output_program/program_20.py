#to find the squre of given number.
import argparse

#Create a AgrumentParser class object
parser = argparse.ArgumentParser(description='This program display the squre value of given number')

#add one argument with the num and type as integer
parser.add_argument("num", type=int, help="Please input integer type value: ")

#Retrive the arguments passed to the program 
args =parser.parse_args()

#Find the squre of the argument passed
result = args.num**2
print("Squre value = ", result)

#List of error
'''
If user press float number:
usage: program_20.py [-h] num
program_20.py: error: argument num: invalid int value: '5.5'

'''

'''
If user enter multiple number:
usage: program_20.py [-h] num
program_20.py: error: unrecognized arguments: 5

'''

'''
If user does not enter any input 
usage: program_20.py [-h] num
program_20.py: error: the following arguments are required: num
'''

'''
If the user got any confused regarding how to use the this program.

usage: program_20.py [-h] num
This program display the squre value of given number
positional arguments:
  num         Please input integer type value:

options:
  -h, --help  show this help message and exit

'''