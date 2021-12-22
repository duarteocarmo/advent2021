import re
from collections import Counter


def read_input_file(file):
    with open(file, "r") as fpr:
        content = fpr.read()
        return content


def day_22_puzzle_1(file, limit=True):
    content = read_input_file(file)

    pattern = re.compile(
        r"(?P<action>(on|off)) "
        r"x=(?P<x_start>-*\d+)..(?P<x_stop>-*\d+),"
        r"y=(?P<y_start>-*\d+)..(?P<y_stop>-*\d+),"
        r"z=(?P<z_start>-*\d+)..(?P<z_stop>-*\d+)"
    )

    cubes = {}
    found = pattern.finditer(content)
    for i, f in enumerate(found):
        action = 1 if f.group("action") == "on" else 0
        x_start, x_stop = int(f.group("x_start")), int(f.group("x_stop"))
        y_start, y_stop = int(f.group("y_start")), int(f.group("y_stop"))
        z_start, z_stop = int(f.group("z_start")), int(f.group("z_stop"))

        if limit:
            x_start = -50 if x_start <= -50 else x_start
            y_start = -50 if y_start <= -50 else y_start
            z_start = -50 if z_start <= -50 else z_start

            x_stop = 50 if x_stop >= 50 else x_stop
            y_stop = 50 if y_stop >= 50 else y_stop
            z_stop = 50 if z_stop >= 50 else z_stop

        for x in range(x_start, x_stop + 1):
            for y in range(y_start, y_stop + 1):
                for z in range(z_start, z_stop + 1):
                    if (x, y, z) not in cubes:
                        cubes[(x, y, z)] = 0
                    cubes[(x, y, z)] = action

    print(f"Answer: {Counter(cubes.values())}")


if __name__ == "__main__":
    file = "22/input.txt"
    day_22_puzzle_1(file)
