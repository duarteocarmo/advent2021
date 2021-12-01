with open("01/input.txt") as file:
    lines = file.readlines()
    lines = [int(line.rstrip()) for line in lines]


# PART 1
increases = 0
for index, value in enumerate(lines):

    if index == len(lines) - 1:
        break
    next_value = lines[index + 1]

    if next_value > value:
        text = "increase"
        increases = increases + 1

print(increases)

# PART 2
previous_sum = 99999999999999999999
sum_increases = 0
for index, value in enumerate(lines):

    if index == len(lines) - 1:
        break

    first = lines[index - 1]
    mid = lines[index]
    next = lines[index + 1]
    current_sum = first + mid + next
    if current_sum > previous_sum:
        sum_increases = sum_increases + 1

    previous_sum = current_sum

print(sum_increases)
