# --- Day 15: Beacon Exclusion Zone ---

def dist(a: tuple[int, int], b: tuple[int, int]):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def parse_line(line):
    """ parse line into 2 tuples 1/ Sensor, 2/ Closes beacon, 3/ Distance"""
    line = line.strip().split(": ")
    line[0] = line[0][10:]
    line[1] = line[1][21:]

    line[0] = line[0].split(", ")
    line[1] = line[1].split(", ")

    line[0] = (int(line[0][0][2:]), int(line[0][1][2:]))
    line[1] = (int(line[1][0][2:]), int(line[1][1][2:]))

    # add extra line with distance between points
    line.append(dist(line[0], line[1]))

    return line


def task_beacon_exclusion_zone_part_1(test=True):
    filename = "../resources/15-test-input.txt" if test else "../resources/15-input.txt"
    with open(filename) as file:
        lines = file.readlines()
        lines = list(map(parse_line, lines))

    min_x, max_x, min_y, max_y = 0, 0, 0, 0

    for line in lines:
        min_x = min(min_x, line[0][0], line[1][0])
        max_x = max(max_x, line[0][0], line[1][0])
        min_y = min(min_y, line[0][1], line[1][1])
        max_y = max(max_y, line[0][1], line[1][1])

    ly = 10 if test else 2000000

    cannot_be_there = set()

    for line in lines:
        # check every sensor [0] if it's distance [2] reaches ly
        sb_dist = line[2]
        ls_dist = dist(line[0], (line[0][0], ly))

        if ls_dist > sb_dist:
            # out of the reach
            continue
        # else

        # distance between sensor and Y axis
        ay_dist = abs(line[0][1] - ly)
        ax_min = line[0][0] - (sb_dist - ay_dist)
        ax_max = line[0][0] + (sb_dist - ay_dist)
        for ax in range(ax_min, ax_max + 1):
            cannot_be_there.add(ax)

    # remove beacons from the set
    for line in lines:
        if line[1][1] == ly and line[1][0] in cannot_be_there:
            cannot_be_there.remove(line[1][0])

    print(len(cannot_be_there))


def task_beacon_exclusion_zone_part_2(test=True):
    filename = "../resources/15-test-input.txt" if test else "../resources/15-input.txt"
    with open(filename) as file:
        lines = file.readlines()
        lines = list(map(parse_line, lines))

    min_x, max_x, min_y, max_y = 0, 0, 0, 0

    for line in lines:
        min_x = min(min_x, line[0][0], line[1][0])
        max_x = max(max_x, line[0][0], line[1][0])
        min_y = min(min_y, line[0][1], line[1][1])
        max_y = max(max_y, line[0][1], line[1][1])

    min_lx, max_lx = (0, 20) if test else (0, 4000000)
    min_ly, max_ly = (0, 20) if test else (0, 4000000)
    ly = min_ly

    while ly <= max_ly:
        row_ranges = list()
        for line in lines:
            # check every sensor [0] if it's distance [2] reaches ly
            sb_dist = line[2]
            ls_dist = dist(line[0], (line[0][0], ly))

            if ls_dist > sb_dist:
                # out of the reach
                continue
            # else

            # distance between sensor and Y axis
            ay_dist = abs(line[0][1] - ly)
            ax_min = max(min_lx, line[0][0] - (sb_dist - ay_dist))
            ax_max = min(max_lx, line[0][0] + (sb_dist - ay_dist))
            row_ranges.append((ax_min, ax_max))

        row_ranges = sorted(row_ranges)
        helper = row_ranges[0]
        for i in row_ranges:
            if helper[1] + 1 >= i[0]:
                helper = (helper[0], max(helper[1], i[1]))
            else:
                print("found something at i = %i and ly %i" % (i[0] - 1, ly))
                fx = i[0] - 1
                fy = ly
                ans = (fx * 4000000) + fy
                print("If nothing else found, then the answer is: " + str(ans))
                break

        ly += 1


print("--- Part 1 ---")
task_beacon_exclusion_zone_part_1(False)
print("--- Part 2 ---")
task_beacon_exclusion_zone_part_2(False)
