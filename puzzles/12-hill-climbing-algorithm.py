import util

# --- Day 12: Hill Climbing Algorithm ---
def task_hill_climbing_algorithm_part_1():
    terrain = []
    util.read_lines("../resources/12-input.txt", lambda x: terrain.append(x.strip()))

    for i in range(len(terrain)):
        for j in range(len(terrain[0])):
            char = terrain[i][j]
            if char == "S":
                start = i, j
            if char == "E":
                end = i, j

    def height(s):
        if s == "S":
            return 0
        if s == "E":
            return 25
        if 97 <= ord(s) <= 122:
            return ord(s) - 97

    def neighbours(i, j):
        for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            ii = i + di
            jj = j + dj

            if not (0 <= ii < len(terrain) and 0 <= jj < len(terrain[0])):
                continue

            if height(terrain[ii][jj]) <= height(terrain[i][j]) + 1:
                yield ii, jj

    visited = [[False] * len(terrain[0]) for _ in range(len(terrain))]
    queue = [(0, start[0], start[1])]

    print("start; " + str(start))

    while len(queue) > 0:
        steps, i, j = queue.pop(0)

        if visited[i][j]:
            continue
        visited[i][j] = True

        if (i, j) == end:
            print(steps)
            break

        for ii, jj in neighbours(i, j):
            queue.append((steps + 1, ii, jj))


print("--- Part 1 ---")
task_hill_climbing_algorithm_part_1()
print("--- Part 2 ---")
# task_hill_climbing_algorithm_part_2()
