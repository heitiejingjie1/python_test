"""
索引相关魔法方法
"""


class Student:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value


class T:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        return self.data[index] ** 3


def test_index():
    s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    stu = Student(s)

    print(stu[3])

    stu[5] = 18
    print(stu[:])

    """for语句也会访问__getitem__()"""
    t = T(s)
    for value in t:
        print(value, end=" ")

    print("\n")


test_index()


"""
迭代器对象魔法方法
拥有__iter__()的对象称为可迭代对象
拥有__iter__()和__next__()的对象称为迭代器
"""


class IterObject:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop

    """返回一个可迭代对象"""

    def __iter__(self):
        return self

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration

        self.value += 1
        return self.value**2


def test_iter():
    s = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    """模拟for迭代"""
    _ = s.__iter__()

    while 1:
        try:
            i = next(_)
        except StopIteration:
            break
        print(i, end=" ")
    print("\n")

    io = IterObject(1, 9)
    for i in io:
        print(i, end=" ")
    print("\n")


test_iter()
