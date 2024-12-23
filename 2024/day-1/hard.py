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

frequency_list = [(a * list2.count(a)) for a in list1]

print(sum(frequency_list))
