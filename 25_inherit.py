'''
Three types of inheritance
- Single Inheritance            # A--> B
- Multiple Inheritance          # (A, B) --> C
- Multilevel Inheritance        # A --> B --> C
'''

# Single Inheritance
print('SINGLE INHERITANCE : ')
class vehicle:
    def v_type(self):
        print('This is from base class')

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
class First():
    def __init__(self):
        super(First, self).__init__()
        print('first')

class Second():
    def __init__(self):
        super(Second, self).__init__()
        print('second')

class Third(Second, First):
    def __init__(self):
        super(Third, self).__init__()
        print('Third')

Third()
Second()
First()

#Multilevel Inheritance :
print('MULTILEVEL INHERITANCE : ')
class Human:
    def Eat(self):
        print('Humans Can Eat.')
class Man(Human):
    def Think(self):
        print('Men can Think.')
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