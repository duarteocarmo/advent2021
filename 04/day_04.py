with open("04/input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

# PART 1

bingo_numbers = [int(_) for _ in lines[0].split(",")]
matrixes = []
matrix = []

for line in lines[1:]:
    if line == "":
        matrix = []
        matrixes.append(matrix)
    else:
        numbrers = [int(_) for _ in line.split(" ") if _ != ""]
        matrix.append(numbrers)


boards = matrixes
complete_boards = []

for board in boards:
    columns = []
    for i in range(5):
        column = [row[i] for row in board]
        columns.append(column)
    complete_boards.append(board + columns)

winner = False
list_to_check = bingo_numbers[:5]
up_to = 4


for i in range(5, len(bingo_numbers)):
    list_to_check = bingo_numbers[0:i]
    win_status = [False for board in complete_boards]
    win_index = 0

    for index, complete_board in enumerate(complete_boards):
        for r_o_c in complete_board:
            winner = all(number in list_to_check for number in r_o_c)
            winner_board = complete_board
            # print(r_o_c)
            # print(list_to_check)
            # print(winner)
            if winner:
                win_status[index] = True
                win_index = index
                break
            # print("=" * 90)
    print("W", win_status.count(True))
    print("L", win_status.count(False))
    if win_status.count(False) == 1:
        print(win_status)
        print(win_status.index(False))
        break
    print("-----")

    # print(list_to_check)
    # print(win_status)
    if win_status.count(True) == len(win_status):
        print(f"The last winner is board: {win_index}, in {len(win_status)}")
        break

list_to_check = bingo_numbers[0: i + 1]
winner_board = complete_boards[win_status.index(False)]
print(f"LIST TO CHECK", list_to_check)
print(f"WINNER COMBO: {r_o_c}")
print(f"LAST WINNER:{winner_board}")
rows = winner_board[0:5]
flatten_numbers = [item for sublist in rows for item in sublist]
unmarked_nunbers = [
    number for number in flatten_numbers if number not in list_to_check
]
print(f"UNMARKED:{unmarked_nunbers}")
print(sum(unmarked_nunbers) * list_to_check[-1])
