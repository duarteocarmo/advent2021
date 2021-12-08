import numpy as np

with open("07/input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

# PART 1
horizontal_positions = [int(_) for _ in lines[-1].split(",")]
horizontal_positions = np.array(horizontal_positions)


to_diff = np.ones(horizontal_positions.shape) * np.median(horizontal_positions)

print("Target position:", np.median(horizontal_positions))
print("Fuel:", np.sum(np.absolute(horizontal_positions - to_diff)))

# PART 2
calc_cost = np.vectorize(lambda s: np.arange(1, s + 1).sum())
cost_2 = [
    calc_cost(np.abs(horizontal_positions - x)).sum()
    for x in range(np.max(horizontal_positions))
]
print("Fuel:", min(cost_2))
