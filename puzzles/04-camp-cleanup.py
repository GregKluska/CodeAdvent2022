import util


# --- Day 4: Camp Cleanup ---

# Some of the pairs have noticed that one of their assignments fully contains the other.
# For example, 2-8 fully contains 3-7, and 6-6 is fully contained by 4-6.
# In pairs where one assignment fully contains the other,
# one Elf in the pair would be exclusively cleaning sections their partner will already be cleaning,
# so these seem like the most in need of reconsideration. In this example, there are 2 such pairs.

# In how many assignment pairs does one range fully contain the other?

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


# It seems like there is still quite a bit of duplicate work planned.
# Instead, the Elves would like to know the number of pairs that overlap at all.

def task_camp_cleanup_part_2():
    pairs = 0

    def process_pair(e1, e2):
        nonlocal pairs

        ov = (max(e1[0], e2[0]), min(e1[1], e2[1]))
        if ov[0] <= ov[1]:
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
task_camp_cleanup_part_2()
