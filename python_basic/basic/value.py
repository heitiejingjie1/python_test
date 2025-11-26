a = 123
print(a)
a = "abc"
print(a)  # 会在内存中创建一个字符串，并将a指向该字符串

a = "ABC"
b = a  # 创建变量b，并将b指向字符串"ABC"
a = "XYZ"  # 创建字符串"XYZ"，并将b指向该字符串
print(b)
print(a)

"""Python中没有实质的变量"""
"""只是将变量大写标志该变量为常量"""
PI = 3.14
PI = 3
print(PI)
