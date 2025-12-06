try:
    print(5 / 0)
except ZeroDivisionError:
    print("0不能作为除数.")

print("请输入两个数字，我来得到商。\n输入'q'退出.\n")

while True:
    first_number = input("first_number: ")
    if first_number == "q":
        break
    second_number = input("second_number: ")
    if second_number == "q":
        break

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("0不能作为除数.")
    else:
        print(answer)
