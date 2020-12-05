"""
    author: Joanna Sokołowska - https://github.com/jsokolowska
 """

with open("../in/aoc02.txt", "r") as file:
    lines = file.read().split("\n")

right_passwords = 0
for line in lines:
    parts = line.split(" ")
    limits = parts[0].split("-")
    letter = parts[1][0]
    password = parts[2]
    one = password[int(limits[0]) - 1]
    two = password[int(limits[1]) - 1]
    if (one == letter) != (two == letter):
        right_passwords += 1

print(right_passwords)
