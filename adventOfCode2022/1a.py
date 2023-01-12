"""
Day One (Calorie Counting) - Part 1
https://adventofcode.com/2022/day/1
"""


with open("inputs/1a.txt", "r") as f:
    calories_list = f.read().splitlines()
    max_calories = 0
    current_calories = 0
    for item in calories_list:
        if item == "":
            current_calories = 0
        else:
            current_calories += int(item)
            max_calories = max(max_calories, current_calories)

    print(max_calories)
