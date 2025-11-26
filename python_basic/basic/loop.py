"""
for .... in 循环
迭代元素
"""

names = ["yin", "hu", "tan", "zhao"]
for name in names:
    print(name)

# 计算1 ~ 10之和
sum = 0
# for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
for x in range(11):  # range生成一列数字
    sum += x
print(sum)


"""
while循环
条件循环
"""
# 计算0 ~ 99奇数之和
sum = 0
n = 99
while n > 0:
    sum += n
    n -= 2
print(n)
print(sum)


"""练习"""
L = ["Bart", "Lisa", "Adam"]
for name in L:
    print(f"hello, {name}")

n = 10
# while n > 0:
#     print("jump")
