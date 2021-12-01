import sys

with open("01/input.txt") as file:
    lines = file.readlines()
    lines = [int(line.rstrip()) for line in lines]

increases = 0

for index, value in enumerate(lines):

    value = value

    if index == len(lines) - 1:
        break
    next_value = lines[index + 1]

    if next_value > value:
        text = "increase"
        increases = increases + 1

print(increases)
