the_count = [1, 2, 3, 4, 5]
fruits = ["apple", "oranges", "pears", "apricots"]
changes = [1, "pennies", 2, "dimes", 3, "wuarters"]

"""遍历列表"""
for number in the_count:
    print(f"This is count {number}.")

for fruit in fruits:
    print(f"A fruit of type: {fruit}")

for i in changes:
    print(f"I got {i}.")

elements = []
"""使用range()函数"""
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    elements.append(i)

for i in elements:
    print(f"Element was: {i}")
