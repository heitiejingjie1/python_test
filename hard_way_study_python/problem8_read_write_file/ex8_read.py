"""不必在脚本中写死文件名，使用命令行参数来获取文件名"""

from sys import argv

# 解包命令行参数
script, filename = argv
# 打开文件并返回文件流
txt = open(filename)

# 输出文件名
print(f"Here's your file {filename}: ")
# 打印文件内容
print(txt.read())
# 关闭文件流
txt.close()

print("Type the filename again: ")
file_again = input("> ")
# 打开文件并返回文件流
txt_again = open(file_again)
# 打印文件内容
print(txt_again.read())
# 关闭文件流
txt.close()
