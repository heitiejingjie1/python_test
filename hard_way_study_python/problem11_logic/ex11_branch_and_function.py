from sys import exit


def gold_room():
    """猜数字"""
    print("This room is full of gold. How much do you take?")

    choice = input("> ")

    if "0" in choice or "1" in choice:
        how_much = int(choice)

        if how_much < 50:
            print("Nice, you're not greedy, you win!")
            exit(0)
        else:
            dead("You greedy bastard!")
    else:
        dead("Man, learn to type a number.")


def bear_room():
    print("这里有一只熊.")
    print("这只熊有一堆蜂蜜.")
    print("那只胖熊正站在另一扇门.")

    print("你打算怎么把这只熊移动呢？")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "取蜂蜜":
            dead("那只熊先是盯着你，然后就猛扇了你一耳光。")
        elif choice == "嘲弄熊" and not bear_moved:
            print("这只熊已经从门口离开了。")
            print("你现在可以进入了。")
            bear_moved = True
        elif choice == "嘲弄熊" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insan.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good job!")
    exit(0)


def start():
    print("你在一个黑暗房间里.")
    print("你的左右两边都有门.")
    print("你选择哪一个呢?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()
