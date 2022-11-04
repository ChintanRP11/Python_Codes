def NAND(x, y):
    if x == 0 and y == 0: return 1
    if x == 0 and y == 1: return 1
    if x == 1 and y == 0: return 1
    if x == 1 and y == 1: return 0

def NOT(x):
    return NAND(x, x)

def AND(x, y):
    return NOT(NAND(x, y))

def OR(x, y):
    return NAND(NAND(x, x), NAND(y, y))

def XOR(x, y):
    return AND(OR(x, y), NOT(AND(x, y))) 

def HALF(x, y):
    carry = AND(x, y)
    sum = XOR(x, y)
    return (carry, sum)

def FULL(x, y, carry_in):
    carry1, sum1 = HALF(x, y)
    carry2, sum2 = HALF(carry_in, sum1)
    carry_out = OR(carry1, carry2)
    return (carry_out, sum2)

def ADD4(left, right):
    carry3, sum3 = FULL(left[3], right[3], 0)
    carry2, sum2 = FULL(left[2], right[2], carry3)
    carry1, sum1 = FULL(left[1], right[1], carry2)
    carry0, sum0 = FULL(left[0], right[0], carry1)
    return [sum0, sum1, sum2, sum3]

def CHOP(left):
    res = []
    chp = [1,1,0,0]
    for i in range(len(left)):
        res.append(AND(left[i],chp[i]))
    return res

def ROUND(left):
    ext = [0,0,1,0]
    nx = ADD4(left,ext)
    res = CHOP(nx)
    return res

print(ADD4([1, 0, 0, 1], [1, 0, 0, 1]))
print()
print(CHOP([1,1,0,1]))
print(ROUND([1,0,1,1]))
print()
print(CHOP([0,1,1,1]))
print(ROUND([0,1,0,1]))

