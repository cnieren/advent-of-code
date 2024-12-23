import os

filename = 'input.txt'
list1 = []
list2 = []

if not os.path.isfile(filename):
    print(f'File: {filename} -- Not Found')
    exit()

with open(filename) as filep:
    for line in filep:
        bits = line.split()
        list1.append(int(bits[0]))
        list2.append(int(bits[1]))

list1.sort()
list2.sort()

delta_list = [abs(a-b) for a, b in zip(list1, list2)]

print(sum(delta_list))
