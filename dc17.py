"""
Implemet a Base converter which takes in a int and the base to convert
"""

def baseConverter(num, base):
    digits = '0123456789ABCDEF'
    temp = []
    ret_num = '' # to be returned after the conversion

    while num > 0:
        temp.append(num % base) # remainder
        num = num // base

    while len(temp) > 0:
        ret_num += digits[temp.pop()]

    return ret_num


print(baseConverter(4,2)) # 100
print(baseConverter(15,16)) # F
print(baseConverter(9,8)) # 11
print(baseConverter(15,6)) # 23
