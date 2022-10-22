# special sequences
# \A	    Returns a match if the specified characters are at the beginning of the string	"\AThe"
# \b	    Returns a match where the specified characters are at the beginning or at the end of a word	r"\bain" r"ain\b"
# \B	    Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word	r"\Bain"  r"ain\B"
# \d	    Returns a match where the string contains digits (numbers from 0-9)	"\d"
# \D	    Returns a match where the string DOES NOT contain digits	"\D"
# \s	    Returns a match where the string contains a white space character	"\s"
# \S	    Returns a match where the string DOES NOT contain a white space character	"\S"
# \w	    Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"
# \W	    Returns a match where the string DOES NOT contain any word characters	"\W"
# \Z	    Returns a match if the specified characters are at the end of the string	"Spain\Z"

import re

str2 = 'This is Python 3.7'
str1 = 'The rain in spain'
res = re.findall('\AThe', str1)
res1 = re.findall('\Ain', str1)
print("res : ",res)
print("res0 : ",res1)

res21 = re.search(r"\bThe", str1)
res51 = re.search(r"\BThe", str1)
print("res21 : ",res21)
print("res51 : ",res51)

# here search is used because of start and end
res2 = re.search(r"ain\b", str1)
res5 = re.search(r"ain\B", str1)
print("res2 : ",res2)
print("res5 : ",res5)

res3 = re.findall('\d', str2)
res4 = re.findall('\D', str2)
print("res3 : ",res3)
print("res4 : ",res4)

res6 = re.findall('spain\Z', str1)
print('res6 : ',res6)

res61 = re.findall('\s', str1)
print('res61 : ',res61)
res62 = re.findall('\S', str1)
print('res62 : ',res62)
