
with open("in/aoc01.txt", "r") as file:
    inputTxt = file.read()

lines = inputTxt.split("\n")
nums = [int(line) for line in lines]

result = False
for i in range(len(nums)):

    for k in range(i, len(nums)):
        for l in range(k, len(nums)):
            if nums[i] + nums[k] + nums[l] == 2020:
                print("Result: " + str(nums[i] * nums[k] * nums[l]))
                result = True
                break
        if result:
            break
    if result:
        break


