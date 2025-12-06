from name_function import get_formatted_name

print("输入'q'退出.")

while True:
    first = input("输入你的姓: ")
    if first == "q":
        break
    last = input("输入你的姓: ")
    if last == "q":
        break

    full_name = get_formatted_name(first, last)
    print(f"你的姓名为: {full_name}")
