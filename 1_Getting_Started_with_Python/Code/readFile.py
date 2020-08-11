fhand = open('list.txt')
lst = []
lst = fhand.read().split()
print(lst)

for i in range(len(lst)):
    if lst[i].endswith(','):
        lst[i] = lst[i][:len(lst[i]) - 1]

print(lst)
