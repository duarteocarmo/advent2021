import itertools

# test_input = "target area: x=20..30, y=-10..-5"
test_input = "target area: x=277..318, y=-92..-53"
xmin, xmax = [
    int(_) for _ in test_input.split(",")[0].split("=")[1].split("..")
]
ymin, ymax = [
    int(_) for _ in test_input.split(",")[1].split("=")[1].split("..")
]


def get_max_height(velocity_x, velocity_y):
    # print(f"Velocity pair: ({velocity_x}, {velocity_y})")
    x, y = (0, 0)
    max_height = y

    while x < xmax or y > ymin:
        x += velocity_x
        y += velocity_y
        max_height = max(max_height, y)
        # print(f"x:{x}; y:{y} (max height: {max_height})")

        if x in range(xmin, xmax + 1) and y in range(ymin, ymax + 1):
            return max_height

        if velocity_x > 0:
            velocity_x -= 1
        else:
            velocity_x += 1

        velocity_y -= 1

    return None


list_possible_x = list(range(1, 5000))
list_possible_y = list(range(-100, 100))
best_coordinates = (0, 0)
best_height = 0

for velocity_pair in itertools.product(list_possible_x, list_possible_y):
    height = get_max_height(*velocity_pair)

    if height:
        if height > best_height:
            best_height = height
            best_coordinates = velocity_pair

print(best_height, best_coordinates)
