import sys
from fibo import fib, fib2
import fibo

fib(200)
print(fib2(500))

# 当前脚本的路径
print(sys.path)

a = []

"""查找模块定义的名称"""
print(dir(fibo))
print(dir())
print(dir(sys))

"""包
需要目录中有__init.py__文件才能将称为包
"""
