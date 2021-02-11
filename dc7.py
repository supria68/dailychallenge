"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.


move_zeros([False,1,0,1,2,0,1,3,"a"]) # returns[False,1,1,2,1,3,"a",0,0]
"""

def move_zeros(array):
    z_arr = [] 
    ret_arr = [] 
    for i in array:
        if i == 0 or i == 0.0:
            if type(i) == int or type(i) == float:
                z_arr.append(0)
            else:
                ret_arr.append(i)
        else:
            ret_arr.append(i)
    
    return ret_arr + z_arr

print(move_zeros([False,1,0,1,2,0,1,3,"a"]))
print(move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]))
print(move_zeros([0]))
print(move_zeros([0, 'a', 9, -6, -6, 'b', 2, '0', 'c', 0, True, 0, False, 'a', 0, 0, 0, 'a', 3, 'string', 'z', -7, 9, 0, 4, '0', 5, -8]))
print(move_zeros([False]))
