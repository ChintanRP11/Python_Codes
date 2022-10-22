import pickle

f = open("student.dat", "rb")
obj = pickle.load(f)    # It loads data of one student in obj from file(student.dat)
obj2 = pickle.load(f)
obj3 = pickle.load(f)
obj.display()           #It uses display method from student.py
obj2.display()
obj3.display()
