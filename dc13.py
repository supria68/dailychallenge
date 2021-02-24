# Detect Capital
# Source - https://leetcode.com/problems/detect-capital/

# 1. All letters in this word are capitals, like "USA".
# 2. All letters in this word are not capitals, like "leetcode".
# 3. Only the first letter in this word is capital, like "Google".
#

def detectCapitalUsage(s):
    if s == s.upper() or s == s.lower():
        return True
    elif s == s.capitalize():
        return True
    else:
        return False

print(detectCapitalUsage('FlaG'))
