from ast import literal_eval
from functools import cmp_to_key


# --- Day 13: Distress Signal ---

def compare_lists(a, b):
    if type(a) is list and type(b) is int:
        b = [b]
    if type(a) is int and type(b) is list:
        a = [a]
    if type(a) is int and type(b) is int:
        if a < b:
            return 1
        elif a == b:
            return 0
        else:
            return -1
    if type(a) is list and type(b) is list:
        i, j = 0, 0
        while i < len(a) and j < len(b):
            res = compare_lists(a[i], b[j])

            match res:
                case 1:
                    return 1
                case -1:
                    return -1

            i += 1
            j += 1

        if i == len(a):
            if j == len(b):
                return 0
            return 1

        if j == len(b):
            return -1

        return 0


def task_distress_signal_part_1(test=False):
    filename = "../resources/13-test-input.txt" if test else "../resources/13-input.txt"
    with open(filename) as file:
        lines = file.read().strip().split()

    ll = 0
    rl = 1

    counter = 0

    while ll < len(lines) - 1 and rl < len(lines):
        l_list = literal_eval(lines[ll])
        r_list = literal_eval(lines[rl])

        res = compare_lists(l_list, r_list)

        if res == 1:
            counter += ll / 2 + 1

        ll += 2
        rl += 2

    print(int(counter))


def task_distress_signal_part_2(test=False):
    filename = "../resources/13-test-input.txt" if test else "../resources/13-input.txt"
    lines = []
    with open(filename) as file:
        for line in file.readlines():
            sline = line.strip()
            if sline == "":
                continue
            lines.append(literal_eval(line))

    lines.append([[2]])
    lines.append([[6]])

    sorted_list = sorted(lines, key=cmp_to_key(compare_lists), reverse=True)
    divider_idx = []

    for i, block in enumerate(sorted_list):
        if block == [[2]] or block == [[6]]:
            divider_idx.append(i + 1)

    print(divider_idx[0] * divider_idx[1])



print("--- Part 1 ---")
task_distress_signal_part_1(False)
print("--- Part 2 ---")
task_distress_signal_part_2(False)
