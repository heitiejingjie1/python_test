print("Mary had a little lamb.")
print("It's fleece was write as {}.".format("show"))
print("And everywhere that Mary went.")

print("." * 10)

# What'd that do?
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"

end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print(end1 + end2 + end3 + end4 + end5 + end6, end=" ")
print(end7 + end8 + end9 + end10 + end11 + end12)


"""占位符"""
formatter = "{} {} {} {}"
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(
    formatter.format(
        "Try your", "Own text here", "Maybe a poem", "Or a song about fear"
    )
)


"""转义字符"""
days = "Mon Tue Wed Thu Fri Sat sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the dsys: ", days)
print("Here are the months: ", months)
print("""
There's something going on here.
With the three double quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")


"""三引号"""
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm spilt\non a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """
    I'll to a list:
    \t* Cat food
    \t* fishies
    \t* Catnip\n\t* Grass
    """

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
