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
        chunks = line.strip().split("don't()")
        valid = []
        for i in range(len(chunks)):
            if i == 0:
                valid.append(chunks[i])
                continue

            start = chunks[i].find("do()")

            if start != -1:
                valid.append(chunks[i][start + 4:])

        valid_line = ''.join(valid)
        print(valid_line)

        iterator = p.finditer(valid_line)
        for match in iterator:
            data.append([int(match.group(1)), int(match.group(2))])

for i in range(len(data)):
    result += (data[i][0] * data[i][1])

print(result)