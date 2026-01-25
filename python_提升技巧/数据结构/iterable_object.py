def iterable():
    """将可迭代对象分解成变量"""
    x, y = (4, 5)
    print(x, y)
    data = ["JIUWHIWO", 30, 65.9, (2026, 1, 18)]
    name, shares, price, date = data
    print(name, shares, price, date)
    """用不到的变量可用_来替代"""
    _, shares, price, _ = data
    print(shares, price)

    """从任意长度的可迭代对象中分解元素"""
    name, *_, date = data
    print(name, date)


iterable()
