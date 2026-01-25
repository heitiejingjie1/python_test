"""
对象调用方法：call()
让对象像函数一样调用
"""


class Test:
    def __call__(self, *args, **kwargs):
        print(f"位置参数-> {args}\n关键字参数-> {kwargs}")


t = Test()

t(1, 2, 3, name="hah", age=30)


"""基于指数的运算"""


class Power:
    def __init__(self, expr: int):
        self.expr = expr

    def __call__(self, base: int):
        return base**self.expr


p = Power(3)
print(p(30))
p = Power(2)
print(p(3))
