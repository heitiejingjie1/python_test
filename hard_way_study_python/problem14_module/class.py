from typing import Optional

"""animal is-a object"""


class Animal(object):
    pass


"""dog is-a animal"""


class Dog(Animal):
    def __init__(self, name):
        """dog has-a name"""
        self.name = name


"""cat is-a animal"""


class Cat(Animal):
    def __init__(self, name):
        """cat has-a name"""
        self.name = name


"""person is-a object"""


class Person(object):
    def __init__(self, name):
        """person has-a name"""
        self.name = name
        """person has-a 宠物"""
        self.pet = None


"""emploee is-a person"""


class Emploee(Person):
    def __init__(self, name, salary):
        super(Emploee, self).__init__(name)
        """emploee has-a salary"""
        self.salary = salary


"""fish is-a object"""


class Fish(object):
    pass


"""salmon is-a fish"""


class Salmon(Fish):
    pass


"""halibut is-a fish"""


class Halibut(Fish):
    pass


def display():
    """rover is-a dog"""
    rover = Dog("Rover")
    """satan is-a cat"""
    satan = Cat("Satan")
    """mary is-a person"""
    mary = Person("Mary")
    """mary.pet is-a satan"""
    mary.pet = satan
    """frank is-a emploee has-a name salary"""
    frank = Emploee("Frank", 12000)
    """frank.pet is-a rover"""
    frank.pet = rover
    """flipper is-a fish"""
    flipper = Fish()
    """crouse is-a salmon"""
    crouse = Salmon()
    """harry is-a halibut"""
    harry = Halibut()
