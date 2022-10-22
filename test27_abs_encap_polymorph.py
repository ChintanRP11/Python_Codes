'''
Abstraction, Encapsulation, Polymorphism are key concepts of OOPs.

Abstraction :
Abstraction is used for hiding the code.
exa : print() --> it is function where code of it is hidden we can not show its code in this file, but data in it are not hidden

Encapsulation :
Encap. is used for hiding both data and code.
for this method we can access data using setter and getter method in capsule.

Polymorphism : multi behaviour(shapes)
It is utilized when we have commonly named methods across classes and subclasses
There are same named methods to do same work in different ways
'''

class Shape():
    def __init__(self):
        pass

    def area(self):
        pass

class Square(Shape):
    def area(self, size):
        print('Area of square is : ', str(int(size) * int(size)) )

class Circle(Shape):
    def area(self, size):
        print('Area of circle is : ', str(3.14 * (int(size)**2)) )

ob = Square()
ob.area(10)

ob1 = Circle()
ob1.area(10)
