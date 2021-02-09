"""
Can you check to see if a string has the same amount of 'x's and 'o's?

Eg:
    XO("ooxx") => true
    XO("xooxx") => false
    XO("ooxXm") => true
    XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
    XO("zzoo") => false

Note: The method must return a boolean and be case insensitive. The string can contain any character
"""


def count_chr(s):
    x_count = s.lower().count('x')
    o_count = s.lower().count('o')
    if x_count == o_count:
        return True
    else:
        return False

print(count_chr('xOoxx'))
print(count_chr('zpzpzpp'))
