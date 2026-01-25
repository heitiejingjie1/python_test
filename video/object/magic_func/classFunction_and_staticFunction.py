"""
类方法：绑定类的方法
静态方法：跟类不绑定，只是放在类里的方法
"""


class Test:
    def func_a(self):
        print(self)

    @classmethod
    def cls_func(cls):
        print(cls)


t = Test()
t.func_a()
t.cls_func()


"""类方法，统计类实例，管理对象"""


class TestCount:
    count: int = 0

    def __init__(self):
        TestCount.count += 1

    @classmethod
    def count_instance(cls):
        print(f"TestCount 创建了 {cls.count} 个实例.")


tc = TestCount()
tc2 = TestCount()
tc3 = TestCount()
tc3.count_instance()


"""静态方法"""


class TestStatic:
    count: int = 0

    def __init__(self):
        TestStatic.count += 1

    @staticmethod
    def count_instance():
        print(f"TestCount 创建了 {TestStatic.count} 个实例.")


tc = TestStatic()
tc2 = TestStatic()
tc3 = TestStatic()
tc.count_instance()
TestStatic.count_instance()
