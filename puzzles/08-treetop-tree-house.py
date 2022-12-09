import util


# --- Day 8: Treetop Tree House ---

def task_treetop_tree_house_part1():
    test_data = [
        "30373",
        "25512",
        "65332",
        "33549",
        "35390"
    ]

    rows = []

    def load_line(line):
        nonlocal rows
        rows.append(line.strip())

    def tree_house_task(forrest):
        visible = 0
        for r in range(1, len(forrest) - 1):
            for c in range(1, len(forrest) - 1):
                if is_visible(r, c, forrest):
                    visible += 1

        visible += (len(forrest) * 2) + (len(forrest[0]) * 2) - 4

        return visible

    def is_visible(row, column, forrest):
        l = True
        t = True
        r = True
        b = True
        for i in range(column - 1, -1, -1):
            if int(forrest[row][i]) >= int(forrest[row][column]):
                l = False
                break
        for i in range(row - 1, -1, -1):
            if int(forrest[i][column]) >= int(forrest[row][column]):
                t = False
                break
        for i in range(column + 1, len(forrest[row])):
            if int(forrest[row][i]) >= int(forrest[row][column]):
                r = False
                break
        for i in range(row + 1, len(forrest)):
            if int(forrest[i][column]) >= int(forrest[row][column]):
                b = False
                break
        return l or t or r or b

    util.read_lines("../resources/08-input.txt", load_line)

    print(tree_house_task(rows))


def task_treetop_tree_house_part2():
    test_data = [
        "30373",
        "25512",
        "65332",
        "33549",
        "35390"
    ]

    rows = []

    def load_line(line):
        nonlocal rows
        rows.append(line.strip())

    def tree_house_task(forrest):
        curr_max = 0
        for r in range(1, len(forrest) - 1):
            for c in range(1, len(forrest) - 1):
                curr_max = max(curr_max, scenic_score(r, c, forrest))

        return curr_max

    def scenic_score(row, column, forrest):
        l = 0
        t = 0
        r = 0
        b = 0
        for i in range(column - 1, -1, -1):
            l += 1
            if int(forrest[row][i]) >= int(forrest[row][column]):
                break
        for i in range(row - 1, -1, -1):
            t += 1
            if int(forrest[i][column]) >= int(forrest[row][column]):
                break
        for i in range(column + 1, len(forrest[row])):
            r += 1
            if int(forrest[row][i]) >= int(forrest[row][column]):
                break
        for i in range(row + 1, len(forrest)):
            b += 1
            if int(forrest[i][column]) >= int(forrest[row][column]):
                break
        return l * t * r * b

    util.read_lines("../resources/08-input.txt", load_line)

    print(tree_house_task(rows))


print("--- Part 1 ---")
task_treetop_tree_house_part1()
print("--- Part 2 ---")
task_treetop_tree_house_part2()
