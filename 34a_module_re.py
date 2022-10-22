# re module is used for check regular expressions in strings

# metacharacters
#   []	    A set of characters	        "[a-m]"
#   \	    Signals a special sequence (can also be used to escape special characters)	        "\d"
#   .	    Any character (except newline character)	        "he..o"
#   ^	    Starts with	        "^hello"
#   $	    Ends with	        "world$"
#   *	    Zero or more occurrences	        "aix*"
#   +	    One or more occurrences	        "aix+"
#   {}	    Exactly the specified number of occurrences	        "al{2}"
#   |	    Either or	        "falls|stays"
#   ()	    Capture and group

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

'''
The search() function searches the string for a match, and returns a Match object if there is a match.
If there is more than one match, only the first occurrence of the match will be returned
If no matches are found, the value None is returned

The findall() function returns a list containing all matches.
The list contains the matches in the order they are found.
If no matches are found, an empty list is returned

The split() function returns a list where the string has been split at each match

The sub() function replaces the matches with the text of your choice

The span() returns a tuple containing the start-, and end positions of the match.

The string returns the string passed into the function

The group() returns the part of the string where there was a match
'''

import re
emailadd =input("Enter email : ")

vld = "(\w+)@(\w+)\.(com)"

r2 = re.match(vld,emailadd)
print(r2.group(1))

if re.match(vld,emailadd):
    print('Valid')
else:
    print("Invalid")
