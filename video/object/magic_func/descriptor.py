"""
描述符：定义了__get__()、__set__()、__delete__()方法的类
"""


class C:
    def __get__(self, instance, owner):
        return instance._x

    def __set__(self, instance, value):
        instance._x = value

    def __delete__(self, instance):
        del instance._x


class D:
    def __init__(self):
        self._x = 30

    c = C()


d = D()
print(d.c)
d.c = 36
print(d.__dict__)
del d.c
print(d.__dict__)
print(type(d))
