import numpy as np
from scipy.ndimage import generic_filter, label
from collections import Counter

with open("09/input.txt") as file:
    lines = file.readlines()
    lines = [list(line.rstrip()) for line in lines]

# PART 1
map = np.array(lines, dtype=int)
footprint = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])

results = generic_filter(
    map,
    lambda values: min(values),
    footprint=footprint,
    mode="constant",
    cval=10,
)

print("Part 1:", np.sum(map[map < results] + 1))


areas = label(map < 9)[0]
largest = Counter(areas.flatten()).most_common(4)[1:]
print(np.prod([v for _, v in largest]))
# largest = Counter(areas.flatten()).most_common(4)[1:]
# print(np.prod([v for _, v in largest]))
