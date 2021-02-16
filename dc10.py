"""
You are given two positive integer numbers a and b. These numbers are being simultaneously decreased by 1 until the smaller one is 0. Sometimes during this process the greater number is going to be divisible (as in with no remainder) by the smaller one. Your task is to tell how many times (starting with a and b) this will be the case.

Both numbers might be as big as 10^12
a might equal b


a = 3, b = 5 #start, 5 is not divisible by 3
a = 2, b = 4 #decreased by 1, 4 is divisible by 2
a = 1, b = 3 #decreased by 1, 3 is divisible by 1
a = 0, b = 2 #decreased by 1, the smaller number is 0, end

The result should be 2

"""

#a, b = ()
def how_many_times(a,b):
    div_count = 0
    if a > b:
        a, b = b, a #b holds the largest value

    while True:
        if b % a == 0:
            div_count += 1
        a -= 1
        b -= 1
        if a == 0: # cause b > a
            break
    return div_count


print(how_many_times(150080, 150032)) #10
print(how_many_times(54, 17))#1


# TODO:
#takesup a lot of time to compute for 10**12.. Maybe try finding factors!
