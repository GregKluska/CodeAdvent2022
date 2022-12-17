# --- Day 15: Beacon Exclusion Zone ---

def parse_line(line):
    """ parse line into 2 tuples with params. 1/ Sensor, 2/ Closes beacon"""
    line = line.strip().split(": ")
    line[0] = line[0][10:]
    line[1] = line[1][21:]

    line[0] = line[0].split(", ")
    line[1] = line[1].split(", ")

    line[0] = (int(line[0][0][2:]), int(line[0][1][2:]))
    line[1] = (int(line[1][0][2:]), int(line[1][1][2:]))

    return line


def task_beacon_exclusion_zone_part_1():
    filename = "../resources/15-input.txt"
    with open(filename) as file:
        lines = file.readlines()
        lines = list(map(parse_line, lines))

    min_x, max_x, min_y, max_y = 0, 0, 0, 0

    for line in lines:
        min_x = min(min_x, line[0][0], line[1][0])
        max_x = max(max_x, line[0][0], line[1][0])
        min_y = min(min_y, line[0][1], line[1][1])
        max_y = max(max_y, line[0][1], line[1][1])

    def dist(a: tuple[int, int], b: tuple[int, int]):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    ly = 10
    unique = set()
    for lx in range(min_x, max_x + 1):
        for line in lines:
            sb_dist = dist(line[0], line[1])
            ls_dist = dist(line[0], (lx, ly))

            if sb_dist < ls_dist:
                continue

            unique.add((lx, ly))

    # remove sensors from unique
    for line in lines:
        if line[0] in unique:
            unique.remove(line[0])
        if line[1] in unique:
            unique.remove(line[1])

    print(len(unique))


print("--- Part 1 ---")
task_beacon_exclusion_zone_part_1()
print("--- Part 2 ---")
# task_beacon_exclusion_zone_part_2()
