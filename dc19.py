"""
Unique usernames

You get an list of names and need to return a list of unique usernames.
For a duplicate name, add the next integer after the name

For example:
Input
['Julie', 'Emma', 'Zoe', 'Liam', 'Emma']
Output
['Julie', 'Emma', 'Zoe', 'Liam', 'Emma1']

Input
['Julie', 'Zoe', 'Zoe', 'Liam', 'Emma', 'Zoe']
Output
['Julie', 'Zoe', 'Zoe1', 'Liam', 'Emma', 'Zoe2']
"""

def unique_unames(names):
    usernames = [names[0]]
    for name in names[1:]:
        if name not in usernames:
            usernames.append(name)
        else:
            count = sum(name in user_name for user_name in usernames)
            usernames.append(name + str(count))
    return usernames

print(unique_unames(['Julie', 'Zoe', 'Zoe', 'Liam', 'Emma', 'Zoe']))
print(unique_unames(['Julie', 'Emma', 'Zoe', 'Liam', 'Emma']))

