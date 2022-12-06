import util


# --- Day 6: Tuning Trouble ---

def task_tuning_trouble(distinct):
    hashset = set()
    marker_at = 0
    position = 0

    def process_line(line):
        nonlocal hashset, marker_at, position
        for i in range(0, len(line)):
            if line[i] in hashset:
                helper = 0
                for x in range(marker_at, marker_at + distinct):
                    helper += 1
                    hashset.remove(line[x])
                    if line[x] == line[i]:
                        break
                marker_at += helper
            hashset.add(line[i])
            if len(hashset) == distinct:
                position = i + 1
                return

    util.read_lines("../resources/06-input.txt", process_line)
    print(position)


def task_tuning_trouble_part_1():
    task_tuning_trouble(4)


def task_tuning_trouble_part_2():
    task_tuning_trouble(14)


print("--- Part 1 ---")
task_tuning_trouble_part_1()
print("--- Part 2 ---")
task_tuning_trouble_part_2()
