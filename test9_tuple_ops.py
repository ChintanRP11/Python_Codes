tup1 = (1, 4, 5, 63, 45, 67, 89)

print(len(tup1))        #-->length of tuple
print(max(tup1))        #-->max value from tuple
print(min(tup1))        #-->min value from tuple

tup2 = ('Java', 'Python', 'C', 'C++', 'R', 'PHP')
tup3 = ('JS', 'HTML', 'CSS', 'MySQL')

tup4 = tup2 + tup3      #--> adding tuples
tup5 = tup2*2           #--> multiplication of tuple
print(tup4)
print(tup5)

del tup2  #--> deleting tuple

tpl1 = ([1, 2, 3], [4, 5, 6], [7, 8, 9, 0])
print(tpl1)
print(len(tpl1))
print(tpl1[0][0:2])
tpl1[1][1] = 11         #-->changing item of list inside the tuple
print(tpl1)

lst1 = list(tpl1)       #--> converting tuple into list, used for changing value of tuple and then it will be converted to tuple again
print(lst1)

lst1.append([10, 11, 12, 13])
print(lst1)

tpl1 = tuple(lst1)      #--> converting list into tuple
print(tpl1)
