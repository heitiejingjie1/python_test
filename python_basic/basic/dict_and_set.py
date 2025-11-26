"""
dict: 字典
键值对: {"key": "value"}
"""

scores = {"yin": 96, "hu": 89, "feng": 65}
print(scores["feng"])
# 插入值
scores["zhao"] = 78
print(scores)


"""一个key只能对应一个value，多次插入同一key会覆盖前一个value"""
scores["tan"] = 92
scores["tan"] = 48
print(scores["tan"])

"""如果key不存在会报错"""
# print(scores["li"])
# 使用get方法获取值,不存在放回none
print(scores.get("li"))

"""删除pop(key)"""
scores.pop("yin")
print(scores)

"""key必须是不可变对象，计算key使用的是hash算法"""

"""
set: 与dict类似
只有key，没有value, 且没有重复的key
"""
s = {"yin", "zhao", "tan"}
print(s)

"""将list变为set"""
num = [1, 2, 3]
s = set(num)
print(s)

"""add添加set元素"""
s.add(4)
s.add(2)
print(s)

"""remove删除set元素"""
s.remove(2)
print(s)

"""练习"""
t = (1, 2, 3)
s = set(t)
print(s)
t = (1, 2, [3, 4])
# s = set(t)
print(s)
