import util


# --- Day 2: Rock Paper Scissors ---

# Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input)
# that they say will be sure to help you win.
# "The first column is what your opponent is going to play:
# A for Rock, B for Paper, and C for Scissors. The second column--"
# Suddenly, the Elf is called away to help with someone's tent.

# The second column, you reason, must be what you should play in response:
# X for Rock, Y for Paper, and Z for Scissors.
# Winning every time would be suspicious, so the responses must have been carefully chosen.

# The winner of the whole tournament is the player with the highest score.
# Your total score is the sum of your scores for each round.
# The score for a single round is the score for the shape you selected
# (1 for Rock, 2 for Paper, and 3 for Scissors)
# plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

def task_rock_paper_scissors_part_1():
    shape_map = {
        'A': 1, 'B': 2, 'C': 3,
        'X': 1, 'Y': 2, 'Z': 3
    }

    total_points = 0

    def process_line(line):
        nonlocal total_points

        points = shape_map[line[2]]
        opponent = shape_map[line[0]]
        helper = points - opponent
        # helper == 0 means draw as both have the same shape, 1 and -2 mean win
        if helper == 0:
            points += 3
        elif helper == 1 or helper == -2:
            points += 6

        total_points += points

    util.read_lines("../resources/02-input.txt", process_line)
    print("Total points: " + str(total_points))


# The Elf finishes helping with the tent and sneaks back over to you.
# "Anyway, the second column says how the round needs to end:
# X means you need to lose, Y means you need to end the round in a draw,
# and Z means you need to win. Good luck!"

def task_rock_paper_scissors_part_2():
    score_map = {'X': 0, 'Y': 3, 'Z': 6}
    shape_map = {'A': 1, 'B': 2, 'C': 3}

    total_points = 0

    def process_line(line):
        nonlocal total_points

        points = score_map[line[2]]

        if points == 3:  # draw
            points += shape_map[line[0]]
        elif points == 6:  # win
            temp = shape_map[line[0]] + 1  # according to the matrix in notes
            if temp > 3:
                temp -= 3
            points += temp
        else:  # lost
            temp = shape_map[line[0]] + 2  # according to the matrix in notes
            if temp > 3:
                temp -= 3
            points += temp

        total_points += points

    util.read_lines("../resources/02-input.txt", process_line)
    print("Total points: " + str(total_points))


print("--- Part 1 ---")
task_rock_paper_scissors_part_1()
print("--- Part 2 ---")
task_rock_paper_scissors_part_2()
