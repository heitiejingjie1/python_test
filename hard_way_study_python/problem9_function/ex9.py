def print_two(*argv):
    argv1, argv2 = argv
    print(f"argv1: {argv1}, argv2: {argv2}")


def print_two_again(argv1, argv2):
    print(f"argv1: {argv1}, argv2: {argv2}")


def print_one(argv1):
    print(f"argv1: {argv1}")


def print_none():
    print("nothing...")


def display():
    print_two("Yin", "Hao")
    print_two_again("Yin", "Hao")
    print_one("First")
    print_none()


# display()


def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheese!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


def display_variable_function():
    print("We can just give the function numbers dirictly: ")
    cheese_and_crackers(20, 30)

    print("Or, we can use variables from our script: ")
    amount_of_cheese = 10
    amount_of_crackers = 50

    cheese_and_crackers(amount_of_cheese, amount_of_crackers)

    print("We can even do math inside too: ")
    cheese_and_crackers(10 + 20, 5 + 6)

    print("And we can combine the two, variables and math: ")
    cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


display_variable_function()
