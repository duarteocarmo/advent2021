import numpy as np

with open("05/input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


# PART 1
matrix_size = 0
for line in lines:
    start, end = line.split("->")
    x1, y1 = [int(_) for _ in start.split(",")]
    x2, y2 = [int(_) for _ in end.split(",")]
    max_of_input = max(x1, y1, x2, y2)
    if max_of_input > matrix_size:
        matrix_size = max_of_input

matrix = np.zeros((matrix_size + 1, matrix_size + 1))

for line in lines:
    start, end = line.split("->")
    x1, y1 = [int(_) for _ in start.split(",")]
    x2, y2 = [int(_) for _ in end.split(",")]

    # FOR PART 1
    if x1 == x2:
        print(x1, y1, "->", x2, y2)
        matrix[x1, min(y1, y2) : max(y1, y2) + 1] += 1

    elif y1 == y2:
        print(x1, y1, "->", x2, y2)
        matrix[min(x1, x2) : max(x1, x2) + 1, y1] += 1

    # ONLY FOR PART 2
    elif abs(x1 - x2) == abs(y1 - y2):
        print("====")
        print(x1, y1, "->", x2, y2)

        if x2 > x1 and y2 > y1:
            y_pos = y1
            for x in range(x1, x2 + 1):
                print(x, y_pos)
                matrix[x, y_pos] += 1
                y_pos += 1

        if x2 > x1 and y2 < y1:
            y_pos = y1
            for x in range(x1, x2 + 1):
                print(x, y_pos)
                matrix[x, y_pos] += 1
                y_pos -= 1

        if x2 < x1 and y2 > y1:
            y_pos = y2
            for x in range(x2, x1 + 1):
                print(x, y_pos)
                matrix[x, y_pos] += 1
                y_pos -= 1

        if x2 < x1 and y2 < y1:
            y_pos = y2
            for x in range(x2, x1 + 1):
                print(x, y_pos)
                matrix[x, y_pos] += 1
                y_pos += 1

        print("====")
    else:
        continue

matrix = matrix.transpose()
print(matrix)
print(matrix[matrix >= 2].shape[-1])
