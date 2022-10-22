'''
it is used when type command for running python file
user has to give arguments with command
'''

import sys
print(len(sys.argv))
print(sys.argv)

a = sys.argv[1]
print("Entered value :", a)
