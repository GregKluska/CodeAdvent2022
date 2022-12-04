import util


# --- Day 4: Camp Cleanup ---

def task_camp_cleanup_part_1():
    pairs = 0

    def process_pair(e1, e2):
        nonlocal pairs

        ov = (max(e1[0], e2[0]), min(e1[1], e2[1]))
        if ov == e1 or ov == e2:
            pairs += 1

    def process_line(line):
        pair_ranges = line.strip().split(",")
        e1 = pair_ranges[0].split("-")
        e2 = pair_ranges[1].split("-")
        process_pair((int(e1[0]), int(e1[1])), (int(e2[0]), int(e2[1])))

    util.read_lines("../resources/04-input.txt", process_line)
    print(pairs)


print("--- Part 1 ---")
task_camp_cleanup_part_1()
print("--- Part 2 ---")
# task_camp_cleanup_part_2()
