txt = open("ex8_sample.txt")

print("Here's your file ex8_sample.txt: ")
print(txt.read())

print("Type the filename again: ")
file_again = input("> ")
# 打开文件并返回文件流
txt_again = open(file_again)
# 打印文件内容
print(txt_again.read())
