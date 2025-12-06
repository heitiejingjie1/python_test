"""关键字参数"""


def parrot(voltage, state="a stiff", action="voom", type="Norwegian Blue"):
    print("-- This parrot wouldn't", action, end=" ")
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


def parrot_display():
    """正确调用"""
    # 1个位置参数
    parrot(1000)
    # 1个关键字参数
    parrot(voltage=1000)
    # 两个关键字参数
    parrot(voltage=1000000, action="VOOOOOM")
    # 关键字参数不必按照声明函数时的顺序来调用
    parrot(action="VOOOOOM", voltage=1000000)
    # 位置参数
    parrot("a million", "bereft of life", "jump")
    # 1个位置参数，1个关键字参数
    parrot("a thousand", state="pushing up the daisies")

    """错误调用"""
    # parrot() # 缺失必需的参数
    # parrot(voltage=5.0, 'dead') # 关键字参数后存在非关键字参数
    # parrot(110, voltage=220) # 同一个参数重复的值
    # parrot(actor='John Cleese') # 未知的关键字参数


def func_test(a):
    pass


def func_test_display():
    """不能对同一个参数多次赋值"""
    # func_test(30, a=31)


"""特殊参数"""


# 仅限位置参数，在参数后添加"/"
def location(arg1, arg2, arg3, /):
    pass


# 仅限关键字参数，在参数前添加"*"
def key_word(*, key1, key2, key3):
    pass


def foo(name, /, **kwds):
    return "name" in kwds


def display():
    parrot_display()
    func_test_display()
    foo(1, **{"name": 2})


display()
