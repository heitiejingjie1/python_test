import math

"""定义函数"""


def my_abs(x):
    # 类型检查
    if not isinstance(x, (int, float)):
        raise TypeError("bad operand type.")

    if x >= 0:
        return x

    x = -x
    return x


print(my_abs(-30))
# my_abs("a")
# abs("a")

"""空函数"""


def get():
    pass


"""返回多个值"""


def move(x, y, step, angle=0.0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)

    return nx, ny


x, y = move(100, 100, 30, math.pi / 6)
print(x, y)


"""练习"""


def duard(a, b, c):
    dleta = math.sqrt(b**2 - 4 * a * c)

    x1 = (-b + dleta) / 2 * a
    x2 = (-b - dleta) / 2 * a

    return x1, x2


"""测试"""
print("quadratic(2, 3, 1) =", duard(2, 3, 1))
print("quadratic(1, 3, -4) =", duard(1, 3, -4))

if duard(2, 3, 1) != (-0.5, -1.0):
    print("测试失败")
elif duard(1, 3, -4) != (1.0, -4.0):
    print("测试失败")
else:
    print("测试成功")


"""函数参数"""


def power(x, n=2):
    s = 1
    while n > 0:
        s *= x
        n -= 1
    return s


print(power(3))
print(power(3, 3))


"""默认参数(坑)
默认参数必须指向不可变对象
"""


def add_end(L=[]):
    L.append("END")
    return L


print(add_end([1, 2, 3]))
print(add_end())
print(add_end())


def new_add_end(L=None):
    if L is None:
        L = []

    L.append("END")
    return L


print(new_add_end())
print(new_add_end())


"""可变参数
list或tuple参数
"""


def add(*nums):
    sum = 0

    for num in nums:
        sum += num

    return sum


print(add(1, 2, 3))

"""关键字参数
dict参数: key=value 键值对参数
"""


def person(name, age, **kw):
    print("name: ", name, "age: ", age, "other: ", kw)


person("yin", 30)
person("zhao", 29, city="chongwing", job="engineer")

extra = {"city": "chongqing", "job": "销售"}
person("yin", 30, **extra)

"""
命名关键字参数

"""


# def person_ars_name(name, age, **kw):
"""如果参数列表里面有可变参数，就不用使用"*"""


def person_ars_name(name, age, *, city, job):
    print(f"name = {name}\nage = {age}\ncity = {city}\njob = {job}")


def person_change_args(name, age, *args, city, job):
    pass


person_ars_name("zhao", 30, city="shanghai", job="程序员")


"""练习"""


def mul(*args):
    mul_num = 1
    for num in args:
        mul_num *= num

    return mul_num


# 测试
print("mul(5) =", mul(5))
print("mul(5, 6) =", mul(5, 6))
print("mul(5, 6, 7) =", mul(5, 6, 7))
print("mul(5, 6, 7, 9) =", mul(5, 6, 7, 9))
if mul(5) != 5:
    print("mul(5)测试失败!")
elif mul(5, 6) != 30:
    print("mul(5, 6)测试失败!")
elif mul(5, 6, 7) != 210:
    print("mul(5, 6, 7)测试失败!")
elif mul(5, 6, 7, 9) != 1890:
    print("mul(5, 6, 7, 9)测试失败!")
else:
    try:
        mul()
        print("mul()测试失败!")
    except TypeError:
        print("测试成功!")


"""递归函数"""


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


"""尾递归
在函数返回的时候，调用自身本身
"""


def fact_iter(n, product):
    if n == 1:
        return product

    return fact_iter(n - 1, n * product)


def fact_product(n):
    return fact_iter(n, 1)


print(fact(5))
print(fact_product(100))

"""汉诺塔"""


def hannuota(n, a, b, c):
    if n == 1:
        print(a, "===>", c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)


hannuota(5, "a", "b", "c")
