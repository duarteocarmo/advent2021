import numpy as np

with open("06/input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


# PART 1
list_of_ages = [int(_) for _ in lines[-1].split(",")]
total_days = 80
initial_state = list_of_ages

for n_day in range(0, total_days + 1):
    # print(f"After day {n_day} ({len(initial_state)}): {initial_state}")
    print(f"After day {n_day} ({len(initial_state)})")
    to_create = 0
    for i in range(len(initial_state)):
        if initial_state[i] == 0:
            initial_state[i] = 7
            to_create += 1

        initial_state[i] -= 1

    initial_state += [8] * to_create

    print("=" * 89)

