"""
隐式继承
    在父类中定义，但没有在子类定义会隐式继承父类行为
"""


class Parent(object):
    def implicit(self):
        print("PARENT implicit()")

    def override(self):
        print("PARENT override()")

    def altered(self):
        print("PARENT altered()")


class Child(Parent):
    """
    显式覆盖
        子类会覆盖父类的方法的行为
    """

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        """调用父类方法"""
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")


class BadStuff(object):
    pass


"""
多重继承
    同时继承多个父类
"""


class SuperFun(Child, BadStuff):
    pass


dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
