"""列表的循环删除"""


def deleteList():
    """利用临时列表解决"""
    name = ["yinhao", "yinhong", "huguangwio", "mali", "yinxuanzhobg"]

    temp = []
    for item in name:
        if item.startswith("yin"):
            # name.remove(item)
            temp.append(item)

    for item in temp:
        name.remove(item)

    print(name)


deleteList()
