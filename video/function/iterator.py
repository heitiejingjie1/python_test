"""
迭代器

拿到迭代器：
     iter()函数
     __iter__()特殊方法
获取迭代器数据：
     next()函数
     __next__()特殊方法

迭代器本身也可迭代
特性:
    迭代器只能向前
    省内存
    惰性机制
"""

s = "我是迭代器"
its = s.__iter__()
print(its)
print(its.__next__())

while 1:
    try:
        print(its.__next__())
    except StopIteration:
        break


"""
生成器：本质是迭代器
     两种方式：
          1. 生成器函数
               yield: 只要出现了 就是生成器函数
                    1. 返回数据
                    2. 分段执行函数
                处理大批量数据
          2. 生成器表达式
               (数据 for循环 if判断)
"""


"生成器函数"


def func():
    print(4546769)
    yield "wo"  # 也有返回的意思，执行next()才会返回函数
    print("我是迭代器哈哈哈")
    yield "我是生成器"


ret = func()
print(ret.__next__())
print(ret.__next__())

"""生成器使用情况"""


def order():
    lst = []

    for i in range(10000):
        lst.append(f"衣服{i}")
        if len(lst) == 50:
            yield lst

            lst = []


ret = order()
print(ret.__next__())
print(ret.__next__())


"""
推导式:
    列表推导式：[数据 for循环 if判断]
    集合推导式：{数据 for循环 if判断}
    字典推导式：{key:value for循环 if判断}
不要把推导式妖魔化
"""


"""
生成器表达式：一次性的
"""
ret = (i for i in range(10))
print(list(ret))
