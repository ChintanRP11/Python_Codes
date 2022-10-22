import pickle, student

f = open('student.dat', "ab")
s = student.Student(123, "johny", 67)
#store data of student in binary format using pickle
#it dumps data into student.dat file
pickle.dump(s, f)
f.close()