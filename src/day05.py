from math import ceil, floor


def load_data():
    with open("../in/aoc05.txt", "r") as file:
        in_text = file.read()

    return in_text.split("\n")


def part_one():
    seats = load_data()
    max_id = 0
    for seat in seats:
        row_l = 0
        row_u = 127
        for char in seat[:7]:
            if char == "B":
                row_l = ceil((row_u + row_l) / 2)
            if char == "F":
                row_u = floor((row_u + row_l) / 2)
            # print(char + ":" + str(row_l) + "-" + str(row_u))
        row = row_l
        col_l = 0
        col_u = 7
        for char in seat[-3:]:
            if char == "L":
                col_u = floor((col_l + col_u) / 2)
            if char == "R":
                col_l = ceil((col_l + col_u) / 2)
        col = col_u
        row_id = row * 8 + col
        if row_id > max_id:
            max_id = row_id

    return max_id


def part_two():
    seats = load_data()
    ids = []
    for seat in seats:
        row_l = 0
        row_u = 127
        for char in seat[:7]:
            if char == "B":
                row_l = ceil((row_u + row_l) / 2)
            if char == "F":
                row_u = floor((row_u + row_l) / 2)
            # print(char + ":" + str(row_l) + "-" + str(row_u))
        row = row_l
        col_l = 0
        col_u = 7
        for char in seat[-3:]:
            if char == "L":
                col_u = floor((col_l + col_u) / 2)
            if char == "R":
                col_l = ceil((col_l + col_u) / 2)
        col = col_u
        row_id = row * 8 + col
        ids.append(row_id)

    my_id = 0
    ids.sort()
    for i in range(len(ids) - 1):
        first = ids[i]
        second = ids[i+1]
        if second == first + 2:
            my_id = second - 1
            break
    return my_id


print(part_two())
