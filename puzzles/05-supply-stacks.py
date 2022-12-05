import util


# --- Day 5: Supply Stacks ---

# The ship has a giant cargo crane capable of moving crates between stacks.
# To ensure none of the crates get crushed or fall over,
# the crane operator will rearrange them in a series of carefully-planned steps.
# After the crates are rearranged, the desired crates will be
# at the top of each stack.

# The Elves don't want to interrupt the crane operator during this delicate
# procedure, but they forgot to ask her which crate will end up where,
# and they want to be ready to unload them as soon as possible, so they can embark.

def task_supply_stack(part):
    reading_stacks = True
    stacks = []

    def process_stacks_line(line):
        nonlocal reading_stacks, stacks

        if line[1] == "1":
            reading_stacks = False
            return

        crates = [line[idx:idx + 4] for idx in range(0, len(line), 4)]

        if len(stacks) == 0:  # stacks not initialised
            for x in range(0, len(crates)):
                stacks.append([])

        for idx in range(0, len(crates)):
            content = crates[idx][1]
            if content == " ":
                continue
            stacks[idx].append(content)

    def process_instruction_line(line):
        nonlocal stacks, part

        instructions = line.split(" ")
        move_count = int(instructions[1])
        move_from = int(instructions[3]) - 1
        move_to = int(instructions[5]) - 1

        for idx in range(0, move_count):
            if part == 2:
                stacks[move_to].insert(idx, stacks[move_from].pop(0))
            else:
                stacks[move_to].insert(0, stacks[move_from].pop(0))

    def is_instruction(line):
        return line.startswith("move")

    def process_line(line):
        nonlocal reading_stacks

        if reading_stacks:
            process_stacks_line(line)
        elif is_instruction(line):
            process_instruction_line(line)

    util.read_lines("../resources/05-input.txt", process_line)

    message = ""
    for i in range(0, len(stacks)):
        message = message + stacks[i][0]
    print(message)


# one at time

def task_supply_stack_part_1():
    task_supply_stack(1)


# The CrateMover 9001 is notable for many new and exciting
# features: air conditioning, leather seats, an extra cup
# holder, and the ability to pick up and move
# multiple crates at once.

def task_supply_stack_part_2():
    task_supply_stack(2)


print("--- Part 1 ---")
task_supply_stack_part_1()
print("--- Part 2 ---")
task_supply_stack_part_2()
