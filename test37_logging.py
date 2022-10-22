# It is used for creating logs
import logging

#logging.basicConfig(filename='mylog.log',level=logging.DEBUG)
#logging.critical('Critical')
#logging.error('Error')
#logging.warning('Warning')
#logging.info('Info')
#logging.debug('Debug')

logging.basicConfig(filename='mylog.log',level=logging.DEBUG)
x,y = input().split()
try:
	logging.info("division in progress, try block")
	c = int(x)/int(y)
	logging.info("printing in progress, try block")
	print(c)
except ZeroDivisionError:
	logging.error("divide by zero error")
	print("Divide by zero error")
finally:
	print("finally block run.")