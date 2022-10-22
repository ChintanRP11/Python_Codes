'''
sys :
This module provides access to some variables which are controlled and used by interpreter
It also provides access to functions that interact with interpreter

os :
it used to work with operating system, it can run os commands
'''
import sys

# sys.argv                  # command line argument
print(sys.winver)           # it gives version number
print(sys.flags)            # it shows status of command line flags
print(sys.prefix)           # it returns path of python environment
#print(sys.exit())          # tells python interpreter to quit

import os

print(os.name)
print(os.environ)               # returns environment variables of system
print(os.getlogin())            # user logon name
print(os.getpid())              # process id of given function
print(os.getppid())             # parent's process id

# commands using python
# print(os.getcwd())
# print(os.chdir('D:\Python'))
# print(os.getcwd())
# print(os.mkdir('pytest'))
# print(os.rmdir('pytest'))
# for i in os.walk('D:\python\py code\Tests'):           # returns all files and folders in it
#    print(i)

import os.path

print(os.path.abspath('test29_module_prop.py'))             # returns absolute path
print(os.path.normpath('Tests\\test29_module_prop.py'))     # normal path name
print(os.path.split('D:\python\py code\Tests\\test29_module_prop.py'))      # in o/p first part is dir. name and another is file name
print(os.path.exists('D:\python\py code\Testings'))         # check file/dir is exists or not
print(os.path.isdir('D:\python\py code\Tests'))             # check it is directory or not
print(os.walk('D:\python\py code\Tests'))
for i in os.walk('D:\python\py code\Tests'):                # shows all files and folders inside given path
    print(i)