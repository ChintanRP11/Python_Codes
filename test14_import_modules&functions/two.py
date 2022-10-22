'''
If one.py file runs then only that file's statements get executed
When two.py file runs then statements of one.py get executed first and then two.py get executed
'''

import one

print('top of two.py file ')

one.onefn()

if __name__ == '__main__':
    print('two.py file')
    print('modulename : ',__name__)
else:
    print('two.py is imported')