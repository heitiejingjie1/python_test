class Student:
    def __init__(self, name, id):
        """__属性名，表示该属性是私有的"""
        self.__name = name
        """_属性名，表示该属性是受保护的"""
        self._id = id

    def study(self, course_name):
        print(f"{self.__name}正在学习{course_name}.")


stu = Student("yin", 1001)
stu.study("python")

"""可以动态的给对象添加属性"""
# stu.age = 36 # 不行了

"""静态方法和类方法"""


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod  # 声明该方法为静态方法
    def is_valid(a, b, c):
        return a + b > c and a + c > b and b + c > a

    @classmethod  # 声明该方法为类方法，把消息发送给类
    def is_valid_class(cls, a, b, c):
        return a + b > c and a + c > b and b + c > a

    @property  # 将方法声明为属性，只能透过属性方式调用
    def perimeter(self):
        """计算周长"""
        return self.a + self.b + self.c

    def area(self):
        """计算面积"""
        p = self.perimeter / 2
        return ((p * (p - self.a)) * (p * (p - self.b)) * (p * (p - self.c))) ** 0.5


tri = Triangle(5, 9, 12)

is_tri = Triangle.is_valid(5, 9, 12)
print(is_tri)
print(tri.perimeter)
print(tri.area())
