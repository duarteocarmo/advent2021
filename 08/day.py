with open("08/input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

# unique_segments = {
#     1: 2,
#     4: 4,
#     7: 3,
#     8: 7,
# }

unique_segments = [2, 4, 3, 7]
counter = 0


# PART 1
output_list = [
    line.split("|")[-1].rstrip().lstrip().split(" ") for line in lines
]

for output in output_list:
    for combination in output:
        if len(list(set(list(combination)))) in unique_segments:
            counter += 1


print(counter)
