#A python program to store the message released by any exception in to a log file.
#logging all error messages from a program
import logging 

#store logging message into log.txt file
logging.basicConfig(filename='log.txt', level=logging.ERROR)

try:
    a = int(input('Enter a number :: '))
    b = int(input('Enter another number ::  '))
    c = a/b

except Exception as e:
    logging.exception(e)

else:
    print('The result of division :: ', c)
    
