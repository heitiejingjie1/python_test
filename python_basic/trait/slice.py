name = ["yin", "zhao", "hu", "tan", "zhu"]
num = list(range(101))

"""切片"""
# 取前3个元素
print(name[0:3])
print(name[:3])

# 倒数第一个元素
print(name[-1])

# 每隔5个元素取一个元素
print(num[::5])


"""练习"""


def trim(str):
    if str[0] == " ":
        return str[1:]
    if str[-1] == " ":
        return str[:-2]
    if str[0] == " " and str[-1] == " ":
        return str[1:-2]

    return str[:]


# 测试:
if trim("hello  ") != "hello":
    print("测试失败!")
elif trim("  hello") != "hello":
    print("测试失败!")
elif trim("  hello  ") != "hello":
    print("测试失败!")
elif trim("  hello  world  ") != "hello  world":
    print("测试失败!")
elif trim("") != "":
    print("测试失败!")
elif trim("    ") != "":
    print("测试失败!")
else:
    print("测试成功!")
