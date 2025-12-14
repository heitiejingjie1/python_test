print("让我们一起练习.")

print("You'd need to know ' bout escapes with \\ that do: ")
print("\n newlines and \t tabs.")

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love 
nor comprehend passion intuition and requires and explanation
\n\t\twhere there is none.
"""

print("-" * 15)

print(poem)

print("-" * 15)

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")


def secrat_formula(started):
    jelly_beans = started * 500
    jar = jelly_beans / 1000
    crates = jar / 500

    return jelly_beans, jar, crates


start_point = 10000
beans, jars, crates = secrat_formula(start_point)

print("格式化字符串")
print("With a starting point of: {}".format(start_point))
print(f"We'd have {beans} beans, {jars} jars and {crates} crates.")

start_point = start_point / 10
print("we can also do that this way: ")
formula = secrat_formula(start_point)

print("列表应用于字符串。")
print("We'd  have {} beans, {} jars and {} crates".format(*formula))
