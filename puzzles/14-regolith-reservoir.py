# --- Day 14: Regolith Reservoir ---

def task_regolith_reservoir_part_1(test):
    filename = "../resources/14-test-input.txt" if test else "../resources/14-input.txt"
    with open(filename) as file:
        lines = file.readlines()
        lines = list(map(lambda x: x.strip(), lines))

    lines = list(map(lambda x: x.split(" -> "), lines))

    min_x, max_x = None, None
    max_y = 0

    def safe_get(arr, y, x):
        return arr[y][x] if range(len(arr[0])) and y in range(len(arr)) else "."

    def get_x(i):
        return i - min_x

    for m in range(len(lines)):  # y
        for n in range(len(lines[m])):  # x
            lines[m][n] = lines[m][n].split(",")
            lines[m][n] = list(map(lambda i: int(i), lines[m][n]))
            x = lines[m][n][0]
            y = lines[m][n][1]
            if min_x is None or min_x > x:
                min_x = x
            if max_x is None or max_x < x:
                max_x = x
            if max_y is None or max_y < y:
                max_y = y

    grid = [["."] * (get_x(max_x) + 1) for _ in range(max_y + 1)]

    for r in lines:
        last_point = None

        for point in r:
            cx = get_x(point[0])
            cy = point[1]
            grid[cy][cx] = "#"

            if last_point is not None:
                lx = get_x(last_point[0])
                ly = last_point[1]
                while cx != lx or cy != ly:
                    if cx < lx:
                        cx = cx + 1
                    elif cx > lx:
                        cx = cx - 1
                    if cy < ly:
                        cy = cy + 1
                    elif cy > ly:
                        cy = cy - 1
                    grid[cy][cx] = "#"

            last_point = point

    i, x, y = 0, get_x(500), 0

    while x in range(0, get_x(max_x) + 1) and y in range(0, max_y):
        if safe_get(grid, y + 1, x) == ".":
            # can fall down
            y += 1
        elif safe_get(grid, y + 1, x - 1) == ".":
            x -= 1
            y += 1
        elif safe_get(grid, y + 1, x + 1) == ".":
            x += 1
            y += 1
        else:
            if grid[y][x] == "O":
                break
            i += 1
            grid[y][x] = "O"
            x, y = get_x(500), 0

    print(i)


def task_regolith_reservoir_part_2(test):
    filename = "../resources/14-test-input.txt" if test else "../resources/14-input.txt"
    with open(filename) as file:
        lines = file.readlines()
        lines = list(map(lambda x: x.strip(), lines))

    lines = list(map(lambda x: x.split(" -> "), lines))

    min_x, max_x = None, None
    max_y = 0

    def safe_get(arr, y, x):
        if x in range(len(arr[0])) and y in range(len(arr)):
            return arr[y][x]
        else:
            return "."

    for m in range(len(lines)):  # y
        for n in range(len(lines[m])):  # x
            lines[m][n] = lines[m][n].split(",")
            lines[m][n] = list(map(lambda i: int(i), lines[m][n]))
            x = lines[m][n][0]
            y = lines[m][n][1]
            if min_x is None or min_x > x:
                min_x = x
            if max_x is None or max_x < x:
                max_x = x
            if max_y is None or max_y < y:
                max_y = y

    max_y += 2

    grid_width = 2 * max_y + 40

    def get_x(i):
        nonlocal grid_width, max_x
        print("Grid width: %i, i: %i, max: %i, res: %i" % (grid_width, i, max_x - min_x, int(i - min_x)))
        # print("Max: %i" % (max_x))
        res = int(i - min_x) + int((grid_width - (max_x-min_x) -2) / 2)
        print(res)
        return res

    grid = [["."] * grid_width for _ in range(max_y + 1)]
    # grid = [["."] * (get_x(max_x) + 1)  for _ in range(max_y + 1)]

    for r in lines:
        last_point = None

        for point in r:
            cx = get_x(point[0])
            print(len(grid[0]))
            print("cx: " + str(cx))
            cy = point[1]
            grid[cy][cx] = "#"

            if last_point is not None:
                lx = get_x(last_point[0])
                ly = last_point[1]
                while cx != lx or cy != ly:
                    if cx < lx:
                        cx = cx + 1
                    elif cx > lx:
                        cx = cx - 1
                    if cy < ly:
                        cy = cy + 1
                    elif cy > ly:
                        cy = cy - 1
                    grid[cy][cx] = "#"

            last_point = point

    for i in range(len(grid[-1])):
        grid[-1][i] = "#"

    i, x, y = 0, get_x(500), 0

    while True:
        if safe_get(grid, y + 1, x) == ".":
            # can fall down
            y += 1
        elif safe_get(grid, y + 1, x - 1) == ".":
            x -= 1
            y += 1
        elif safe_get(grid, y + 1, x + 1) == ".":
            x += 1
            y += 1
        else:
            if grid[y][x] == "o":
                break
            i += 1
            grid[y][x] = "o"
            x, y = get_x(500), 0

    print("x: %i , y: %i" % (x, y))
    print(i)

    for a in grid:
        print("".join(a))


print("--- Part 1 ---")
task_regolith_reservoir_part_1(False)
print("--- Part 2 ---")
task_regolith_reservoir_part_2(False)
