import re
print('Please enter file name:')
fname = input()
try:
    fhand = open(fname)
except:
    fhand = open('regex_sum_876892.txt')
print('Sum =', sum(int(i) for i in re.findall('[0-9]+',fhand.read()) ))