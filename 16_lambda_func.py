'''
Lambda is short-hand function

normal functions are defined using 'def' keyword and
anonymous functions are defined using 'lambda' keyword

when we require nameless function for short period of time

=> Map, Filter, Reduce using lambda
Map :
it returns list of results after applying the given function each item of given iterable of list, tuples, etc.

Filter :
it returns some filtered values using lambda function inside it

Reduce :
it used to computation on iterables
it used to reduce list as sum of list items, max from list, etc..
importing module compulsary : from functools import reduce

'''
#Lambda :
sqr = (lambda x : x**2)
print(sqr(3))
print(sqr(5))

#Map :
def sum(n):
    return n+n

numbers = (1,2,3,4)
result = map(sum, numbers)
print(result)
print(list(result))

#--> now, Map using lambda
print('Map lambda')
items = (2, 3, 5, 8)
res = map(lambda x:x+x, items)  # in map, if function generate any value then it will return each values but if there is condition then it will return true or false for each inputs. refer(Practice/P_43.py)
print(list(res))

#Filter :                       # in map, lambda returns value true or false, and filter returns that items which are true for given condition
print('filter')
data2 = [-1, 4, -6, 7, 9]
flt_pos = filter(lambda x:x>0, data2)
flt_neg = filter(lambda x:x<0, data2)
print(list(flt_pos))
print(list(flt_neg))

set1 = {-1, 4, 6}
flt_inset = filter(lambda x:x in set1, data2)
print(list(flt_inset))

#Reduce :
from functools import reduce
import operator

lst1 = [1, 2, 4, 5, 6, 9, 0]
red_lst = reduce((lambda x, y : x+y), lst1)
red_lst1 = reduce(operator.add, lst1)
print(red_lst)
print(red_lst1)

# finding max using reduce functionality
max_lst = reduce((lambda x, y : x if x > y else y), lst1)
print(max_lst)