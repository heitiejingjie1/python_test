ten_things = str("Apples Oranges Crows Telephone Light Sugar")

print("Wait there are not 10 things in that list. Let's fix that.")

"""split(ten_things, " ")"""
stuff = ten_things.split(" ")
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# while len(stuff) != 10:
#     """pop(more_stuff),把more_stuff作为参数调用pop函数"""
#     next_one = more_stuff.pop()
#     print("Adding: ", next_one)
#     """append(stuff, next_one)"""
#     stuff.append(next_one)
#
#     print(f"There are {len(stuff)} items now.")

length = 10 - len(stuff)
for _ in range(0, length):
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")


print("There we go: ", stuff)
print("Let's  do some things with stuff.")

print(stuff[1])
print(stuff[-1])

# whoa! fancy
"""pop(stuff)"""
print(stuff.pop())
print(" ".join(stuff))

# what? cool!
print("#".join(stuff[3:5]))

# super stellar
