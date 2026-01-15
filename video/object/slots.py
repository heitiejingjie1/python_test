"""
__slots__属性:
    1. 节省内存
    2. 访问属性更快
"""

from pympler import asizeof  # 查看内存


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class StudentSlots:
    __slots__ = ["name", "age"]

    def __init__(self, name, age):
        self.name = name
        self.age = age


stu = Student("殷浩", 30)
stu_slots = StudentSlots("殷洪", 36)
print(stu.__dict__)
print(stu_slots.__slots__)

"""查看内存"""
print(asizeof.asizeof(stu))
print(asizeof.asizeof(stu_slots))


"""不能创建新的属性"""
