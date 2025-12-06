class Dog:
    """模拟小狗"""

    # 创建实例时自动调用
    def __init__(self, name, age):
        """初始化属性"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗坐下"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """模拟小狗滚动"""
        print(f"{self.name} rolled over.")


"""创建实例"""
my_dog = Dog("write", 30)
your_dog = Dog("black", 36)

# 访问属性
print(f"my dog name is {my_dog.name}.")
print(f"my dog age is {my_dog.age}.")
print(f"my dog name is {your_dog.name}.")
print(f"my dog age is {your_dog.age}.")

# 访问方法
my_dog.sit()
my_dog.roll_over()


"""练习"""


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print("餐馆正在开业。")


restaurant = Restaurant("fengmuxia", "米线")
restaurant.describe_restaurant()
restaurant.open_restaurant()
