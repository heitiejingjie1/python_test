from pathlib import Path

path = Path("file_test.txt")
f_string = "我喜欢编程.\n"
f_string += f_string
f_string += f_string
path.write_text(f_string)


"""练习"""
path = Path("guess_book.txt")
context = ""
while True:
    guess = input("请输入你的姓名: ")
    if guess == "exit":
        break

    guess += "\n"
    context += guess

path.write_text(context)
