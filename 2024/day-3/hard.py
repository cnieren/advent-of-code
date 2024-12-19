import os
import re

filename = 'input.txt'
data = []
result = 0

def mult(a, b):
    return a * b

if not os.path.isfile(filename):
    print(f'File: {filename} -- Not Found')
    exit()

with open(filename) as filep:
    p = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    for line in filep:
        # Read file here
        iterator = p.finditer(line)
        for match in iterator:
            data.append([int(match.group(1)), int(match.group(2))])

for i in range(len(data)):
    result += (data[i][0] * data[i][1])

print(result)