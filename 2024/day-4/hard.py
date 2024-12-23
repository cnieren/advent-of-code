import os
import re

filename = 'input.txt'
board = []

if not os.path.isfile(filename):
    print(f'File: {filename} -- Not Found')
    exit()

with open(filename) as filep:
    for line in filep:
        # Read file here
        board.append(list(line.strip()))

count = 0
rows, cols = len(board), len(board[0])
legs = {"M", "S"}

for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        if board[i][j] == "A":
            if {board[i - 1][j - 1], board[i + 1][j + 1]} == legs and {board[i - 1][j + 1], board[i + 1][j - 1]} == legs:
                count += 1

print(count)