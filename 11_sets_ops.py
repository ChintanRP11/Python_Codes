x = set('this is python sets')
print(x)

a = {1, 2, 3, 4, 5}
b = {4, 5, 6 ,7, 8}
c = {2, 3, 5}

print(a|b)                  #-->union of sets
print(a.union(b))           #-->union of sets

print(a&b)                  #-->intersection of sets
print(a.intersection(b))    #-->intersection of sets

print(a-b)                  #-->differnce of sets
print(a.difference(b))      #-->differnce of sets

print(c.issubset(a))        #--> checking subset

print(a.issuperset(c))      #--> checking superset

print(1 in a)

set1 = {1, 2, 3, 4, 'a', 'b'}
set1.add('f')
print(set1)

print(set1.remove(3))              #--> throws error if item is not in set
print(set1)

print(set1.discard(5))      #--> Cannot generate error if item is not in set
print(set1)

set1.pop()                  #--> remove random element from set
print(set1)

set1.clear()                #-->remove all elements from set
print(set1)
