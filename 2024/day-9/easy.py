import os

filename = 'test-input.txt'
disk_map = ''
expanded = ''
data = []

def expand(line: str):
    result = ''
    id = 0
    i = 0
    for c in line:
        if i % 2 == 0:
            result += str(id) * int(c)
            id += 1
        else:
            result += '.' * int(c)
        i += 1
    
    return result
    
def compact(line: str):
    result = line.rstrip('.')
    space_count = line.count('.')

    while space_count > 0:
        target = result.find('.')
        to_move = result[-1]

        if target == -1:
            return result
        
        if to_move == '.':
            result = result[:-1]
            space_count -= 1
            continue
        
        result = result.replace('.', result[-1], 1)
        result = result[:-1]

        space_count -= 1
    
    return result


if not os.path.isfile(filename):
    print(f'File: {filename} -- Not Found')
    exit()

with open(filename) as filep:
    for line in filep:
        result = 0

        disk_map = line.strip() 

        expanded = expand(disk_map)

        compacted = compact(expanded)

        for idx, n in enumerate(compacted):
            result += idx * int(n)

        print(result)


