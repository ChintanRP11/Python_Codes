import random

print(random.randrange(100))
print(random.randrange(1, 100, 7))         # (start, stop, step), random number with every next 7th number like in this case : (1, 8, 15, 21, ...)
print(random.randint(0, 3))                # it returns anyone from (0, 1, 2, 3)

print(random.getstate)                  # it  gives random() 's state
print(random.uniform(1, 2))             # floating number 1<=num<=2
print(random.uniform(4, 2))             # floating number 2<=num<=4
