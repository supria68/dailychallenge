"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21
"""

def reverse_dig(num):
    num = str(num)

    if num.startswith('-'):
        return int('-'+num.split('-')[1][::-1])
    else:
        return int(num[::-1])


print(reverse_dig(123))
print(reverse_dig(-321))
print(reverse_dig(100))

