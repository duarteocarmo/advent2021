import numpy as np
from scipy.ndimage import generic_filter

with open("11/test_input.txt") as file:
    lines = file.readlines()
    lines = [list(line.rstrip()) for line in lines]

matrix = np.array(lines, dtype=int)
footprint = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])


def function(values):
    return (values > 9).sum() - (values[4] > 9)



increment = matrix + 1
zeros = np.zeros_like(matrix)

while True:
    results = generic_filter(
        increment,
        function,
        footprint=footprint,
        mode="constant",
        cval=10,
    )
    flashes = zeros + (matrix > 9)
    matrix[flashes] = 0
    matrix = results + matrix
    if results.sum() == 0:
        break


print(results)
