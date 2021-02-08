"""
Let's pretend your company just hired your friend from college and paid you a referral bonus. Awesome! To celebrate, you're taking your team out to the terrible dive bar next door and using the referral bonus to buy, and build, the largest three-dimensional beer can pyramid you can. And then probably drink those beers, because let's pretend it's Friday too.

A beer can pyramid will square the number of cans in each level - 1 can in the top level, 4 in the second, 9 in the next, 16, 25...

Complete the beeramid function to return the number of complete levels of a beer can pyramid you can make, given the parameters of: your referral bonus, and the price of a beer can

For example:

beeramid(1500, 2); // should === 12
beeramid(5000, 3); // should === 16
"""

# Solution can also be---
"""
Let number of levels be L, number of cans be N. 

1 + 2**2 + 3**2 + 4**2 +.... = N
(Sum of squared series) = L (L + 1)(2L + 1)/6
    
    L = 1
    while True:
        if can_count < L*(L+1)*(2*L+1)/6: 
            return L-1
        L += 1
"""
def beeramid(bonus, price):

    can_count = bonus // price
    level = 0

    while ((level+1)**2 <= can_count):
        level += 1
        can_count -= level ** 2
    
    return level


if __name__ == "__main__":
    print(beeramid(5000, 3))
    print(beeramid(-1, 2))
    print(beeramid(21, 1.5))
