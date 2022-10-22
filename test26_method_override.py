'''
Method Overriding :
In this both Parent and Child class Have same method, so when we call that method using child class's object then there will be child class's method will be called
'''
class vehicle:
    def v_type(self):
        print('This is from base class')

class car(vehicle):
    def c_type(self):
        print('This is from derived class')
    def v_type(self):                           # it overrides the method of parent class
        print('This is from derived class')

ob = car()
ob1 = vehicle()
ob.v_type()
ob1.v_type()