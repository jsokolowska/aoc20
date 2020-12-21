import re


def load_data():
    with open("../in/aoc04.txt", "r") as file:
        text = file.read()
    lines = text.split("\n")
    passports = []
    curr_pass = ""
    for line in lines:
        if not len(line):
            passports.append(curr_pass)
            curr_pass = ""
        else:
            curr_pass = curr_pass + line + " "
    passports.append(curr_pass)
    return passports


def part_one():
    passports = load_data()
    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    valid_num = 0
    for passport in passports:
        fields = set([x[0:3] for x in passport.split(" ")])
        if required_fields.issubset(fields):
            valid_num += 1
    return valid_num


def part_two():
    passports = load_data()
    byr = "byr:[0-9]{4} "
    iyr = "iyr:[0-9]{4} "
    eyr = "eyr:[0-9]{4} "
    hgt = "hgt:[0-9]*(cm|in) "
    hcl = "hcl:#[0-9a-f]{6} "
    ecl = "ecl:(amb|blu|brn|gry|grn|hzl|oth) "
    pid = "pid:[0-9]{9} "
    valid_num = 0
    for i in range(len(passports)):
        entry = passports[i]
        match_byr = re.search(byr, entry)
        match_iyr = re.search(iyr, entry)
        match_eyr = re.search(eyr, entry)
        match_hgt = re.search(hgt, entry)
        match_hcl = re.search(hcl, entry)
        match_ecl = re.search(ecl, entry)
        match_pid = re.search(pid, entry)
        fulfilled = 0
        if match_byr:
            val = int(match_byr.group()[-5:])
            if 1920 <= val <= 2002:
                fulfilled += 1
        if match_iyr:
            val = int(match_iyr.group()[-5:])
            if 2010 <= val <= 2020:
                fulfilled += 1
        if match_eyr:
            val = int(match_eyr.group()[-5:-1])
            if 2020 <= val <= 2030:
                fulfilled += 1
        if match_hgt:
            unit = match_hgt.group()[-3:-1]
            string = re.search(":[0-9]+[i|c]", match_hgt.group())
            val = int(string.group()[1:-1])
            if (unit == "in" and 59 <= val <= 76) or (unit == "cm" and 150 <= val <= 193):
                fulfilled += 1
        if match_hcl:
            fulfilled += 1
        if match_ecl:
            fulfilled += 1
        if match_pid:
            fulfilled += 1
        if fulfilled == 7:
            valid_num += 1

    return valid_num


print(part_two())
