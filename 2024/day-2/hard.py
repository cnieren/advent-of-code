import os
import string

filename = 'input.txt'
data = []
safeCount = 0

def is_safe(levels):
    difs = [a - b for a, b in zip(levels, levels[1:])]

    is_monotonic = all(i > 0 for i in difs) or all(i < 0 for i in difs)
    is_in_range = all(0 < abs(i) <= 3 for i in difs)

    return is_monotonic and is_in_range

if not os.path.isfile(filename):
    print(f'File: {filename} -- Not Found')
    exit()

with open(filename) as filep:
    for line in filep:
        levels = [*map(int, line.split())]
        if is_safe(levels):
            safeCount += 1
        else:
            for i in range(len(levels)):
                tolerated_levels = levels[:i] + levels[i+1:]
                if is_safe(tolerated_levels):
                    safeCount += 1 
                    break

print(safeCount)