from typing import Any
import numpy as np
from collections import Counter

with open("14/input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

pairs = dict()
original = ""


def flatten(t):
    return [item for sublist in t for item in sublist]


for line in lines:

    if line == "":
        continue

    elif "->" in line:
        pair, rule = line.split(" -> ")
        pairs[pair] = rule

    else:
        original = list(line)

print(original)
print(pairs)


TOTAL_STEPS = 100

for step in range(1, TOTAL_STEPS):

    next_original = original

    list_of_pairs = [
        [original[i], original[i + 1]] for i in range(len(original) - 1)
    ]
    new_pairs = []


    for pair in list_of_pairs:
        pair_string = "".join(pair)

        if pair_string in pairs.keys():
            pair.insert(1, pairs[pair_string])
            new_pairs.append(pair)

        else:
            new_pairs.append(pair)

    last_letter = new_pairs[-1][-1]
    new_pairs = [_[0:2] for _ in new_pairs]
    new_pairs = flatten(new_pairs) 
    new_pairs.append(last_letter)
    original = new_pairs
    size = len(original)
    print(f"Step {step} ({size}) : {original}")

    # PART 1
    # if step == 10:
    #     break

    # PART 2
    if step == 40:
        break

    print("=" * 89, step)

c = Counter(original)
common = c.most_common()
most = common[0][1]
less = common[-1][1]
print(most - less)



