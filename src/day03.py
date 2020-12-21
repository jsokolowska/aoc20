with open("../in/aoc03.txt", "r") as file:
    inputText = file.read()

tree = "#"
lines = inputText.split("\n")
height = len(lines)
width = len(lines[0])
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
results = []

for slope in slopes:
    x = 0
    y = 0
    trees = 0
    while y < height:
        if lines[y][x] == tree:
            trees += 1
        y += slope[1]
        x = (slope[0] + x) % width
    results.append(trees)

mult = 1
for num in results:
    mult *= num
print(mult)


