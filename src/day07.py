import re


def load_data():
    with open("../in/aoc07.txt", "r") as file:
        text = file.read()
    return text


def part_one():
    lines = load_data().split("\n")
    my_bag = "shiny gold bag"
    bags = {my_bag}
    curr = bags
    new_bags = set()
    found = True
    temp_lines = []
    line_match = False
    while found:
        found = False
        for line in lines:
            for bag in curr:
                reg = "contain.*" + bag
                match = re.search(reg, line)
                if match:
                    new_bag = " ".join(line.split(" ")[:2]) + " bag"
                    new_bags.add(new_bag)
                    line_match = True
                    found = True
                    break
            if not line_match:
                temp_lines.append(line)
            line_match = False
        bags = bags | curr
        curr = new_bags
        new_bags = set()
        lines = temp_lines
        temp_lines = []
    bags.remove(my_bag)
    return bags


def part_two():
    text = load_data()

    def how_many_bags(color):
        reg = color + " bags contain no other bags."
        match = re.search(reg, text)
        if match:
            return 0
        else:
            reg = color + ".* contain.*\n"
            match = re.search(reg, text)
            line = match.group()
            line = " ".join(line.split(" ")[4:])
            bags = line.split(", ")
            res = 0
            for bag in bags:
                parts = bag.split(" ")
                num = int(parts[0])
                new_color = parts[1] + " " + parts[2]
                res += num * (how_many_bags(new_color) + 1)
            return res

    my_bag = "shiny gold bag"
    return how_many_bags(my_bag)


res = part_two()
print("Result: ")

print(res)
