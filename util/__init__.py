def read_lines(file_name, block):
    file = open(file_name, 'r')
    lines = file.readlines()
    for line in lines:
        block(line)