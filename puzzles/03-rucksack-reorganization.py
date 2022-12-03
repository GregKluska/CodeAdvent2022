import util


# --- Day 3: Rucksack Reorganization ---

# The Elves have made a list of all the items currently in each rucksack (your puzzle input),
# but they need your help finding the errors. Every item type is identified by a single lowercase
# or uppercase letter (that is, a and A refer to different types of items).

# The list of items for each rucksack is given as characters all on a single line.
# A given rucksack always has the same number of items in each of its two compartments,
# so the first half of the characters represent items in the first compartment,
# while the second half of the characters represent items in the second compartment.

def char_to_priority(char):
    priority = ord(char) - 96
    if priority < 1:
        priority += 58
    return priority


def task_rucksack_reorganization_part_1():
    total_priority = 0

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


# For safety, the Elves are divided into groups of three.
# Every Elf carries a badge that identifies their group.
# For efficiency, within each group of three Elves, the badge is the only item type carried by all three Elves.
# That is, if a group's badge is item type B, then all three Elves will have item type B somewhere in their rucksack,
# and at most two of the Elves will be carrying any other item type.

# The problem is that someone forgot to put this year's updated authenticity sticker on the badges.
# All badges need to be pulled out of the rucksacks so the new authenticity stickers can be attached.

# Additionally, nobody wrote down which item type corresponds to each group's badges.
# The only way to tell which item type is the right one is by finding the one item type
# that is common between all three Elves in each group.
def task_rucksack_reorganization_part_2():
    total_priority = 0
    helper = 0
    group_hash_map = {}

    def add_priority(priority):
        nonlocal total_priority
        total_priority += priority

    def find_badge(group):
        for char in group:
            if group[char] == 3:
                return char
        return False

    def process_line(line):
        nonlocal helper, group_hash_map
        hash_map = {}

        # after every 3 lines, add priority bc a new group is coming
        if helper == 3:
            add_priority(char_to_priority(find_badge(group_hash_map)))
            helper = 0
            group_hash_map = {}

        for char in line:
            hash_map[char] = True

        for char in hash_map:
            curr_value = group_hash_map.get(char, 0)
            group_hash_map[char] = curr_value + 1

        helper += 1

    util.read_lines("../resources/03-input.txt", process_line)
    # last case
    add_priority(char_to_priority(find_badge(group_hash_map)))

    print(total_priority)


print("--- Part 1 ---")
task_rucksack_reorganization_part_1()
print("--- Part 2 ---")
task_rucksack_reorganization_part_2()
