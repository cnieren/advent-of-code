import os
import string

filename = ''
data = []

if not os.path.isfile(filename):
    print(f'File: {filename} -- Not Found')
    exit()

with open(filename) as filep:
    for line in filep:
        # Read file here


print(data)