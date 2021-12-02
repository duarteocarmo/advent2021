with open("02/input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

depth = 0
horizontal_pos = 0

# PART 1
for line in lines:
    movement, quantity = line.split(" ")
    quantity = int(quantity)

    if movement == "forward":
        horizontal_pos = horizontal_pos + quantity

    if movement == "down":
        depth = depth + quantity

    if movement == "up":
        depth = depth - quantity

print(f"Depth: {depth}; Horizontal Position: {horizontal_pos}")
print(f"Result: {depth * horizontal_pos}")

depth = 0
horizontal_pos = 0
aim = 0

# PART 2
for line in lines:
    movement, quantity = line.split(" ")
    quantity = int(quantity)

    if movement == "forward":
        horizontal_pos = horizontal_pos + quantity
        depth = depth + (aim * quantity)

    if movement == "down":
        aim = aim + quantity

    if movement == "up":
        aim = aim - quantity

print(f"Depth: {depth}; Horizontal Position: {horizontal_pos}")
print(f"Result: {depth * horizontal_pos}")
