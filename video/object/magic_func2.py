"""
__new__()、__init__()、__del__()
__new__负责"生": 创建instance(对象)
__init__负责"养": 赋予对象各种属性
"""


class UpperCls(str):
    """cls代表正在实例化的类"""

    def __new__(cls, value):
        new_value = value.upper()
        return super().__new__(cls, new_value)


uc = UpperCls("hello")
print(uc)


class Person:
    """slef指向被__new__创建出来的实例"""

    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person("小红", 9)
print(p.name)


"""
单例模式：
"""


class DatabaseConnector:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, host, port):
        if not hasattr(self, "initialized"):
            self.host = host
            self.port = port
            self.initialized = True


conn1 = DatabaseConnector("localhost", 5432)
conn2 = DatabaseConnector("localhost", 5431)

print(conn1)
print(conn2)
print(conn1 is conn2)


"""
不可变类定制：
"""


class PositiveInt(int):
    """创建的整数永远为正"""

    def __new__(cls, value):
        if value < 0:
            value = -value
        return super().__new__(cls, value)

    def __init__(self, value):
        super().__init__()

    def __del__(self):
        print("我销毁了")


p = PositiveInt(-10)
del p
