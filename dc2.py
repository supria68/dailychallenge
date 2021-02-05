"""
Your task is to return a string that displays a diamond shape on the screen using asterisk (“*”) characters.
  *
 ***
*****
 ***
  *

The shape that the print method will return should resemble a diamond. A number provided as input will represent the number of asterisks printed on the middle line. The line above and below will be centered and will have two less asterisks than the middle line. This reduction will continue for each line until a line with a single asterisk is printed at the top and bottom of the figure.

Return null if input is an even number or a negative number.

"""


def diamond(count):
    
    if count <= 0 or count % 2 == 0:
        print('Please input a positive odd number')
        return
    for i in range(count):
        i = i - count // 2
        if i < 0:
            i = -i
        print(' ' * i + '*' * (count - i * 2) + ' ' * i) 

if __name__ == "__main__":
    diamond(5)
    diamond(8)
