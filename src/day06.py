def load_data ():
    with open("../in/aoc06.txt", "r") as file:
        text = file.read()
    lines = text.split("\n")
    groups = []
    current = ""
    for line in lines:
        if not len(line):
            groups.append(current)
            current = ""
        else:
            current = current + line + " "
    groups.append(current)
    return groups


def part_one():
    groups = load_data()
    c_sum = 0
    for group in groups:
        questions = set(group)
        c_sum += len(questions) - 1   # substract whitespace
    return c_sum


def part_two():
    groups = load_data()
    c_sum = 0
    for group in groups:
        people = group.split(" ")
        common = set(people[0])
        for i in range(len(people) - 2):
            next = people[i+1]
            common = common.intersection(next)
        c_sum += len(common)
    return c_sum


print(part_two())
