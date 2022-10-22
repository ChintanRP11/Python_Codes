def generator_fun(x,y):
	while x < y:
		yield x
		x += 1


res = generator_fun(10,20)
for i in res :
	print(i)
