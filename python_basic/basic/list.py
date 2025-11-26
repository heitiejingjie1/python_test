#!/usr/bin/env python3
classMates = ["小红", "小明", "小刚"]

length = len(classMates)
# print(classMates[3])
print(classMates[-1])
print(classMates[0])

"""添加元素"""
classMates.append("小殷")  # 追加元素
classMates.insert(2, "小胡")  # 添加元素

"""删除元素"""
mate = classMates.pop()
mate = classMates.pop(0)
print(classMates)

"""列表里面也可以是别的列表"""
classMates = ["小谭", classMates, "小风"]
print(classMates)

# 元组
"""元组一旦初始化就不能更改"""
names = ("yin", "hu", "zhao")
# names[0] = "tan"
t = 1  # 定义的是1这个数
t = (1,)  # 定义的是一个元素的tuple
print(t)

"""可变tuple"""
change = (1, 2, ["yinhao", "yinqiang"])
change[2][0] = "huguangqio"
print(change)

"""练习"""
L = [
    ["Apple", "Google", "Microsoft"],
    ["Java", "Python", "Ruby", "PHP"],
    ["Adam", "Bart", "Bob"],
]

print(L[0][0])
print(L[1][1])
print(L[2][2])
