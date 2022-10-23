# creation of class
class demo():
    pass

x = demo()  # x is instance of class demo.
print(x)

class demo2():
    # method of class demo2. accessed only by demo2 class objects
    def met1(self):
        print('Hello this is met1 method from demo2 class')


y = demo2()  # y is instance(object) of class demo2
print(y) #prints object of class demo2
y.met1()  # y is calling method met1

print(demo2())
demo2().met1()  # here calling met1 without y(any instance)
