from typing import Iterable


d = {"a": 1, "b": 2, "c": 3}

"""迭代键"""
for key in d.keys():
    print(key)
"""迭代值"""
for value in d.values():
    print(value)
"""迭代键值"""
for key, value in d.items():
    print(f"{key}:{value}")


"""迭代字符串"""
for ch in "ABCD":
    print(ch)

"""判断对象是否可迭代"""
print(isinstance(d, Iterable))
print(isinstance("abc", Iterable))
print(isinstance(123, Iterable))

"""下标迭代"""
nums = list(range(6))
for i, value in enumerate(nums):
    print(f"i = {i}, value = {value}")


"""练习"""


def findMinAndMax(L):
    if L == []:
        return (None, None)

    min = L[0]
    max = L[0]
    for value in L:
        if value >= max:
            max = value
        if value <= min:
            min = value

    return (min, max)


nums = [6, 1, 123, -45, 65, 98, 456, -79, 15, 30]
print(findMinAndMax(nums))
print(findMinAndMax([]))

# 测试
if findMinAndMax([]) != (None, None):
    print("测试失败!")
elif findMinAndMax([7]) != (7, 7):
    print("测试失败!")
elif findMinAndMax([7, 1]) != (1, 7):
    print("测试失败!")
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print("测试失败!")
else:
    print("测试成功!")
