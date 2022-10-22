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

if True:
    obj = college()
    obj.test()
    # del obj             # --> deleting object
    # obj.test()         #--> this will throw an error because object is destructed
    obj = clg()         #--> prev. 'obj' will be destructed and new (this) will be constructed

print('thsi jjk slfs')
