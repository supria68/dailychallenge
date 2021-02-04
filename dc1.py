"""
Your goal is to create a function that removes the first and last letters of a string. Strings with two characters or less are considered invalid. You can choose to have your function return null or simply ignore.
"""

def solution(somestr):
    if len(somestr) > 2:
        return somestr[1:-1]
    return None

def goingwild(somestr):
    if len(somestr) > 2:
        temp = list(somestr)
        temp.pop()
        temp.reverse()
        temp.pop()
        temp.reverse()
        return ''.join(temp)
    return None 

if __name__ == "__main__":
    
    # my testcases
    print(solution('hello whatsup?')) # ello whatsup
    print(solution('d4')) # None

    print(goingwild('hello whatsup?')) # ello whatsup

