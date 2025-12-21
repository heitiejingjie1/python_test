"""列表推导式"""

from typing import OrderedDict


def list_deri_formula():
    symbols = "$¢£¥€"

    codes = [ord(symbol) for symbol in symbols]
    print(codes)
    # print(symbol)

    """
    海象运算符
    作用域限定在该函数内
    """
    x = "ABC"
    codes = [last := ord(c) for c in x]
    print(codes)
    print(last)

    """列表推导式与filter和map函数"""
    beyond_ascii = [ord(c) for c in symbols if ord(c) > 127]
    print(beyond_ascii)
    beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
    print(beyond_ascii)

    """练习：笛卡尔积"""
    colors = ["white", "black"]
    sizes = ["S", "M", "L"]
    tShirts = [(color, size) for color in colors for size in sizes]
    print(tShirts)
    """打印"""
    for color in colors:
        for size in sizes:
            print(color, size)


list_deri_formula()
# print(last)

"""列表生成式"""


def list_generative():
    pass
