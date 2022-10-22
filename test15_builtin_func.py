'''
some functions are built-in it means we don't have to import any module for that functions
'''

# sorted()      --> it returns sorted items of related variable
print('sorted() : ')
lst1 = [12, 1, 34, -5, 0, -11]
print(sorted(lst1))

# all()         --> it returns true if all items are in variable are true or like exist E.g.:-....
print('all() : ')
lst2 = [True, 1, 'abc', 2]      #--> it has all true values
lst5 = [True, -1, 'acv']
print(all(lst2))
print(all(lst5))

lst3 = [True, 2, False]         #--> lst3 and lst4 both have False items, lst3 have False and lst4 have 0
lst4 = [True, 0, 'acv']
lst6 = [True, None, 'acv']      #--> None is keyword but is is not have true value  so it won't have all true value
print(all(lst3))
print(all(lst4))
print(all(lst6))

#any()          --> it returns true if atleast one item of variable is true
print('any() : ')
lst7 = [True, False, 35]
lst8 = [False, 0, None]
print(any(lst7))
print(any(lst8))

#bool()         --> it return boolean value of that item
print('bool() : ')
print(bool(0))
print(bool(1))
print(bool('str'))
print(bool(None))
print(bool(False))
print(bool(True))
print(bool('A'))

#chr()          -->it returns character which unicode is given integer
print('chr() : ')
print(chr(125))
print(chr(62))

#abs()          --> returns absolute value of integer, floating point number & complex numbers
print(abs(10/9))
#int()          --> convert string(which are only numbers Not alphabets) into integer
#len()
#reversed()     --> reverses the sequence using loop

#bin()          --> binary representation of number prefixed with '0b'
print('bin() : ')
print(bin(14))

#sum()          --> sum of numbers
print('sum() : ')
print(sum((1, 7, 2, 4, 6)))

#enumerate()    -->it used to indexing iterables(lists, tuples, etc..), it returns list of tuples, each tuple consists index values and items
print('enumerate() : ')
fruits = ['apple', 'banana', 'grapes', 'orange']
fruitstpl = ('apple', 'banana', 'grapes', 'orange')
enfrt = enumerate(fruits)
enfrt2 = enumerate(fruits, 10)      #--> starting index as second parameter
print(type(enfrt))
print(enfrt)
print(list(enfrt))
print(list(enfrt2))