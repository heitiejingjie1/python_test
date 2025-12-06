from collections import deque


def list_display():
    names = [
        "jiushiwo",
        "fengmuxia",
        "heitiejingjie",
        "gaobanshawu",
        "gaobantongjie",
        "xuezhinaixuexia",
    ]
    names2 = ["yin", "hao"]

    names.append("dalaoshi")
    print(names)
    names.extend(names2)
    print(names)
    names.insert(1, "tan")
    print(names)
    names.remove("dalaoshi")
    print(names)
    names.pop()
    print(names)
    print(names.index("fengmuxia"))
    print(names.count("gaobanshawu"))
    print(names.sort())
    print(names.reverse())


list_display()

"""用列表实现堆栈"""


def stack_display():
    stack = [3, 4, 5]
    # 在栈顶插入数据
    stack.append(6)
    stack.append(7)
    print(stack)
    # 在栈顶弹出数据
    print(stack.pop())
    print(stack.pop())


stack_display()

"""用列表实现队列"""


def deque_display():
    queue = deque(["fengmuxia", "heitiejingjie", "jiushiwo", "gaobantongnai"])

    # 队列插入右边数据
    queue.append("gaobanshawu")
    queue.append("xuezhinaixuexia")
    # 队列弹出左边数据
    print(queue.popleft())
    print(queue.popleft())


deque_display()

"""列表推导式"""
squares = [x**2 for x in range(1, 11)]
print(squares)
# 还可推导列表
squares = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(squares)
# 嵌套的列表推导式
matrix = [[1, 2, 3, 10], [4, 5, 6, 11], [7, 8, 9, 12]]
m_list = [[row[i] for row in matrix] for i in range(4)]
print(m_list)

"""del语句"""
a = [1, 2, 3, 4, 56]
print(a)
del a[2]
print(a)
del a[:]
print(a)
del a
# print(a)

"""元组
与列表类似，只是元组元素不可改变
"""
# 元组只有一个元素时，需在元素后添加"，"
singlenton = ("hello",)
print(singlenton)
t = 123, "fengmuxia", "h"
x, y, z = t  # 序列解包
print(x, y, z)
tup = tuple("ueoyeywiwkl")
print(tup)


"""集合
不重复元素组成的无序多项式
"""
names = {"fengmuxia", "heitiejingjie", "fengmuxia", "gaoban"}
print(names)
a = set("asdfjjjhsgjagajushdgsj")
print(a)
