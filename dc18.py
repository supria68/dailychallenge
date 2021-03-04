"""
Reverse an array without affecting special characters
Given a string, that contains special character together with alphabets (‘a’ to ‘z’ and ‘A’ to ‘Z’), reverse the string in a way that special characters are not affected.
Examples:
Input:   str = "a,b$c"
Output:  str = "c,b$a"
Note that $ and , are not moved anywhere.  
Only subsequence "abc" is reversed
Input:   str = "Ab,c,de!$"
Output:  str = "ed,c,bA!$"
"""

def reverse(s):
    inp = list(s)
    l = 0 # from first literal
    r = len(inp) - 1 # from last literal
    
    while l < r:
        #if literal is not an alphabet, proceed
        # else reverse them!

        if inp[l].isalpha() == 0: 
            l += 1
        elif inp[r].isalpha() == 0:
            r -= 1
        else:
            inp[l],inp[r] = inp[r],inp[l]
            l += 1
            r -= 1
            
    return ''.join(inp)

print(reverse("a!!!b.c.d,e'f,ghi"))  # should return i!!!h.g.f,e'd,cba
print(reverse("Ab,c,de!$"))  # should return ed,c,bA!$
