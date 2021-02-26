"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

"""

def brute_force(nums, k):
    for i in range(len(nums)-1):
        for j in range(len(nums)-i):
            if nums[i] + nums[j] == k:
                return True
    return False

def second_method(nums,k):
    s = set(nums)
    for i in nums:
        if k-i in s:
            return True
    return False

print(brute_force([10,15,3,7],17))
print(second_method([10,15,3,7],17))
