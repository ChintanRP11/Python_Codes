'''
The findall() function returns a list containing all matches.
The list contains the matches in the order they are found.
If no matches are found, an empty list is returned
'''
import re

str1 = 'The rain in Spain'

res = re.findall('ai',str1)
for i in res:
    print(i)
