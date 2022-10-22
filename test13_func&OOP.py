'''
functions :
def fun_name(params):
    return <something>

return is used to stop execution of function code after return statement, insider function will not be executed
return also give its value to function calling object

'''

# def person_data(name, age):
#         print('Name : {} and Age : {}'.format(name,age))
#
# abc, xyz = input("Enter name and age : ").split(',')
# person_data(abc, xyz)
# person_data('jay', 34)


# def sum(a, b):
#     sum = int(a) + int(b)
#     print(sum)
#
# sum(12, 23)
# sum(22, 23)

def person(name):
    print(name)
    return name*2           # return is used to stop execution of function
    # print('hello')          # because of "return" this won't be executed

x = person('chintan')
print(x)

a=10
def sum(val1, val2, b=5):
    result = val1 - val2+b
    return result

z= sum(1,2)
print(z)
print(sum(4,3,10))