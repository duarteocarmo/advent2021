with open("10/test_input.txt") as file:
    lines = file.readlines()
    lines = [list(line.rstrip()) for line in lines]

pairs = [
    ["(", ")"],
    ["[", "]"],
    ["<", ">"],
    ["{", "}"],
]
openers = [_[0] for _ in pairs]
closers = [_[1] for _ in pairs]

points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

reversers = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

# PART 1
line = lines[0]
il_list = []

for line in lines:
    print(line)
    while True:
        change = False
        for i in range(len(line) - 1):
            if [line[i], line[i + 1]] in pairs:
                del line[i : i + 2]
                change = True
                break

        if change == False:
            # PART 1
            if not all(el in openers for el in line):
                illegal = [el for el in line if el in closers][0]
                il_list.append(illegal)
            # PART 2
            else:
                print(line)
                reverse = [reversers[x] for x in line]
                print(reverse)
            break
    print("=" * 89)

print(il_list)
print(sum(points[x] for x in il_list))
