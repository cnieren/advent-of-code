import os
from collections import defaultdict
import re

def groups(data, func):
    grouping = defaultdict(list)
    for y in range(len(data)):
        for x in range(len(data[y])):
            grouping[func(x, y)].append(data[y][x])
    return list(map(grouping.get, sorted(grouping)))

filename = 'input.txt'
board = []

if not os.path.isfile(filename):
    print(f'File: {filename} -- Not Found')
    exit()

with open(filename) as filep:
    for line in filep:
        # Read file here
        board.append(list(line.strip()))

cols = groups(board, lambda x, y: x)
rows = groups(board, lambda x, y: y)
fdiag = groups(board, lambda x, y: x + y)
bdiag = groups(board, lambda x, y: x - y)

p = re.compile(r"XMAS")
count = 0

for x in range(len(rows)):
    row_str = ''.join(rows[x])
    row_rev = row_str[::-1]
    m = p.findall(row_str)
    count += len(m)
    m = p.findall(row_rev)
    count += len(m)

for x in range(len(cols)):
    col_str = ''.join(cols[x])
    col_rev = col_str[::-1]
    m = p.findall(col_str)
    count += len(m)
    m = p.findall(col_rev)
    count += len(m)

for x in range(len(fdiag)):
    fstr = ''.join(fdiag[x])
    rstr = fstr[::-1]
    m = p.findall(fstr)
    count += len(m)
    m = p.findall(rstr)
    count += len(m)

for x in range(len(bdiag)):
    fstr = ''.join(bdiag[x])
    rstr = fstr[::-1]
    m = p.findall(fstr)
    count += len(m)
    m = p.findall(rstr)
    count += len(m)

print(count)
