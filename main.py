import math
from abc import ABC, abstractmethod

enter_massage = input("Enter your massage: ")
test_message1 = "Square TopRight 1 1 Side 1"
test_message2 = "Rectangle TopRight 2 2 BottomLeft 1 1"
test_message3 = "Circle Center 1 1 Radius 2"


class Shape(ABC):
    @abstractmethod
    def get_perimetr(self) -> float:
        pass

    @abstractmethod
    def get_area(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_perimetr(self):
        return 2 * math.pi * self.radius

    def get_area(self):
        return 2 * math.pi * (self.radius ** 2)


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_perimetr(self):
        return 4 * self.side

    def get_area(self):
        return self.side * self.side


class Rectangle(Shape):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def get_perimetr(self):
        return 2 * (self.side1 + self.side2)

    def get_area(self):
        return self.side1 * self.side2


def print_result(input):
    parts = input.split()
    if parts[0] == "Circle":
        radius = float(parts[5])
        shape = Circle(radius)
    elif parts[0] == "Rectangle":
        side1 = abs(float(parts[2]) - float(parts[5]))
        side2 = abs(float(parts[3]) - float(parts[6]))
        shape = Rectangle(side1, side2)
    elif parts[0] == "Square":
        side = float(parts[5])
        shape = Square(side)
    else:
        return f'Unknown shape type: {parts[0]}'

    area = shape.get_area()
    perimetr = shape.get_perimetr()
    result_string = f"{parts[0]} perimetr {perimetr} area {area}"
    print(result_string)


print_result(test_message3)
print_result(test_message1)
print_result(test_message2)
print_result(enter_massage)