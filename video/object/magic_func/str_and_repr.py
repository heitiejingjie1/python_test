"""
字符串魔法方法
str()：将对象转换为字符串
repr()：将对象转换为程序可执行的字符串
"""


def test():
    print(str(123))
    print(repr(123))

    print(str("heitiejingjie"))
    print(repr("heitiejingjie"))

    """将参数去引号"""
    print(eval("12+13"))

    # print(eval(str("hdhdgdhj")))
    print(eval(repr("hdhdgdhj")))

    print(eval(repr(4546458)))

    st = eval("'hshsjdjjd'")
    print(st)


test()


class D:
    """如果对象放入列表，将无法调用"""

    def __str__(self):
        return "I love python."


d = D()

print(d)

d = [D(), D(), D()]
print(d)
for value in d:
    print(value)

print("=" * 20)


class R:
    """如果对象放入列表，可调用"""

    def __repr__(self):
        return "I love python."


r = R()
print(r)
r = [R(), R(), R()]
print(r)
for value in r:
    print(value)
