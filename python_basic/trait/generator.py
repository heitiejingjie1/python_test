"""生成器
一边循环一边计算的机制，称为生成器
generator: 生成器，保存的是一个算法
"""

L = [x * x for x in range(11)]
print(L)
G = (x * x for x in range(11))
print(G)
for value in G:
    print(value)

"""
如果生成器用列表生成式来写非常困难
可借助函数来写
"""


"""普通函数"""


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n += 1
    return "Done"


"""generator函数"""


def fib_generator(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return "Done"


fib(10)
fibo = fib_generator(6)
print(next(fibo))
print(next(fibo))
print(next(fibo))


def odd():
    print("step 1")
    yield 1
    print("step 2")
    yield (3)
    print("step 3")
    yield (5)


print(next(odd()))
print(next(odd()))
print(next(odd()))

o = odd()
print(next(o))
print(next(o))
print(next(o))
# print(next(o))

"""如需获取最后的return值，需要捕获异常"""
for value in fib_generator(30):
    print(value)

g = fib_generator(10)

while True:
    try:
        x = next(g)
        print("g: ", x)
    except StopIteration as e:
        print("generator return value: ", e.value)
        break

"""练习"""
