def test_if():
    people = 20
    cats = 30
    dogs = 15

    if people < cats:
        print("Too many cats! The word is doomed!")

    if people > cats:
        print("Not many cats! The word is saved!")

    if people < dogs:
        print("The word is drooled on!")

    if people > dogs:
        print("The word is dry!")
        dogs += 5

    if people >= dogs:
        print("People are greater than or equal to dogs.")

    if people <= dogs:
        print("People are less than or equal to dogs.")

    if people == dogs:
        print("People are dogs.")


# test_if()


def test_if_and_else():
    people = 30
    cars = 40
    trucks = 15

    if cars > people:
        print("We should take the cars.")
    elif cars < people:
        print("We should not take the cars.")
    else:
        print("We can't decide.")

    if trucks > cars:
        print("That's to many trucks.")
    elif trucks < cars:
        print("Maybe we could take the trucks.")
    else:
        print("We still can't decide.")

    if people > trucks:
        print("Alright. let's just take the trucks.")
    else:
        print("Fine. let's stay home then.")


test_if_and_else()
