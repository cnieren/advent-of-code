import os
import string

filename = 'input.txt'
data = []
safeCount = 0

def isSafeReport(report: list[int]):
    asc = sorted(report)
    desc = sorted(report, reverse=True)

    if report == asc:
        for i in range(len(report) - 1):
            delta = report[i+1] - report[i]
            if (delta < 1 or delta > 3):
                return False
    elif report == desc:
        for i in range(len(report) - 1):
            delta = report[i] - report[i+1]
            if (delta < 1 or delta > 3):
                return False
    else:
        return False

    return True

if not os.path.isfile(filename):
    print(f'File: {filename} -- Not Found')
    exit()

with open(filename) as filep:
    for line in filep:
        report = [int(i) for i in line.split()]
        # data.append([isSafeReport(report), report])
        if isSafeReport(report):
            safeCount += 1

print(safeCount)