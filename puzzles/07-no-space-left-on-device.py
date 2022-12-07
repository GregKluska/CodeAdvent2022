import util


# --- Day 7: No Space Left On Device ---

def get_total_spaces():
    spaces = {}
    curr_path = []

    def process_command(command):
        nonlocal curr_path
        comm = command.split(" ")

        # we only take "cd" because "ls" has no effect in the current line
        if comm[1] == "cd":
            path_to = comm[2].strip()
            match path_to:
                case "/":
                    curr_path = []
                case "..":
                    del curr_path[-1]
                case other:
                    curr_path.append(other)

    def process_space(line):
        nonlocal spaces, curr_path
        spline = line.split(" ")

        if spline[0] != "dir":
            spaces["/"] = spaces.get("/", 0) + int(spline[0])
            loc_path = ""
            for p in range(0, len(curr_path)):
                loc_path += "/" + curr_path[p]
                spaces[loc_path] = spaces.get(loc_path, 0) + int(spline[0])

    def process_line(line):
        if line[0] == "$":
            process_command(line)
        else:
            process_space(line)

    util.read_lines("../resources/07-input.txt", process_line)

    return spaces


def task_no_space_left_on_device_part1():
    spaces = get_total_spaces()

    res = 0

    for p in spaces:
        if spaces[p] <= 100000:
            res += spaces[p]

    print(res)


def task_no_space_left_on_device_part2():
    spaces = get_total_spaces()

    unused_space = 70000000 - spaces["/"]
    needed_to_get = 30000000 - unused_space

    # looking for the dir
    curr_closest = spaces["/"]
    for p in spaces:
        if needed_to_get <= spaces[p] < curr_closest:
            curr_closest = spaces[p]

    print(curr_closest)


print("--- Part 1 ---")
task_no_space_left_on_device_part1()
print("--- Part 2 ---")
task_no_space_left_on_device_part2()
