'''
operators used for string formatting
%c = character
%i = signed integer
%u = unsigned int
%o = octal int
%x = hex int with lowercase
%e = exponential notation with lowercase 'e'
%f = floating point number
%g = shorter of %f and %e
'''

str1 = 'First'
str2 = 'welcome to python and welcome to python again'
str3 = 'Third'
str4 = 'fourth'

print(str1[1:3])
print(str1[::-1])                            #--> reversing string
#str1[2] = 'a'                              #-->it throws an error

print(str4.capitalize())                    #--> capitalizes first letter of string
print(str2.count('to', 0, len(str2)))       #-->counting string 'to' how many times happens in str2. 1st param is string, 2nd is starting position, 3rd is ending position

print(max(str3))                            #--> as per ASCII value
print(min(str3))                            #--> as per ASCII value

print(str2)
print(str2.replace('to', 'TO', 1))          #--> it replace string with given string and third param is for how many to's will be channged
print(str2.replace('to', 'TO', 2))

print(str4.upper())                         #--> converts string to uppercase
print(str4.lower())                         #--> converts string to lowercase

print(str2)
print(str2.index('p'))                      #--> find string's position
print(str2.index('p', 12))                  #--> find string's position after given start index
#print(str2.index('p', 12, 23))             #--> find string between given positions, here it throws an error because string is not found

print(str2.find('p'))                       #--> find position of 'p'
print(str2.find('z'))                       #--> it returns -1 because of z is not in string it not throws error like .index()
print(str2.find('p', 12))
#str.index() used when substring/character is in string otherwise use str.find()it returns -1 when substring/character is not in string

print(str3+str3)