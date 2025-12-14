def add(a, b):
    """返回和"""
    print(f"ADDING {a} + {b}")
    return a + b


def subtract(a, b):
    """返回差"""
    print(f"SUBTRACTING {a} - {b}")
    return a - b


def multiply(a, b):
    """返回积"""
    print(f"MULTIPLYING {a} * {b}")
    return a * b


def divide(a, b):
    """返回商"""
    print(f"DIVIDING {a} / {b}")
    return a / b


def display_math():
    print("让我们来进行一些数学运算吧!")
    age = add(25, 5)
    height = subtract(78, 4)
    weight = multiply(90, 2)
    iq = divide(100, 2)

    print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

    """附加"""
    print("这是附加选项.")
    what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
    print("That becomes: ", what, "can you do it by hand?")

    """数学公式"""
    number = 25 + (78 - (90 * (100 / 2)))
    print(number)

    number = subtract(add(24, divide(34, 100)), 1023)
    print(number)
    number = 24 + 34 / 100 - 1023
    print(number)


display_math()
