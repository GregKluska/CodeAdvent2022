import util


# --- Day 3: Rucksack Reorganization ---

# The Elves have made a list of all the items currently in each rucksack (your puzzle input),
# but they need your help finding the errors. Every item type is identified by a single lowercase
# or uppercase letter (that is, a and A refer to different types of items).

# The list of items for each rucksack is given as characters all on a single line.
# A given rucksack always has the same number of items in each of its two compartments,
# so the first half of the characters represent items in the first compartment,
# while the second half of the characters represent items in the second compartment.

def task_rucksack_reorganization_part_1():
    total_priority = 0

    def char_to_priority(char):
        priority = ord(char) - 96
        if priority < 1:
            priority += 58
        return priority

    def process_line(line):
        nonlocal total_priority
        hash_map = {}
        second_compartment_map = {}
        first_compartment, second_compartment = line[:len(line) // 2], line[len(line) // 2:]

        for char in first_compartment:
            priority = char_to_priority(char)
            hash_map[priority] = True

        for char in second_compartment:
            priority = char_to_priority(char)
            if hash_map.get(priority, False) is True and second_compartment_map.get(priority, False) is False:
                second_compartment_map[priority] = True
                total_priority += priority

    util.read_lines("../resources/03-input.txt", process_line)

    print(total_priority)


print("--- Part 1 ---")
task_rucksack_reorganization_part_1()
print("--- Part 2 ---")
# task_rock_paper_scissors_part_2()
