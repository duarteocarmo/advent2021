with open("03/input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


# PART 1
gamma_rate = []
epsilon_rate = []

for position in range(len(lines[0])):
    column_array = []
    for line in lines:
        el = int(line[position])
        column_array.append(el)

    if column_array.count(0) > column_array.count(1):
        most_common = 0
        less_common = 1
    else:
        most_common = 1
        less_common = 0

    gamma_rate.append(most_common)
    epsilon_rate.append(less_common)

gamma_rate = int("".join(str(x) for x in gamma_rate), 2)
epsilon_rate = int("".join(str(x) for x in epsilon_rate), 2)
print(gamma_rate * epsilon_rate)
print("=" * 89)
# PART 2
oxygen_rating = []
co2_rating = []


def find_rating(element, lines):

    if element == "co2":
        preferred = "0"
    if element == "o2":
        preferred = "1"

    position_tracker = len(lines[0])
    for position_tracker in range(len(lines[0])):
        elements = [int(number[position_tracker]) for number in lines]

        if elements.count(0) > elements.count(1):
            most_common = "0"
            less_common = "1"

        if elements.count(0) < elements.count(1):
            most_common = "1"
            less_common = "0"

        if elements.count(0) == elements.count(1):
            most_common = "1"
            less_common = "0"

        if element == "o2":
            lines = [el for el in lines if el[position_tracker] == most_common]

        if element == "co2":
            lines = [el for el in lines if el[position_tracker] == less_common]

        if len(lines) == 1:
            return int(lines[-1], 2)


o2_rating = find_rating(element="o2", lines=lines)
print(o2_rating)
co2_rating = find_rating(element="co2", lines=lines)
print(co2_rating)
print(co2_rating * o2_rating)
# print(o2_rating * co2_rating)

# for position in range(len(lines[0])):
#     column_array = []
#     for line in lines:
#         el = int(line[position])
#         column_array.append(el)

#     if column_array.count(0) >column_array.count(1):
#         most_common = 0
#         less_common = 1
#     else:
#         most_common = 1
#         less_common = 0

#     gamma_rate.append(most_common)
#     epsilon_rate.append(less_common)

# gamma_rate = int(''.join(str(x) for x in gamma_rate), 2)
# epsilon_rate = int(''.join(str(x) for x in epsilon_rate), 2)
# print(gamma_rate* epsilon_rate)
