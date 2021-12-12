import numpy as np
import random

with open("12/test_input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

neighboors = dict()

for line in lines:
    p1, p2 = line.split("-")
    if p1 not in neighboors.keys():
        neighboors[p1] = list()
    if p2 not in neighboors.keys():
        neighboors[p2] = list()
    neighboors[p1].append(p2)
    neighboors[p2].append(p1)


paths = []

TOTAL_LOOPS = 10_000_000

for i in range(TOTAL_LOOPS):
    path = ["start"]
    while path[-1] != "end":
        excluded = [el for el in path if el.islower()]
        possible = list(set(neighboors[path[-1]]) - set(excluded))
        if len(possible) == 0:
            path = ["start"]
            continue
        # print("->", excluded, possible)
        path.append(random.choice(possible))

    if path not in paths:
        paths.append(path)

    print(f"Loop {i}/{TOTAL_LOOPS} - combinations: {len(paths)}")

print(len(paths))
