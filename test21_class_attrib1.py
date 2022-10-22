'''
here two types of attributes
    - 1. Built-in attribs..
    - 2. User-defined attribs...

'''

# Built in attribs.......
class diamond():
    '''this is diamond class and docstrings'''
    count = 0

print("btfn__dict__ : ", diamond.__dict__)          #it gives class's namespace means details of class in dictionary format
print("btfn__doc__ : ", diamond.__doc__)            #it gives class's document string
print("btfn__name__ : ", diamond.__name__)          #it gives diamond class name
print("btfn__module__ : ", diamond.__module__)      #it gives module name in which class is defined, in this case it shows __main__ but if class is imported from another module then it will shows that  module name
print("btfn__bases__ : ", diamond.__bases__)        #it gives base class name, it used when classes are inherited