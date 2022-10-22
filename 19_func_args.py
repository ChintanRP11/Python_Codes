def fun1(a):
    return a + a


print(fun1(1))  # if fun1() .... (no arguments) then it will gives error


# Keyword Argument :
def fun2(str, int):
    return str * int


print(fun2(3, 'keys'))


def fun3(a1, a2, a3, a4):
    return a1 * a3 + a2 * a4


print(fun3(a1=2, a2=3, a3=11, a4=12))


# Default Argument :
def fun4(a, d=5):
    return a * d


print(fun4(3))  # if you don't assign value of 'd' it will take d = 5
print(fun4(3, 4))  # here, d = 4


# variable-length arguments :
def person(user, *users):  # -->must have one argument for user
    print('Users of python : ' + user)
    for i in users:
        print('Users of python : {}'.format(i))
    print()


# person()                       -->it gives error
person('chintan')
person('jay', 'vivek', 'milan')


def person1(*users):  # --> here if no argument pass in function then it won't give an error because it can accepts any arguments from 0 times to n times
    for i in users:
        print('Users of python1 : {}'.format(i))
    print()


person1()
person1('chintan')
person1('jay', 'vivek')


# variable length keyword arguments :
def myfunc(a, b, *students, **kwargs):
    print(str(a))
    print(str(b))
    print(str(students))
    print(str(kwargs))


myfunc(10, 'abc', 'Chintan', 'Jeel', name='Jay', country='India')
# o/p contains
# 10                                    --> a
# abc                                   --> b
# ('Chintan', 'Jeel')                   --> *students
# {'name': 'Jay', 'country': 'India'}   --> **kwargs
