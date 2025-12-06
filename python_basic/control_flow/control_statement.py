def if_display():
    x = int(input("请输入你的年龄: "))

    if x < 0:
        print("年纪不符！")
    elif x == 0:
        print("刚出生！")
    else:
        print("年纪可以了！")


def for_display():
    words = ["cat", "window", "deskpan"]

    for word in words:
        print(word, len(word))

    """修改字典内容"""
    users = {"jiushiwo": "active", "heitiejingjie": "inactive", "fengmuxia": "active"}
    # 迭代一个字典副本
    for user, status in users.copy().items():
        if status == "inactive":
            del users[user]
    print(users)

    users = {"jiushiwo": "active", "heitiejingjie": "inactive", "fengmuxia": "active"}
    # 创建一个副本
    active_users = {}
    for user, status in users.items():
        if status == "active":
            active_users[user] = status
    print(active_users)

    """
    for_else语句
    未执行break语句时，执行else子句
    """
    for n in range(2, 11):
        for x in range(2, n):
            if n % x == 0:
                print(f"{n} equals {x} * {n // x}")
                break
        else:
            print(n, " is a primer number.")


def range_display():
    for i in range(5):
        print(i)

    # 还可使用范围和步长
    list1 = list(range(5, 10))
    print(list1)
    list1 = list(range(-10, -100, -30))
    print(list1)

    # 返回一个枚举对象
    list2 = list(enumerate(list1, 1))
    print(list2)


def match_display():
    status = 415
    match status:
        case 400:
            print("bad request")
        case 401 | 402 | 403:  # 可组合
            print("not aloowed")
        case 404:
            print("not found")
        case 418:
            print("I am teapot")
        case _:
            print("something's wrong with the internet")

    """match还可解构"""
    point = (30, 26)
    match point:
        case (0, 0):
            print("origin")
        case (x, 0):
            print(f"x = {x}")
        case (0, y):
            print(f"y = {y}")
        case (x, y):
            print(f"x = {x},y = {y}")
        case _:
            raise ValueError("not a point")


def display():
    # if_display()
    # for_display()
    # range_display()
    match_display()


display()
