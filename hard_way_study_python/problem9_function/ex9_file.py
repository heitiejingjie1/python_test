from sys import argv

script, input_file = argv

"""读取文件"""


def print_all(f):
    print(f.read())


"""回到文件首"""


def rewind(f):
    f.seek(0)


"""打印一行"""


def print_one_line(line_count, f):
    print(line_count, f.readline(), end="")


def display_file():
    current_file = open(input_file)

    print("First let's print the whole file:\n")
    """打印当前文件"""
    print_all(current_file)

    print("Now let's rewind, kind of like a tape.")
    """将光标移至文件首"""
    rewind(current_file)

    print("Let's print three line: ")
    current_line = 1
    print_one_line(current_line, current_file)
    current_line += 1
    print_one_line(current_line, current_file)
    current_line += 1
    print_one_line(current_line, current_file)


display_file()
