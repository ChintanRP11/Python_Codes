'''structure of assert is {
assert condition, string(if condition did not meet)} if x is lessthan 10 then string printed
code after assertion error will not run
we can handle it using try and except block'''

x= int(input())
# if assert fails then it return error with message and execution stops.
assert x>10, 'Wrong input...' 
print('valid input')
