'''
User Defined Attributes :
Three types :
    - Public (test)             # freely used within program
    - Protected (_test)         # only child class and itself accessing, but we can access it outside of class when it is very necessary
    - Private (__test)          # used by itself only not outside of class, it is like hidden attributes, we can also access it outside using class name
'''


class demo():
    def __init__(self):
        self.tst = ('I am Public')
        self._tst = ('I am Protected')
        self.__tst = ('I am Private')

    def test(self):
        print('This is public method.')

    def _test(self):
        print('This is protected method.')

    def __test(self):
        print('This is private method.')

    # It is concept for encapsulation
    def display(self):
        print(self.__tst)


# It is concept for encapsulation
ab = demo()
ab.display()

ob = demo()
print(ob.tst)
print(ob._tst)  # it will not throw an error
# print(ob.__tst)        # it throws an error because it is private attribute
print(ob._demo__tst)  # we can access private attrib this way (this way is called name mangling)

ob.test()
ob._test()
# ob.__test()             # it throws an error because it is private attribute
# but we can use it this way....
ob._demo__test()
