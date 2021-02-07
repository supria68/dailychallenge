"""
Write a function that returns the number (count) of vowels in a given string. Letters considered as vowels are: a, i, e, o, and u. The function should be able to take all types of characters as input, including lower case letters, upper case letters, symbols, and numbers.
"""

def countVowels(s):
    counter = 0
    for i in list(s):
        if i.lower() in ['a','e','i','o','u']:
            counter += 1
    return counter


if __name__ == "__main__":
    print(countVowels('coOpEr'))
