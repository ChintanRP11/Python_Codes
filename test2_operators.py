'''
Operators:
    -Arithmetic
    -Assignment
    -Comparison
    -Logical
    -Bitwise
    -Identity
    -Membership

Arithmetic:
    -Addition(+), Subtraction(-), Multipliacation(*), Division(/), Modulus(%), Exponent(**), Floor Division(//)

Assignment:
    -Assigns value from right to left
    -exa: a = a + b --> a += b

Comparison:
    -Equal(==), Not Equal(!=), >, <, >=, <=

Logical:
    - 'and', 'or', 'not' and more logical operations

Bitwise:
    -it performs logical operation on binary base
    -Binary AND(&), OR(|), XOR(^), NOT(~), Left Shift(<<), Right Shift(>>)

Identity:(use to check identity)
    -is, is not

Membership:(use to check if it exist in list, tuple, dictionary, etc...)
    -in, not in
'''

#Arithmetic
print("ARITHMETIC:")
print(4+5)
print(12-5)
print(4*5)
print(45/5); print(44/5)
print(44%5)
print(2**3) # 2^3
print(5//2) #output in int
print(5-9+6*7**2/2)

#Assignment
print("ASSIGNMENT:")
a, b, c = 10, 5, 24
print(a)
a += b          # it is a = a + b
print(a)
c /= b          # it is c = c / b
print(c)

#Comparison
print("COMPARISON:")
print(10 == 10)
d, e, f = 10, 5, 10
print(d != e)
print(d == f)
print(d > e)
print(e > f)
print(d >= f)
print('abc' == 'abd')
print('abc' == 'abc')

#Logical
print("LOGICAL:")
g, h, i = 10, 20, 30
print(g and h and i)    #it gives greater value
print(g or h or i)      #it gives lesser value
print(not g)            #returns False because g contains some value or data (g is true)
print(not 1)            #returns False because 1 means True
print(not 0)            #returns True because 0 means False

#Bitwise
print("BITWISE:")
A, B, C = 12, 4, 8
print(A & B)
print(C | B)
print(C << 1)
print(C >> 1)

#Identity
print("IDENTITY:")
D, E, F = 'newdata', 'olddata', int(23)
print(D == 'newdata')
# print(D is 'newdata')

#Membership
print("MEMBERSHIP:")
lst1 = [10, 4, 5, 6, 7, 33]
print(3 in lst1)
print(4 in lst1)
a = 5
print(a in lst1)
