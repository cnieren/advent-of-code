import os
import re

filename = 'input.txt'
updates = []
rules = {}

def addRule(rule):
    p = re.compile(r"(\d+)\|(\d+)")
    m = p.match(rule)
    key = int(m.group(1))
    value = int(m.group(2))

    if key in rules:
        rules[key].append(value)
    else:
        rules[key] = [value]

def is_valid_update(update):
    
    for i in range(len(update) - 1):
        for j in range(len(update)):
            # Don't check the first item against its self
            if i == 0 and j == 0:
                continue

            # Check the values before this one
            if i < j:
                if not update[i] in rules:
                    return False
                if update[j] in rules[update[i]]:
                    continue
                else:
                    return False

            # Don't check against yourself
            if i == j:
                continue

            # Check the values after this one
            if i > j:
                if not update[j] in rules:
                    return False
                if update[i] in rules[update[j]]:
                    continue
                else:
                    return False
    
    return True

def find_middle_update(update):
    mid = int(len(update) / 2)
    return update[mid]

if not os.path.isfile(filename):
    print(f'File: {filename} -- Not Found')
    exit()

with open(filename) as filep:
    is_reading_rules = True
    for line in filep:
        if not line.strip():
            is_reading_rules = False
            continue

        if is_reading_rules:
            addRule(line)
        else:
            updates.append([int(x) for x in line.strip().split(',')])

total = 0
for update in updates:
    if is_valid_update(update):
        total += find_middle_update(update)

print(total)