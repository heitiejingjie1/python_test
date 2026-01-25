"""
property(): 设置属性，放置属性被污染
"""


class Test:
    def __init__(self, x):
        self._x = x

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def del_x(self):
        del self._x

    x = property(get_x, set_x, del_x)


t = Test(30)
print(t.x)
t.x = 35
print(t.__dict__)
del t.x
print(t.__dict__)

"""使用getattr()，setattr()，delattr()实现上述功能"""


class TestAttr:
    def __init__(self, x):
        self._x = x

    def __getattribute__(self, name):
        if name == "x":
            return self._x
        else:
            return super().__getattribute__(name)

    def __setattr__(self, name, value):
        if name == "x":
            super().__setattr__("_x", value)
        else:
            super().__setattr__(name, value)

    def __delattr__(self, name):
        if name == "x":
            del self._x
        else:
            super().__delattr__(name)


t = TestAttr(30)
print(t.x)
t.x = 100
print(t.__dict__)
del t.x
print(t.__dict__)


"""将property作为装饰器，创建只读属性"""


class TestPro:
    def __init__(self, x):
        self.__x = x

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @x.deleter
    def x(self):
        del self.__x


tp = TestPro(36)
print(tp.x)
tp.x = 57
print(tp.__dict__)
del tp.x
print(tp.__dict__)
