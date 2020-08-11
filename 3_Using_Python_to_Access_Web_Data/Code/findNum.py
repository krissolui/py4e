import re
print('Please enter file name:')
fname = input()
try:
    fhand = open(fname)
except:
    fhand = open('regex_sum_876892.txt')
lst = []
for line in fhand:
    nums = re.findall('[0-9]+', line)
    for num in nums:
        lst.append(int(num))
Sum = sum(lst)
count = len(lst)
print('Sum =', Sum, 'Count =', count)