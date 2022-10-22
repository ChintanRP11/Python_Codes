# The sub() function replaces the matches with the text of your choice

import re

str = "The rain in Spain"
x = re.sub("\s", "9", str)      #replace whitespace to 9
print(x)

x1 = re.sub("\s", "9", str, 2)      #replace whitespace to 9 only 2 times
print(x1)