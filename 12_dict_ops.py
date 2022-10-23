dict1 = {'name':'chintan', 'age':55, 'rno':45, 'city':'pune'}
set1 = {1, 2, 3, 4}
lst1 = [5, 6, 7, 8, 9]

print(dict1['name'])            #--> print certain value of given key
print(len(dict1))               #--> no of pairs are in dictionary
st = str(dict1)                 #--> convert dictionary into string
print(str(dict1))

print(type(set1))               #--> returns type of variable
print(type(lst1))
print(type(dict1))

del(dict1['rno'])               #--> remove an certain pair from dictionary if available and if not avail then throws an error
print(dict1)

print(dict1.items())            #--> return all items of dictionary
print(dict1.keys())             #--> return keys
print(dict1.values())           #--> return values

print(dict1.copy())             #--> creates copy of dictionary
dict1.clear()                   #--> remove all items from dictionary
print(dict1)
