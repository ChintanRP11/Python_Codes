'''
Constructor and destructor of class
'''
class college():
    def __init__(self):             #--> Initialize method , object is intialized
        print('constructor for college()')

    def __del__(self):              # --> delete method because object destructed with it, we can manually destroy it using del obj()
        print('destructor of college()')

    def test(self):
        print('this is test')

class clg():
    def __init__(self):
        print('constructor for clg()')

    def __del__(self):
        print('destructor of clg()')


obj = college()
obj.test()
# del obj             # --> deleting object
# obj.test()         #--> this will throw an error because object is destructed

# obj with instance of college() is destructed because here we have assigned new class instance to obj. So, obj will be new constructor for class clg()
obj = clg()
obj2 = college()
print('thsi jjk slfs')


# at the end of the program all instances are destructed automatically