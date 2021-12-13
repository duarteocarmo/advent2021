import numpy as np
import random

with open("13/input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

positions = []
max_x = 0
max_y = 0
folds = []

for line in lines:
    if line == "":
        continue
    if "fold" in line:
        folds.append(line)
        continue
    x, y = line.split(",")
    positions.append((int(x), int(y)))
    max_x = max(max_x, int(x))
    max_y = max(max_y, int(y))

print(positions)
map = np.zeros((max_y + 1, max_x + 1))

for position in positions:
    map[position[1], position[0]] = 1

print(folds)
print(map)
# np.split(map, [7], axis=0)[1]

result = map
for fold in folds:
    print(fold)
    unit = int(fold.split("=")[-1])
    if "y" in fold:
        part_1 = result[0:unit, :]
        part_2 = np.flip(result[unit + 1:, :], axis=0)
    else:
        part_1 = result[:, 0:unit]
        part_2 = np.flip(result[:, unit + 1:], axis=1)

    result = part_1 + part_2
    print(result)
    print(result[result>0].shape[0])





