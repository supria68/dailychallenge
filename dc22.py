# Given a non-negative integer num, repeatedly add
# all its digits until the result has only one digit.
#
# For example:
#
# Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2.
# Since 2 has only one digit, return it.

def recursive_add(num):
    if len(str(num)) == 1:
        return num
    else:
        total = 0
        for i in str(num):
            total += int(i)

        return recursive_add(total)


print(recursive_add(38))
