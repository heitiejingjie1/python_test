import os

"""列表生成式"""

nums = [x * x for x in range(1, 11)]
print(nums)

# 偶数平方
nums = [x * x for x in range(1, 11) if x % 2 == 0]
print(nums)

# 还可使用两层循环
string = [m + n for m in "ABC" for n in "DEF"]
print(string)

# 列出当前目录下的所有文件
files = [d for d in os.listdir(".")]
print(files)


"""练习"""
L1 = ["Hello", "World", 18, "Apple", None]
L2 = [s.lower() if isinstance(s, str) == True else s for s in L1]
print(L2)
