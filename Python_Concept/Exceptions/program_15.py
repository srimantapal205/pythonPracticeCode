#A ppython program that create a log file with errors and critical messages.
#understanding logging of error message.
import logging

#store message in mylog.text file
#store only the messages with level equal to or more than that of ERROR
logging.basicConfig(filename='errorlogs.txt', level=logging.ERROR)

#these message are stored in to the file.
logging.error('There is an error in the program.')
logging.critical('There is a problem in the design.')

#but these are not stored
logging.warning('The project is going slow !')
logging.info('You are junior programmer !')
logging.debug('Line no. 10 contains syntax error..')