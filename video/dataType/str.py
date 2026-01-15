"""
字符串格式化问题
"""


def formatAndSliceDemo():
    name = input("请输入你的姓名：")
    address = input("请输入你的地址：")
    age = input("请输入你的年龄：")
    hobby = input("请输入你的爱好：")

    # your = "我的姓名为%s, 我的地址是%s, 我的年龄是%d, 我的爱好是%s" % (
    #     name,
    #     address,
    #     age,
    #     hobby,
    # )

    # your = "我的姓名为{}, 我的地址是{}, 我的年龄是{}, 我的爱好是{}".format(
    #     name, address, age, hobby
    # )

    your = f"我的姓名为{name}, 我的地址是{address}, 我的年龄是{age}, 我的爱好是{hobby}"

    print(your)

    """
    slice
    """
    s = "abcdefghjklmnopqrstuvwxyz"
    print(s[3:12:2])
    print(s[-1:-15:-3])


"""
字符串一般操作
"""


def operatorDemo():
    """切割与替换"""
    # 忽略字符串前后空格
    s = "    jehdjjj  hhej hhrj    "
    s1 = s.strip()
    print(s1)

    # 字符串替换
    s1 = s.replace(" ", "")
    print(s1)

    # 字符串切割
    s = "python_c_cpp_c#_rust"
    s1 = s.split("_")  # 用什么切会损失什么
    print(s1)

    """查找与判断"""
    d = input("请输入你的名字:")
    if d.startswith("殷"):
        print("你姓殷")
    else:
        print("不姓殷")


"""字符串判断"""


def isTrueStr():
    print("hajhsgsjhDjshkjs".isupper())
    print("hajhsgsjhDjshkjs".islower())
    print("DHSJHDHSKSHHD".isupper())
    print("dhjshgsjsksgdh".islower())
    print("ndndbdhhjs".isalpha())  # 是否只包含字母
    print("sjnshshs".isalnum())  # 是否只包含字母和数字
    print("hsbjsjshdhj".isdecimal())  # 是否只包含数字
    print("snnsjsjhshsjs".isspace())
    print("hshshshgsj".istitle())

    """对齐文本"""
    print("hello".rjust(20, "="))  # 右对齐
    print("hello".ljust(20, "="))  # 左对齐
    print("hello".center(20, "="))  # 居中对齐


def display():
    # formatAndSliceDemo()
    # operatorDemo()
    isTrueStr()


display()
