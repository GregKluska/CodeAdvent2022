import util
import copy


# --- Day 11: Monkey in the Middle ---

class Monkey:
    id = -1
    items = []
    operation = None
    test = -1
    if_true = -1
    if_false = -1
    inspected = 0


def task_monkey_in_the_middle_part_1():
    monkeys = []

    curr_monkey = Monkey()

    def process_line(raw_line):
        nonlocal monkeys, curr_monkey

        line = raw_line.strip()
        if line == "":
            monkeys.append(copy.deepcopy(curr_monkey))
            curr_monkey = Monkey()
        elif line.startswith("Monkey "):
            nums = [int(x.replace(":", "")) for x in line.split() if x.replace(":", "").isdigit()]
            curr_monkey.id = nums[0]
        elif line.startswith("Starting items: "):
            nums = [int(x.replace(",", "")) for x in line.split() if x.replace(",", "").isdigit()]
            curr_monkey.items = nums
        elif line.startswith("Operation: new ="):
            arr = line.split()[-2::]
            if arr[1] == "old":
                if arr[0] == "+":
                    curr_monkey.operation = lambda x: x + x
                else:
                    curr_monkey.operation = lambda x: x * x
            else:
                if arr[0] == "+":
                    curr_monkey.operation = lambda x: x + int(arr[1])
                else:
                    curr_monkey.operation = lambda x: x * int(arr[1])
        elif line.startswith("Test: divisible by "):
            nums = [int(x) for x in line.split() if x.isdigit()]
            curr_monkey.test = nums[0]
        elif line.startswith("If true"):
            nums = [int(x) for x in line.split() if x.isdigit()]
            curr_monkey.if_true = nums[0]
        elif line.startswith("If false"):
            nums = [int(x) for x in line.split() if x.isdigit()]
            curr_monkey.if_false = nums[0]

    util.read_lines("../resources/11-input.txt", process_line)
    monkeys.append(copy.deepcopy(curr_monkey))

    print()
    for rnd in range(1, 21):
        print("Round " + str(rnd))
        for monkey in monkeys:
            print()
            print("Monkey %i:" % monkey.id)
            for item in monkey.items:
                print("+Monkey inspects an item with a worry level of %i." % item)
                item = monkey.operation(item)
                monkey.inspected += 1
                print("+-Worry level is raised to %i." % item)
                item = int(item / 3)
                print("+-Monkey gets bored with item. Worry level is divided by 3 to %i." % item)
                if item % monkey.test == 0:
                    print("+-Current worry level is divisible by %i." % monkey.test)
                    monkeys[monkey.if_true].items.append(item)
                else:
                    print("+-Current worry level is not divisible by %i." % monkey.test)
                    monkeys[monkey.if_false].items.append(item)
            monkey.items = []

    max_three = []
    for monk in monkeys:
        print("Monkey %i inspected items %i times." % (monk.id, monk.inspected))
        max_three.append(monk.inspected)
    max_three.sort()
    print(max_three[-2::][0] * max_three[-2::][1])


def task_monkey_in_the_middle_part_2():
    monkeys = []

    curr_monkey = Monkey()

    def process_line(raw_line):
        nonlocal monkeys, curr_monkey

        line = raw_line.strip()
        if line == "":
            monkeys.append(copy.deepcopy(curr_monkey))
            curr_monkey = Monkey()
        elif line.startswith("Monkey "):
            nums = [int(x.replace(":", "")) for x in line.split() if x.replace(":", "").isdigit()]
            curr_monkey.id = nums[0]
        elif line.startswith("Starting items: "):
            nums = [int(x.replace(",", "")) for x in line.split() if x.replace(",", "").isdigit()]
            curr_monkey.items = nums
        elif line.startswith("Operation: new ="):
            arr = line.split()[-2::]
            if arr[1] == "old":
                if arr[0] == "+":
                    curr_monkey.operation = lambda x: x + x
                else:
                    curr_monkey.operation = lambda x: x * x
            else:
                if arr[0] == "+":
                    curr_monkey.operation = lambda x: x + int(arr[1])
                else:
                    curr_monkey.operation = lambda x: x * int(arr[1])
        elif line.startswith("Test: divisible by "):
            nums = [int(x) for x in line.split() if x.isdigit()]
            curr_monkey.test = nums[0]
        elif line.startswith("If true"):
            nums = [int(x) for x in line.split() if x.isdigit()]
            curr_monkey.if_true = nums[0]
        elif line.startswith("If false"):
            nums = [int(x) for x in line.split() if x.isdigit()]
            curr_monkey.if_false = nums[0]

    util.read_lines("../resources/11-input.txt", process_line)
    monkeys.append(copy.deepcopy(curr_monkey))

    max_stress = 1
    for monkey in monkeys:
        max_stress = monkey.test * max_stress

    print()
    for rnd in range(1, 10001):
        for monkey in monkeys:
            for item in monkey.items:
                item = monkey.operation(item) % max_stress
                monkey.inspected += 1
                if item % monkey.test == 0:
                    monkeys[monkey.if_true].items.append(item)
                else:
                    monkeys[monkey.if_false].items.append(item)
            monkey.items = []

    max_three = []
    for monk in monkeys:
        print("Monkey %i inspected items %i times." % (monk.id, monk.inspected))
        max_three.append(monk.inspected)
    max_three.sort()
    print(max_three[-2::][0] * max_three[-2::][1])


print("--- Part 1 ---")
task_monkey_in_the_middle_part_1()
print("--- Part 2 ---")
task_monkey_in_the_middle_part_2()
