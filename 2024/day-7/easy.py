import os

filename = 'input.txt'
data = []
result = []

if not os.path.isfile(filename):
    print(f'File: {filename} -- Not Found')
    exit()

with open(filename) as filep:
    for line in filep:
        test_val, numbers = line.split(':')
        data.append((int(test_val), [*map(int, numbers.strip().split())]))

for test_val, numbers in data:
    possibles = [numbers.pop(0)]

    while numbers:
        curr = numbers.pop(0)
        temp = []
        for p in possibles:
            temp.append(p + curr)
            temp.append(p * curr)
        possibles = temp
    
    if test_val in possibles:
        result.append(test_val)

print(sum(result))