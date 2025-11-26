score = "b"

match score:
    case "a":
        print("score is 'a'")
    case "b":
        print("score is 'b'")
    case "c":
        print("score is 'c'")
    case "d":
        print("score is 'd'")
    case _:
        print("score is ???")

"""复杂匹配"""
age = 15.2

match age:
    case x if x < 10:
        print(f"< 10 years old: {age}")
    case 10:
        print("10 years old.")
    case x if 11 <= x <= 18:
        print("11 ~ 18 years old.")
    case 19:
        print("19 years old.")
    case _:
        print(f"> 19 years old:{age}")

"""匹配列表"""
args = ["gcc", "hello.c", "world.c"]
# args = ["clean"]
# args = ["file.c"]

match args:
    case ["gcc"]:
        print("gcc: missing source files.")
    case ["gcc", file1, *files]:
        print("gcc compile: " + file1 + ", " + ", ".join(files))
    case ["clean"]:
        print("clean.")
    case _:
        print("error.")
