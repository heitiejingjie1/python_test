from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("以'w'模式打开文件。")
target = open(filename, "w")

print("清空文件。拜拜!")
target.truncate()

print("现在我要让你写三行。")
line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print("现在将这三行写入文件。")
target.write(line1 + "\n")
target.write(line2 + "\n")
target.write(line3 + "\n")

print("现在关闭这文件。")
target.close()
