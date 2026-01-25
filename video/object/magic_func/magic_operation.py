"""
魔法方法
"""

"""一元运算符"""


class Singgle:
    def __init__(self, x) -> None:
        self.x = x

    def __neg__(self):
        return -self.x

    def __pos__(self):
        return self.x

    def __abs__(self):
        return "hahshs"


ss = Singgle(8)
print(-ss)
print(+ss)
ss = -ss
print(abs(ss))
