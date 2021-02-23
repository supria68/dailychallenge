"""
Given the sum and greatest common divisor of two numbers, return those two numbers in ascending order. If the numbers do not exist, return -1 or your language's equivalent.

Examples
Given sum = 12 and gcd = 4...

solve(12,4) = [4,8]. The two numbers 4 and 8 sum to 12 and have a gcd of 4.

solve(12,5) = -1. No two numbers exist that sum to 12 and have gcd of 5.
"""

def solve(s,g):
    
    answer = []
    original_s = s
    while s % g == 0:
        if int(s / g) <= g:
            answer.append(g)
            break

        s = int(s / g)

    if s != original_s and len(answer) == 0:
        answer.append(g)

    if len(answer) == 0:
        return -1

    answer.append(original_s - answer[0])

    return tuple(answer)

print(solve(12,4))
print(solve(12,5))
