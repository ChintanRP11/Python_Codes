import math

# setting up extra bit as per requirements. k for integer part and m for float part.
def bitsetter(binNum, k, m):
    if k == 0 and m == 0:
        return binNum
    iPart, fPart = binNum.split('.')
    il = len(iPart)
    fl = len(fPart)
    if il < k:
        iPart = '0'*(k-il) + iPart
    if fl < m:
        fPart = fPart + '0'*(k-fl)
    return iPart+'.'+fPart

# binary to decimal conversion
def bin2dec(binNum):  
    iPart, fPart = binNum.split('.')
    iPart = int(iPart)
    decimal, i, n = 0, 0, 0
    while(iPart != 0):
        dec = iPart % 10
        decimal = decimal + dec * pow(2, i)
        iPart = iPart//10
        i += 1
    frac = 0
    mul = 1/2
    for i in fPart:
        if i == '1':
            frac += 1*mul
        mul /= 2
    return decimal+frac

# Biased representation of Binary to decimal
def biasbin2dec(binNum, bias):
    num = bin2dec(binNum)
    return num-bias

# Decimal to binary conversion
def dec2bin(num,k=0,m=0):
    res = ''
    dec = int(num // 1)
    frac = num % 1
    while dec != 0:
        rem = dec % 2
        dec = dec // 2
        res = str(rem) + res
    res += '.'
    while frac != 0.0:
        ml = frac * 2
        res += str(int(ml))
        frac = ml % 1
        
    res = bitsetter(res, k , m)
    return res
    
#Biased representation of Decimal to Binary
def biasdec2bin(dec, bias, k=0, m=0):
    num = dec + bias
    return dec2bin(num,k,m)

#Sign Magnitude representation of Decimal to Binary
def signmagdec2bin(dec, k=0, m= 0):
    if dec < 0:
        bn = dec2bin(dec*-1, k-1, m)
        res = '1' + bn
    else:
        bn = dec2bin(dec, k-1, m)
        res = '0' + bn
    return res
        
#2's Complement representation of Decimal to Binary
def twoscompd2b(num,k=0,m=0):
    if num >= 0:
        return dec2bin(num,k,m)
    else:
        res = onescompd2b(num,k)
        ext = ((1/2)**m)
        res = bin2dec(res) + ext
        return dec2bin(res)

#1's Complement representation of Decimal to Binary
def onescompd2b(num,k=0,m=0):
    if num >= 0:
        return dec2bin(num,k,m)
    else:
        res = ''
        bn = dec2bin(num*-1, k ,m)
        for i in bn:
            if i == '1':
                res += '0'
            elif i == '0':
                res += '1'
            else:
                res += '.'
        return res

# this fucntions gives the digits require to represresent decimal to any base
def reqbits(frm, to):
    res = math.log(frm, to)
    print(f'{res:.2f}n digits require to represent n digit(base {frm}) number into base {to} ')
    return res
    


print("Dicmal to binary (68.40625): ",dec2bin(68.40625))
print("Biased Dicmal to binary (68.40625,128): ", biasdec2bin(68.40625,128))
print("Biased Dicmal to binary (-68.40625,128): ",biasdec2bin(-68.40625,128))
print("Binary to decimal ('1000100.01101'): ",bin2dec('1000100.01101'))
print("Biased Binary to decimal('111011.10011',128): ",biasbin2dec('111011.10011',128))
print("Biased Binary to decimal('11000100.01101',128): ",biasbin2dec('11000100.01101',128))

print()
print("Dicmal to binary (37.8125): ",dec2bin(37.8125))
print("Biased Dicmal to binary (37.8125,64): ", biasdec2bin(37.8125,64))
print("Biased Dicmal to binary (-37.8125,64): ", biasdec2bin(-37.8125,64))
print("Binary to decimal ('100101.1101'): ",bin2dec('100101.1101'))
print("Biased Binary to decimal('1100101.1101',64): ",biasbin2dec('1100101.1101',64))
print("Biased Binary to decimal('0011010.0011',64): ",biasbin2dec('0011010.0011',64))
print("Decimal to Binary using 1's complement (-37.8125,7): ", onescompd2b(-37.8125,7))
print()
print("Decimal to Binary using 2's complement (-37.8125,7,4): ",twoscompd2b(-37.8125,7,4))
print("Decimal to Binary using 2's complement (-7,5): ",twoscompd2b(-7,5))
print("Decimal to Binary using 2's complement (13,5): ",twoscompd2b(13,5))
print("Decimal to Binary using 2's complement (-14,5): ",twoscompd2b(-14,5))

print("reqbits(10, 2): ",reqbits(10, 2))
print()
print("Dicmal to binary (37.8125): ",dec2bin(37.8125))
print()
print("Sign Magnitude Decimal to binary (37.8125, 7, 4): ",signmagdec2bin(37.8125, 7, 4))
print("Sign Magnitude Decimal to binary (-37.8125, 7, 4): ",signmagdec2bin(-37.8125, 7, 4))
print()
print("Biased Dicmal to binary (37.8125, 64, 7, 4): ", biasdec2bin(37.8125, 64, 7, 4))
print("Biased Dicmal to binary (-37.8125, 64, 7, 4): ",biasdec2bin(-37.8125, 64, 7, 4))
print()
print("Decimal to Binary using 2's complement (37.8125,7,4): ",twoscompd2b(37.8125,7,4))
print("Decimal to Binary using 2's complement (-37.8125,7,4): ",twoscompd2b(-37.8125,7,4))
print()
print("Decimal to Binary using 1's complement (37.8125,7,4): ",onescompd2b(37.8125,7,4))
print("Decimal to Binary using 1's complement (-37.8125,7,4): ",onescompd2b(-37.8125,7,4))


print("Dicmal to binary (68.40625): ",dec2bin(68.40625))
print()
print("Sign Magnitude Decimal to binary (68.40625, 8, 5): ",signmagdec2bin(68.40625, 8, 5))
print("Sign Magnitude Decimal to binary (-68.40625, 8, 5): ",signmagdec2bin(-68.40625, 8, 5))
print()
print("Biased Dicmal to binary (68.40625, 128, 8, 5): ",biasdec2bin(68.40625, 128, 8, 5))
print("Biased Dicmal to binary (-68.40625, 128, 8, 5): ",biasdec2bin(-68.40625, 128, 8, 5))
print()
print("Decimal to Binary using 2's complement (68.40625,8,5): ",twoscompd2b(68.40625,8,5))
print("Decimal to Binary using 2's complement (-68.40625,8,5): ",twoscompd2b(-68.40625,8,5))
print()
print("Decimal to Binary using 1's complement (68.40625,8,5): ",onescompd2b(68.40625,8,5))
print("Decimal to Binary using 1's complement (-68.40625,8,5): ",onescompd2b(-68.40625,8,5))