'''
Exceptions are Runtime Errors
It will cause:
	abnormal termination of program
	unfriendly information to the end user
	improrper shutdown of the resources

'''

# #try except is use for hide error and print something in place of error
import sys
# #
# randomlist = ['a', 0, 'v', 2]
#
# for entry in randomlist:
#     try:
#         print('The entry is :',entry)
#         r = 1/int(entry)
#         break
#     except:
#         print(sys.exc_info()[0], 'occured')
#         print('next entry...')
#         print()
# print('reciprocal of ',entry,'is',r)



#try finally  --> it is used when certain actions must be performed in any condition (if error occured or not)
# like file closing, database connection closing, etc...
# try:
#     fh = open('fileops3','r')
#     fh.write('THis is write from try')
# except:
#     print(sys.exc_info()[0], 'Error : cant find file or write data')
# finally:
#     fh.close()


#user - defined exception
#create some class with <errorname> which has to be raised
#after that we can raise error in certain cases
#and then we expect <errornamae> with print()

class HigherValue(Exception):
    pass
class LowerValue(Exception):
    pass
import random
val = random.randrange(0,41)
print(val)
try:
    if val < 20:
        raise LowerValue
    elif val > 20:
        raise HigherValue
    else:
        print('Perfect value')
except HigherValue:
    print('value is too high')
except LowerValue:
    print('value is too low')
