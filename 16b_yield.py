'''
yield and return statements both are used inside function definitions.
--> return statement is only executed once in a single function call
--> while yield can be used multiple times in a single function call. 
--> return statement returns a specific variable or expression value. 
--> yield statement returns a iterator that can be iterated using next().
'''


def generator_fun(x,y):
	while x < y:
		yield x
		x += 1

res = generator_fun(10,17)
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))