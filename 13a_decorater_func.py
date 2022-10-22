def decorfunc(fun):
	def doubler():
		result = fun()
		return result*2
	return doubler

# @<decor function name> it is used to do some calculation or perform any actions on any functions
@decorfunc
def num():
	return 5

@decorfunc
def str1():
	return 'new'

print(num())
print(str1())