"""
函数可以当做变量一样使用
函数嵌套:
    将嵌套函数当做变量使用就好理解了

    嵌套函数可以像变量一样作为返回值使用
函数也可作为参数
"""


def func():
    a = 20

    def func2():
        def func3():
            print("func3")

        print("func2")
        func3()

    print(a)
    print("func")
    return func2


# rfunc = func()
# print(rfunc)
# rfunc()


def valueFunc(func):
    print(func)
    func()


valueFunc(func)

"""
作用域:里面可以直接访问函数外面，外面不能访问函数里面
     如想改变全局变量，使用global value 引入全局变量
     如想改变函数局部变量，使用nonlobal value引入局部变量
"""

gValue = 100


def scopeFunc():
    global gValue
    gValue = 200

    nValue = "我是函数局部"

    def inner():
        nonlocal nValue
        nValue = "我是函数局部函数inner"

    inner()
    print(nValue)


scopeFunc()
print(gValue)

"""
闭包：内层函数对外层函数局部变量的使用，此时内层函数称为闭包函数
    1. 让局部变量常驻内存
    2. 避免全局变量被修改
"""


def closedFunc():
    a = 10  # 将它当做全局变量

    # 这就叫闭包
    def inner():
        nonlocal a
        a += 1

    return inner


ret = closedFunc()

ret()

print(ret)

ret()
