import util


# --- Day 1: Calorie Counting ---

# The Elves take turns writing down the number of Calories contained by the various meals,
# snacks, rations, etc. that they've brought with them, one item per line.
# Each Elf separates their own inventory from the previous Elf's inventory (if any) by a blank line.

# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

def task_calorie_counting_part_1():
    max_calories = 0
    curr_calories = 0

    def process_line(line):
        nonlocal max_calories, curr_calories
        if line == "\n":
            max_calories = max(max_calories, curr_calories)
            curr_calories = 0
        else:
            curr_calories += int(line)
        max_calories = max(max_calories, curr_calories)

    util.read_lines("../resources/01-input.txt", process_line)

    print(max_calories)


# Find the top three Elves carrying the most Calories.
# How many Calories are those Elves carrying in total?

def task_calorie_counting_part_2():
    # top 3 elves, descending order
    max_calories = [0, 0, 0]
    curr_calories = 0

    def compare_and_put_in_place(calories):
        nonlocal max_calories

        for i in range(0, len(max_calories)):
            if max_calories[i] < calories:
                max_calories.insert(i, calories)
                del max_calories[-1]
                break

    def process_line(line):
        nonlocal max_calories, curr_calories

        if line == "\n":
            compare_and_put_in_place(curr_calories)
            curr_calories = 0
        else:
            curr_calories += int(line)

    compare_and_put_in_place(curr_calories)
    util.read_lines("../resources/01-input.txt", process_line)

    print(sum(max_calories))


print("--- Part 1 ---")
task_calorie_counting_part_1()
print("--- Part 2 ---")
task_calorie_counting_part_2()
