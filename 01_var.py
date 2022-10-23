'''
Data Types in Python
    -immutable data types (Items can not be change)
        -Numeric
        -Strings
        -Tuples
    -mutable data types (Items can be change) (liable to change)
        -Lists
        -Dictionaries
        -Sets

Immutable :
Numeric (Representation of Numbers in other ways : Binary, Octal, Hexadecimal)
    -int(Signed Integers)
    -float(Real Numbers)
    -Complex Numbers
Strings
    -declared using single or double quotes
Tuples
    -values separated by comma
    -enclosed using parenthesis ()
    -it can have objects of different data types
    -elements cannot be changed because Tuple is immutable


Mutable:
Lists
    -it can have objects of different data types
    -enclosed using square brackets[]
    -value of it's element can be change
Dictionaries
    -contains pairs of key:value
    -pairs are separated by comma
    -enclosed using curly braces{}
Sets
    -unordered collection of items
    -every element in set has to be unique if a = {1,2,3,3} then it will be set a = {1,2,3}
    -enclosed using {}
    -print result will come in ordered items

'''

# Immutable Data Types
# Numerics
a = 10
b = 9.99
c = 5 + 6j
d = 6 + 7j
e = '1001'

# type() used to check variable's type
print(type(a))
print(type(b))
print(type(c))
print(a)
print(b)
# convert number with any base to decimal
print(int(e,2)) #=> From bin(2) to dec, we can also do hex(16) to dec using int(h,16) and for oct 8 also. where base 2-36 and 0 (it takes base from string)
print(d-c)


#Strings
A = 'Strings in Python'
B = "Python Strings"
print(type(A))
print(B)


#Tuples
tup1 = (2,4,4.6,'tests')
print(tup1)
# slicing tuple and store it into new variable
viv = tup1[1:3]
print(viv)
# accessing tupe element
print(tup1[3])
# tup1[2] = 7 #it generates error becuase element of tuple cannot be changed.
print((a,b,c, viv))

#Mutable Data Types
#Lists
Alst = [1,4,5,6.55,'testlist','list','test',[66,77,88],(33,44,55)]
print(Alst) #prints whole list
# accessing or changing list elements
Alst[5] = 'list1'
print(Alst)
Alst[7][2] = 99
print(Alst)
#we cananot change value Alst[8][0-2] because Alst[8] is tuple. However We can change whole tuple to another whole new element.
Alst[8] = 111
print(Alst)

#Dictionaries (Key:Value) pairs
dict1 = {'RollNo':11, 'Name':'ABC', 'Result':'Pass'}
print(dict1) #prints whole dictionary
print(dict1['Name']) #access specific value using its key
dict1['Name'] = 'XYZ' # changing or adding new key: value pair
print(dict1['Name'])

contact = {'Alice':90909, 'Bob':90800, 'Charlie':78665, 'Jane':35562, 'Mike':27763}
print(contact['Charlie'])


#Sets - unordered list
Aset = {1,3,4,2,6,6,7,8,9,9,9,0}
Bset = {'A','C','B','B','E','D','E','E'}

print(Aset)
print(Bset)
#print(Bset[4]) #it gives error because set is not subscriptable
Aset.add(5)
Aset.remove(6)
print(Aset)