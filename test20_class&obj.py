class demo():
    pass


x = demo()  # x is instance of class demo.
print(x)


class demo2():
    def met1(self):
        print('Hello this is met1 method from demo2 class')


y = demo2()  # y is instance(object) of class demo2
print(y)
y.met1()  # y is calling met1

print(demo2())
demo2().met1()  # here calling met1 without y(any instance)
