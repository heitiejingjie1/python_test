"""
mixin模式：混入模式
    在 Python 等面向对象语言中，通常它是实现了某种功能单元的类，用于被其他子类继承，将功能组合到子类中
"""


class MappingMixin:
    def __getitem__(self, key):
        return self.__dict__.get(key)

    def __setitem__(self, key, value):
        return self.__dict__.setdefault(key, value)


class ReprMixin:
    def __repr__(self):
        s = self.__class__.__name__ + "("
        for k, v in self.__dict__.items():
            if not k.startswith("_"):
                s += f"{k}={v}, "
        s = s.rstrip(", ") + ")"
        return s


class Person(MappingMixin, ReprMixin):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


p = Person("殷", 30, "男")
print(p.gender)

p.__setitem__("addrr", "重庆")
print(p.__dict__)
print(p)
