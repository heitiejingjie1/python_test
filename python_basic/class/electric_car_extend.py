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

    """油车油箱"""

    def fill_gas_tank(self):
        pass


"""继承类"""


class Battery:
    """电池类"""

    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"电池的容量为{self.battery_size}-kwh.")

    def get_range(self):
        ranges = 0
        if self.battery_size == 40:
            ranges = 150
        elif self.battery_size == 65:
            ranges = 225

        print(f"该车能行驶{ranges}km.")


class ElectricCar(Car):
    """电动车独特之处"""

    def __init__(self, make, model, year):
        """继承父类的属性"""
        super().__init__(make, model, year)

        # 子类的新属性
        # self.battery_size = 40

        """将实例用做属性"""
        self.battery = Battery()

    """重写父类方法"""

    def fill_gas_tank(self):
        print("该车没有油箱.")


tesla = ElectricCar("tesla", "mod3", 2025)
print(tesla.get_descriptive_name())
tesla.battery.describe_battery()
tesla.fill_gas_tank()
tesla.battery.get_range()
