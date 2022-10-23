'''
Three types of inheritance
- Single Inheritance            # A--> B
- Multiple Inheritance          # (A, B) --> C
- Multilevel Inheritance        # A --> B --> C
'''

# Single Inheritance
print('SINGLE INHERITANCE : ')
# parent class
class vehicle:
    def v_type(self):
        print('This is from base class')

# inherited class from vehicle class, child class
class car(vehicle):
    def c_type(self):
        print('This is from derived class')
    # def v_type(self):
    #     print('This is from derived class')

ob = car()
ob.v_type()
ob.c_type()

# Multiple Inheritance :
print('MULTIPLE INHERITANCE : ')
# parent class 1
class First():
    def __init__(self):
        super(First, self).__init__()
        print('first')

# parent class 2
class Second():
    def __init__(self):
        super(Second, self).__init__()
        print('second')

# child class inherited from class Second and First
class Third(Second, First):
    def __init__(self):
        super(Third, self).__init__()
        print('Third')


Third()     # initialize all its parents classes if they are not already inialized
Second()
First()

#Multilevel Inheritance :
print('MULTILEVEL INHERITANCE : ')
# parent class
class Human:
    def Eat(self):
        print('Humans Can Eat.')

# child class of class Human
class Man(Human):
    def Think(self):
        print('Men can Think.')

# child class of class Man -> this class can access all members of its both parent classes
class Young(Man):
    def Run(self):
        print('Younger can Run.')

ob3 = Young()
ob3.Run()
ob3.Think()
ob3.Eat()
print("btfn__bases__ : ", Young.__bases__)
print("btfn__bases__man : ", Man.__bases__)
print("btfn__bases__third : ", Third.__bases__)