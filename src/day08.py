def load_data():
    with open("../in/aoc08.txt", "r") as file:
        text = file.read()
    return text.split("\n")


def part_one():
    instructions = load_data()
    in_point = 0
    visited = set()
    acc = 0
    second_visit = False
    while not second_visit:
        if in_point in visited:
            return acc
        else:
            visited.add(in_point)
        instr = instructions[in_point]
        ops = instr.split(" ")
        command = ops[0]
        arg = int(ops[1])
        if command == "nop":
            in_point += 1
        elif command == "acc":
            acc += arg
            in_point += 1
        elif command == "jmp":
            in_point += arg


def part_two():
    i_copy = load_data()
    for i in range(len(i_copy)):
        in_point = 0
        visited = set()
        acc = 0
        second_visit = False
        instructions = i_copy[:]
        instr = instructions[i].split(" ")
        if instr[0] == "nop":
            instr[0] = "jmp"
            instructions[i] = " ".join(instr)
        elif instr[0] == "jmp":
            instr[0] = "nop"
            instructions[i] = " ".join(instr)
        else:
            continue
        while not second_visit:
            if in_point == len(instructions):
                print("found: " + str(acc))
                return acc
            if in_point in visited:
                break
            else:
                visited.add(in_point)
            instr = instructions[in_point]
            ops = instr.split(" ")
            command = ops[0]
            arg = int(ops[1])
            if command == "nop":
                in_point += 1
            elif command == "acc":
                acc += arg
                in_point += 1
            elif command == "jmp":
                in_point += arg
    print("Fail")
    return -1


res = part_two()
print(str(res))
