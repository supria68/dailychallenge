"""
You are given a small checkbook to balance that is given to you as a string. Sometimes, this checkbook will be cluttered by non-alphanumeric characters.

The first line shows the original balance. Each other (not blank) line gives information: check number, category, and check amount.

You need to clean the lines first, keeping only letters, digits, dots, and spaces. Next, return the report as a string. On each line of the report, you have to add the new balance. In the last two lines, return the total expenses and average expense. Round your results to two decimal places.

Example Checkbook
1000.00
125 Market 125.45
126 Hardware 34.95
127 Video 7.45
128 Book 14.32
129 Gasoline 16.10

Example Solution
Original_Balance: 1000.00
125 Market 125.45 Balance 874.55
126 Hardware 34.95 Balance 839.60
127 Video 7.45 Balance 832.15
128 Book 14.32 Balance 817.83
129 Gasoline 16.10 Balance 801.73
Total expense 198.27
Average expense 39.65
"""

import re

filename = 'myfile.txt' #contains the eg!

with open(filename) as f:
    content = f.read().splitlines()
    total = float(re.sub(r'[^0-9\.]','',content[0]))
    expense = 0
    print(total)
    for item in content[1:]:
        item = re.sub(r'[^a-zA-Z0-9\.\s]','',item)
        id, name, bill = item.split(' ')
        total = round(total - float(bill),2)
        expense += float(bill)
        print(id +' '+name+' '+str(bill)+' '+'Balance: '+str(total))
    print('Total expense '+str(round(expense,2)))
    print('Average expense '+str(round(expense/(len(content)-1),2)))

