"""
属性相关的魔法方法
"""


class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    """拦截并获取属性值"""

    def __getattribute__(self, attrname):
        print("获取到了")
        return super().__getattribute__(attrname)

    """获取不存在的属性值时触发"""

    def __getattri__(self, attrname):
        if attrname == "gender":
            print("这是啥~")
        else:
            raise AttributeError

    def __setattr__(self, attrname, value):
        # self.name = value  # 会导致无限递归
        self.__dict__[attrname] = value  # 利用__dict__进行赋值

    def __delattr__(self, attrname):
        del self.__dict__[attrname]


def test():
    stu = Student("殷浩", 30)
    print(hasattr(stu, "name"))  # 判断是否有这个属性
    print(getattr(stu, "name"))  # 获取属性的值
    print(getattr(stu, "_Student__age"))

    setattr(stu, "_Student__age", 36)  # 设置属性的值
    print(getattr(stu, "_Student__age"))

    # print(stu.gender)

    del stu.name
    print(stu.__dict__)


test()
