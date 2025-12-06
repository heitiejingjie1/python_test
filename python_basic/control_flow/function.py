"""斐波那契数列
函数无返回值
"""


def fib_non_return(n):
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b


"""斐波那契数列
函数有返回值
"""


def fib_return_value(n):
    result = []
    a, b = 1, 1

    while a < n:
        result.append(a)
        a, b = b, a + b

    return result


"""默认值参数"""


def ask_ok(prompt, retries=4, reminder="Please try again."):
    while True:
        reply = input(prompt)
        if reply in {"y", "ye", "yes"}:
            return True
        if reply in {"n", "no", "nop", "nope"}:
            return False

        retries -= 1

        if retries < 0:
            raise ValueError("invalid.")

        print(reminder)


"""默认值为列表、字典、或类实例可变类型时，有不同的表现"""


def f_list(a, L=[]):
    L.append(a)
    return L


def f_list_none(a, L=[]):
    """如果不想有以上表现，该做出判断"""
    if L is None:
        L = []

    L.append(a)


def display():
    fib_non_return(4000)
    # print(fib(10))

    result = fib_return_value(2000)
    print(result)

    # ask_ok("n")

    print(f_list(30))
    print(f_list(40))
    print(f_list(50))
    print(f_list_none(31))
    print(f_list_none(31))
    print(f_list_none(31))


display()
