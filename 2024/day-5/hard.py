from collections import defaultdict
import os

filename = 'input.txt'
updates = []
rules = defaultdict(set)

def is_valid_update(update):
    
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if update[j] not in rules[update[i]]:
                return False
    
    return True

def fix_update(update):
    filtered_rules = defaultdict(set)
    for i in update:
        filtered_rules[i] = rules[i] & set(update)
    
    ordered_keys = sorted(filtered_rules, key=lambda k: len(filtered_rules[k]), reverse=True) 
    return ordered_keys


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
            a, b = map(int, line.split("|"))
            rules[a].add(b)
        else:
            updates.append([int(x) for x in line.strip().split(',')])

total = 0
for update in updates:
    if not is_valid_update(update):
        fixed_update = fix_update(update)
        total += find_middle_update(fixed_update)

print(total)