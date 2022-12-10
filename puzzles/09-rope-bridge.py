import util


# --- Day 9: Rope Bridge ---
def task_rope_bridge_part_1():
    test_data = [
        "R 4",
        "U 4",
        "L 3",
        "D 1",
        "R 4",
        "D 1",
        "L 5",
        "R 2",
    ]

    head = [0, 0]
    tail = [0, 0]
    visited = set()

    def update_tail(x, y):
        nonlocal head, tail, visited
        if rope_length() > 1:
            tail[0] = x
            tail[1] = y
            visited.add((x, y))

    def rope_length():
        nonlocal head, tail
        return max(abs(head[0] - tail[0]), abs(head[1] - tail[1]))

    def move_head(x, y):
        nonlocal head
        head[0] += x
        head[1] += y

        update_tail(head[0] - x, head[1] - y)

    def process_line(line):
        command = line.split(" ")

        move_x = 0
        move_y = 0
        match (command[0]):
            case "L":
                move_x = -1
            case "U":
                move_y = 1
            case "R":
                move_x = 1
            case "D":
                move_y = -1
        for a in range(0, int(command[1])):
            move_head(move_x, move_y)

    util.read_lines("../resources/09-input.txt", process_line)
    # for i in test_data:
    #     process_line(i)
    print(len(visited) + 1)


def task_rope_bridge_part_2():
    test_data = [
        "R 5",
        "U 8",
        "L 8",
        "D 3",
        "R 17",
        "D 10",
        "L 25",
        "U 20",
    ]

    knots = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    visited = set()
    visited.add((0,0))

    def knot_length(a: list, b: list):
        return max(abs(a[0] - b[0]), abs(a[1] - b[1]))

    def update_knot(knot_idx: int):
        nonlocal knots, visited

        if knot_length(knots[knot_idx - 1], knots[knot_idx]) > 1:
            # move the knot because it's too far
            if abs(knots[knot_idx - 1][0] - knots[knot_idx][0]) >= 1:
                if knots[knot_idx - 1][0] - knots[knot_idx][0] > 0:
                    move_x = 1
                else:
                    move_x = -1
            else:
                move_x = 0

            if abs(knots[knot_idx - 1][1] - knots[knot_idx][1]) >= 1:
                if knots[knot_idx - 1][1] - knots[knot_idx][1] > 0:
                    move_y = 1
                else:
                    move_y = -1
            else:
                move_y = 0

            knots[knot_idx][0] += move_x
            knots[knot_idx][1] += move_y

            if knot_idx == 9:
                visited.add((knots[knot_idx][0], knots[knot_idx][1]))

            # print(knots)
            if knot_idx < len(knots) - 1:
                update_knot(knot_idx + 1)

    def move(x, y):
        nonlocal knots

        knots[0][0] += x
        knots[0][1] += y

        update_knot(1)

    def process_line(line):
        # print(line)
        command = line.split(" ")

        move_x = 0
        move_y = 0
        match (command[0]):
            case "L":
                move_x = -1
            case "U":
                move_y = 1
            case "R":
                move_x = 1
            case "D":
                move_y = -1
        for a in range(0, int(command[1])):
            move(move_x, move_y)

    util.read_lines("../resources/09-input.txt", process_line)
    # for i in test_data:
    #     process_line(i)
    print(len(visited))
    # print(visited)


print("--- Part 1 ---")
task_rope_bridge_part_1()
print("--- Part 2 ---")
task_rope_bridge_part_2()
