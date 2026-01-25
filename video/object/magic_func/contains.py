"""
对象成员检测: contains
"""


class Con:
    def __init__(self, data):
        self.data = data

    def __contains__(self, item):
        print("嘿!")
        return item in self.data


s = [1, 2, 3, 4, 5, 6, 7, 8]
c = Con(s)
print(3 in c)
print(188888888 in c)


"""
代偿机制: 如果成员检测时，没有contains方法，会用iter()和next()或者getitem()进行代偿
"""


class ConIter:
    """docstring for ConIter."""

    def __init__(self, data):
        super(ConIter, self).__init__()
        self.data = data

    def __iter__(self):
        print("iter -> ", end="")
        self.i = 0
        return self

    def __next__(self):
        print("next -> ", end="")

        if self.i == len(self.data):
            raise StopIteration
        item = self.data[self.i]
        self.i += 1
        return item

    def __getitem__(self, index):
        print("getitem -> ", end="")
        return self.data[index]


ci = ConIter(s)
print(6 in ci)
