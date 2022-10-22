'''
Global and Local Variables
'''

a = 40          #--> it is global variable it declares not in function and it can be used anywhere in program
def sum(b):
    c = 50      #--> it is local variable it declares inside func. and it can be used within this function only
    return b + c
print(a)
print(sum(a))
print(c)