"""列表推导式"""

from typing import OrderedDict
import array
import os


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


# list_deri_formula()
# print(last)

"""生成器表达式"""


def list_generative():
    """生成器表达式使用迭代器协议逐个产出项，而不是构建整个列表提供给其他构造函数，使用圆括号"""
    symbols = "$¢£¥€¤"
    gen = tuple(ord(s) for s in symbols)
    print(gen)

    """array构造函数"""
    arr = array.array("I", (ord(s) for s in symbols))
    print(arr)


# list_generative()


"""元组不仅仅是不可变列表"""


def tuple_demo():
    """还可用作没有字段名称的记录"""
    """不能排序"""

    def tuple_record():
        lax_coordinates = (33.9425, -118.408056)
        city, year, pop, chg, area = ("tokyo", 2003, 32_450, 0.66, 8014)
        traveler_ids = [("USA", "31195855"), ("BRA", "CE342567"), ("ESP", "XDA205856")]

        for passport in sorted(traveler_ids):
            print("%s/%s" % passport)

        for country, _ in traveler_ids:
            print(country)

    """不可变列表"""
    """仅针对元组的引用不可变，如果引用的值是可变的，那元组的值也会变化"""

    def tuple_immutable_list():
        a = (10, "alpha", [1, 2])
        b = (10, "alpha", [1, 2])

        print(a == b)
        b[-1].append(3)
        print(a == b)
        print(b)

    tuple_record()
    tuple_immutable_list()

    """判断是否可哈希"""

    def fixed(o):
        try:
            hash(o)
        except TypeError:
            return False
        return True

    a = (10, "alpha", [1, 2])
    b = (10, "alpha", (1, 2))

    print(fixed(a))
    print(fixed(b))

    """元组和列表的特殊方法"""
    tuple()
    list()


# tuple_demo()

"""拆包"""


def unpack():
    """不用我们手动通过索引从序列中提取元素"""

    """并行赋值"""

    def one_line_assignment():
        lax_coordinates = (33.9425, -118.408056)
        latitude, longitude = lax_coordinates
        print(latitude)
        print(longitude)

        def divmod(a, b):
            return a, b

        num = (30, "yinhao")
        print(divmod(*num))  # 这也是拆包

        _, filename = os.path.split(
            "/home/user/projects/skeleton/setup.py"
        )  # 只获取最后一个文件名
        print(filename)

        """使用*获取余下的项"""
        a, b, *rest = range(5)
        print(a)
        print(b)
        print(rest)

        a, *rest, b, c = range(10)  # *可以是任意位置
        print(a)
        print(rest)
        print(b)
        print(c)

    """嵌套拆包"""

    def nesting_unpack():
        metro_areas = [
            ("Tokyo", "JP", 36.933, (35.689722, 139.691667)),
            ("Delhi NCR", "IN", 21.935, (28.613889, 77.208889)),
            ("Mexico City", "MX", 20.142, (19.433333, -99.133333)),
            ("New York-Newark", "US", 20.104, (40.808611, -74.020386)),
            ("São Paulo", "BR", 19.649, (-23.547778, -46.635833)),
        ]

        print(f"{'':15} | {'latitude':>9} | {'longitude':>9}")
        for name, _, _, (lat, lon) in metro_areas:
            if lon <= 0:
                print(f"{name:15} | {lat:9.4f} | {lon:9.4f}")

    one_line_assignment()
    nesting_unpack()


# unpack()

"""模式匹配，改进是析构"""


def match_demo():
    """析构嵌套元组"""

    def nesting_tuple():
        metro_areas = [
            ("Tokyo", "JP", 36.933, (35.689722, 139.691667)),
            ("Delhi NCR", "IN", 21.935, (28.613889, 77.208889)),
            ("Mexico City", "MX", 20.142, (19.433333, -99.133333)),
            ("New York-Newark", "US", 20.104, (40.808611, -74.020386)),
            ("São Paulo", "BR", 19.649, (-23.547778, -46.635833)),
        ]

        print(f"{'':15} | {'latitude':>9} | {'longitude':>9}")
        for record in metro_areas:
            match record:
                case [name, _, _, (lat, lon)] if lon <= 0:
                    print(f"{name:15} | {lat:9.4f} | {lon:9.4f}")

    nesting_tuple()


match_demo()
