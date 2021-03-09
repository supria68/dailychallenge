"""
Write a function that receives string and number,
and returns original string if number <= length of string, or
string filled with spaces before original string with length = number

Example 
>> string_fill("abc", 7)
    abc

>> string_fill("abc", 2)
abc

"""

def string_fill(s, num):
    if len(s) >= num:
        return s
    else:
        count_spaces = num - len(s)
        return " " * count_spaces + s


#execute the function
print(string_fill("abc", 7))
print(string_fill("abc", 2))
