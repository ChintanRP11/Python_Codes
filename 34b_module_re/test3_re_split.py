# The split() function returns a list where the string has been split at each match
import re

str = 'The rain in spain'
x = re.split("\s", str)
print(x)

x1 = re.split('i', str)
print(x1)

x3 = re.split("\s", str, 1)     #third argument is number of occurrence or iterations
x4 = re.split("\s", str, 2)
print(x3)
print(x4)