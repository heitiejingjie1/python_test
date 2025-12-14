i = 0
numbers = []


# while i < 6:
#     print(f"At the top i is {i}.")
#     numbers.append(i)
#     i += 1
#     print("Number now: ", numbers)
#     print(f"At the bottom i is {i}.")
#
# print("The numbers: ")


def print_number():
    for number in numbers:
        print(number)


"""练习"""


def test_while(i):
    if i == 6:
        return

    print(f"At the top i is {i}.")
    numbers.append(i)
    print("Number now: ", numbers)
    print(f"At the bottom i is {i}.")

    return test_while(i + 1)


# test_while(0)
# print_number()


def test_range(count):
    for i in range(0, count):
        print(f"At the top i is {i}.")
        numbers.append(i)
        print("Number now: ", numbers)
        print(f"At the bottom i is {i}.")


test_range(6)
print_number()
