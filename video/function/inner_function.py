"""
内置函数
"""

"""format"""
a = 18
print(format(a, "08x"))  # 定长字符串

"""ord、chr"""
a = "殷"
print(ord(a))  # 获取Python中unicode编码
print(chr(ord(a)))  # 转化码位为文字

# for i in range(65535):
#     print(chr(i), end="")


"""all、any"""
print(all(["hah", "d", 18]))  # 当做and来使用
print(any(["shsjjs", 0]))  # 当做or来使用


"""
enumerate
直接获取索引和数据
"""
name = ["殷浩", "印象很深", "shdhhdj", "多喝水"]

for key, value in enumerate(name):
    print(f"{key} {value}")

"""hash、id"""
a = "殷浩"
print(hash(a))  # 计算hash值
print(hash(a))  # 计算hash值

print(id(a))  # 直接获取内存地址


"""dir"""

print(dir(a))  # 获取当前数据可执行的操作

"""
zip：把多个可迭代内容合并，按索引位置合并
"""
name = ("殷浩", "殷洪", "胡光琼")
age = (30, 36, 56)
attr = ("ChongQing", "HeChuan", "QuanZhou")

print(list(zip(name, age, attr)))

"""
locales：获取局部作用域以字典类型返回的局部变量
globals：获取全局作用域以字典类型返回的全局变量
"""


def func_local():
    x = 20

    def inner():
        inner_x = 30

    print(locals())
    print(globals())


func_local()


"""
sorted: 排序
需要一个排序函数
sorted(iter,key=排序函数)
"""
s = sorted(["jiushiwo", "heitiejingjie", "fengmuxia"], key=lambda s: len(s))
print(s)


"""
filter: 筛选
需要一个筛选函数
"""
s = filter(lambda s: s[0][0] in "j", s)
print(list(s))


"""
map: 映射
需要一个映射函数
"""
s = list(map(lambda x: x.upper(), name))
print(s)
