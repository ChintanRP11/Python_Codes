def onefn():
    print('function from one.py')

print('top of one.py')

if __name__ == "__main__":
    print('one.py file')
    print('modulename : ',__name__)
else:
    print('one.py is imported')
    print('modulename : ',__name__)