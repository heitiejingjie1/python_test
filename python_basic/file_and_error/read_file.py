from pathlib import Path

"""读取文件"""
path = Path("pi_digits.txt")
contents = path.read_text()
contents = contents.rstrip()
print(contents)


"""访问文件中的各行"""
lines = contents.splitlines()
for line in lines:
    print(line)

"""使用文件内容"""
pi_string = " "
for line in lines:
    pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))

"""练习"""
python_file = Path("learning_file.txt")
contents = python_file.read_text()
f_string = "In python you can "
for line in contents:
    print(f"{f_string}{line}")
