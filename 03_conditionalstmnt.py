'''
Conditional statements
    -if, elif, else
'''

a, b, c = 45, 62, 30
if a < b:
    if a < c:
        if b < c:
            print("{}<={}<={}".format(a, b, c))
        else:
            print("{}<={}<={}".format(a, c, b))
    else:
        print("{}<={}<={}".format(c, a, b))
else:
    if b < c:
        if a < c:
            print("{}<={}<={}".format(b, a, c))
        else:
            print("{}<={}<={}".format(b, c, a))
    else:
        print("{}<={}<={}".format(c, b, a))

x = 10
y =5
if x>11:
    print("yes")
elif x==10:
    print("on elif")
else:
    print("in else")

