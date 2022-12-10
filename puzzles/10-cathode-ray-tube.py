import util


# --- Day 10: Cathode-Ray Tube ---

def task_cathode_ray_tube_part_1():
    sum_of_signals = 0
    cycles = 1
    x = 1

    def cycle_updated():
        nonlocal cycles, x, sum_of_signals
        if (cycles - 20) % 40 == 0:
            print("During the %sth cycle, register X has the value %s, so the signal strength is %s * %s = %s." % (
                str(cycles), str(x), str(cycles), str(x), str(cycles * x)))
            sum_of_signals += cycles * x

    def addx(number: int):
        nonlocal cycles, x
        for i in range(0, 2):
            cycles += 1
            if i == 1:
                x += number
            cycle_updated()

    def noop():
        nonlocal cycles
        cycles += 1
        cycle_updated()

    def process_line(line):
        command = line.strip().split()

        match command[0]:
            case "addx":
                addx(int(command[1]))
            case "noop":
                noop()

    util.read_lines("../resources/10-input.txt", process_line)
    print("The sum of these signal strengths is %s." % str(sum_of_signals))


def task_cathode_ray_tube_part_2():
    cycles = 1
    x = 1
    row = ""
    crt = []

    def render():
        nonlocal row, x

        if len(row) + 1 in range(x, x + 3):
            row += "#"
        else:
            row += "."

    def cycle_updated():
        nonlocal cycles, x, row, crt

        render()

        if cycles % 40 == 0:
            crt.append(row)
            row = ""

    def addx(number: int):
        nonlocal cycles, x
        for i in range(0, 2):
            cycles += 1
            if i == 1:
                x += number
                # print_sprint()
            cycle_updated()

    def noop():
        nonlocal cycles
        cycles += 1
        cycle_updated()

    def print_sprint():
        nonlocal x
        debug_text = "Sprite position: "
        for pixel in range(1, 41):
            if pixel in range(x, x + 3):
                debug_text += "#"
            else:
                debug_text += "."
        print(debug_text)

    def process_line(line):
        command = line.strip().split()
        match command[0]:
            case "addx":
                addx(int(command[1]))
            case "noop":
                noop()

    render()
    # print_sprint()
    util.read_lines("../resources/10-input.txt", process_line)

    print()
    print("result: ")
    for i in crt:
        print(i)


print("--- Part 1 ---")
task_cathode_ray_tube_part_1()
print("--- Part 2 ---")
task_cathode_ray_tube_part_2()
