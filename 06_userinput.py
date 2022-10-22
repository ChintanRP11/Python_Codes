'''
-Taking inputs from user
-input()
-takes multiple inputs through only one input() function using .split() function
'''

name = input('Enter Name : ')
gender, age = input('Enter Your Gender and Age : ').split(',')

print('Name = {}, Age = {}, Gender = {}'.format(name, age, gender))
print(f'Name = {name}, Age = {age}, Gender = {gender}')