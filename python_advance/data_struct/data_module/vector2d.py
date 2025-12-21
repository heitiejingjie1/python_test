import math


class Vector(object):
    """初始化向量"""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    """返回字符串表现形式"""

    def __repr__(self):
        return f"Vector({self.x!r},{self.y!r})"

    """返回绝对值"""

    def __abs__(self):
        return math.hypot(self.x, self.y)

    """返回布尔值"""

    def __bool__(self):
        return bool(abs(self))

    """加法"""

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    """标量乘法"""

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
