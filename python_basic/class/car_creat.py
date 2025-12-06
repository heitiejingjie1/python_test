class Car:
    def __init__(self, make, model, year):
        """初始化汽车属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # 给属性赋默认值

    def get_descriptive_name(self):
        """描述性信息"""
        long_name = f"{self.make} {self.year} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"this car has {self.odometer_reading} miles on it.")

    """通过方法修改属性值"""

    def update_odometer(self, mileage):
        """禁止回调里程数"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("不能回调里程数")

    """通过方法递增属性值"""

    def increment_odometer(self, miles):
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("不能递减里程数.")


new_car = Car("audi", "a4", 2025)
print(new_car.get_descriptive_name())
new_car.read_odometer()

"""修改属性的值"""
new_car.update_odometer(35)
new_car.odometer_reading = 30
new_car.read_odometer()
new_car.increment_odometer(10)
new_car.read_odometer()


"""练习"""


class User:
    def __init__(self, login_attempts):
        self.login_attempts = login_attempts

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attemots(self):
        self.login_attempts = 0


my_user = User(0)
my_user.increment_login_attempts()
my_user.increment_login_attempts()
my_user.increment_login_attempts()
my_user.increment_login_attempts()
my_user.increment_login_attempts()
print(my_user.login_attempts)
my_user.reset_login_attemots()
print(my_user.login_attempts)
