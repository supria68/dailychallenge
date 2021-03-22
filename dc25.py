"""
An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.

For example:

9 is an Armstrong number, because 9 = 9^1 = 9
10 is not an Armstrong number, because 10 != 1^2 + 0^2 = 2
153 is an Armstrong number, because: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
154 is not an Armstrong number, because: 154 != 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190
Write some code to determine whether a number is an Armstrong number.

"""

def is_armstrong(num):
    order = len(str(num))
    total = 0

    for i in str(num):
        total += int(i) ** order

    if total == num:
        return True
    else:
        return False

"""
making it short:

return sum(int(i) ** len(str(num)) for i in str(num)) == num
"""

print(is_armstrong(153)) #True
print(is_armstrong(10)) #False
    
