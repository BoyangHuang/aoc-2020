grid = []
with open("path.txt", mode="r", newline="\n") as f:
    for line in f.readlines():
        grid.append(line.replace("\n", ""))

to_test = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
ret = []
max_len = len(grid[0])

for step in to_test:
    right, down = step
    trees_hit = 0
    current_idx = right
    go_down = 0
    for i, row in enumerate(grid):
        if i == 0:
            continue
        if go_down < down - 1:
            go_down += 1
            continue

        go_down = 0
        try:
            letter = row[current_idx]
        except IndexError:
            current_idx = abs(max_len - current_idx)
            letter = row[current_idx]

        if letter == "#":
            trees_hit += 1
        current_idx += right
    ret.append(trees_hit)

import math
print(math.prod(ret))