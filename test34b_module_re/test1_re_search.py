'''
The search() function searches the string for a match, and returns a Match object if there is a match.
If there is more than one match, only the first occurrence of the match will be returned
If no matches are found, the value None is returned
'''

import re

str1 = 'The rain in Spain'

res = re.search('ai',str1)
print('first ai is located at position : ',res.start())

res2 = re.search('\s', str1)
print('first whitespace is located at position : ',res2.start())
