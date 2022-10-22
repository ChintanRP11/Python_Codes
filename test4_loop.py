'''
Loops:
    -for
    -while
    -nested loops

Loop Control statements:
    -break --> breaks the loop
    -continue --> skip the step of loop as given condition
    -pass --> null operation, its also used when you don't want to write any code inside loop or function

'''

#While loop
a = 15
while (a > 0):
    print(a, end=' ')
    a = a - 1
print()

#For loop
for b in range(10):
    print(b, end=' ')
print()

#we can also use loops for to create diff data types:
list = [x**2 for x in range(5)] #--> it is just storing elements in list
print(list)

#Nested loop
for c in range(1,6):
    for d in range(c):
        print(d, end='')
    print()


#break statement
for e in range(10):
    if e == 6:
        break
    print(e, end=', ')
print()

#continue statement
#skips when f becomes 6, otherwise it prints f.
for f in range(10):
    print('Y', end='')
    if f == 6:
        continue
    print(f, end=', ')
print()

#pass statement
for g in range(5):
    if g > 1:
        pass
        print("in pass....")
    else:
        print(g)


lst = ['sdf', 'sdfssf', 'dfds', 'we']
for i in lst:
    if i == 'sdfssf':
        continue
    else:
        print('no')