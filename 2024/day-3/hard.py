import os
import re

filename = 'input.txt'
result = 0

if not os.path.isfile(filename):
    print(f'File: {filename} -- Not Found')
    exit()

with open(filename) as filep:
    data = filep.read()

    mul_pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    do_pattern = re.compile(r"do\(\)")
    dont_pattern = re.compile(r"don't\(\)")

    sep=')'
    chunks = [x+sep for x in data.split(")")]

    enabled = True
    for chunk in chunks:
        do_found = do_pattern.search(chunk)
        dont_found = dont_pattern.search(chunk)
        mul_found = mul_pattern.search(chunk)
        if do_found:
            enabled = True
        elif dont_found:
            enabled = False
        elif mul_found and enabled:
            result += int(mul_found.group(1)) * int(mul_found.group(2))

print(result)