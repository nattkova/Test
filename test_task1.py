import sys
import math
from abc import ABC, abstractmethod
import unittest

class Shape(ABC):
    def __init__(self):
        self.name = "AbstractShape"

    @abstractmethod
    def get_perimetr(self) -> float:
        pass

    @abstractmethod
    def get_area(self) -> float:
        pass

    def get_name(self) -> str:
        return self.name


class Circle(Shape):
    def __init__(self, radius):
        self.name = "Circle"
        self.radius = radius

    def get_perimetr(self):
        return 2 * math.pi * self.radius

    def get_area(self):
        return 2 * math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, side1, side2):
        self.name = "Rectangle"
        self.side1 = side1
        self.side2 = side2

    def get_perimetr(self):
        return 2 * (self.side1 + self.side2)

    def get_area(self):
        return self.side1 * self.side2


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.name = "Square"



def get_shape_by_description(text: str): #хочу передати саме рядок
    parts = text.split()
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
    return shape # для тестів, щоб перевіти, що вона повертає

def get_result_text(text: str):
    shape = get_shape_by_description(text)
    name = shape.get_name()
    area = shape.get_area()
    perimetr = shape.get_perimetr()
    result_string = f"{name} perimetr {perimetr} area {area}"
    return result_string


class TestShapes(unittest.TestCase):
    def test_circle(self):
        text = "Circle Center 1 1 Radius 2"
        shape = get_shape_by_description(text)
        self.assertEqual(shape.get_name(), "Circle")
        self.assertAlmostEqual(shape.get_perimetr(), 12.56637, 5) # має бути рівним цьому числу з точністю до 5 знаків
        self.assertAlmostEqual(shape.get_area(), 25.13274, 5)

    def test_square(self):
        text = "Square TopRight 1 1 Side 1"
        result = get_result_text(text)
        expected_output = "Square perimetr 4.0 area 1.0"
        self.assertEqual(result, expected_output)

    def test_rectangle(self):
        text = "Rectangle TopRight 2 2 BottomLeft 1 1"
        result = get_result_text(text)
        expected_output = "Rectangle perimetr 4.0 area 1.0"
        self.assertEqual(result, expected_output)

    def test_rectangle_objact(self):
        text = "Rectangle TopRight 2 2 BottomLeft 1 1"
        shape = get_shape_by_description(text)
        self.assertEqual(shape.get_name(), "Rectangle")
        self.assertEqual(shape.side1, 1 )
        self.assertEqual(shape.side2, 1 )
        self.assertAlmostEqual(shape.get_perimetr(), 4.0 )
        self.assertAlmostEqual(shape.get_area(),1.0 )

    def test_square_objact(self):
        text = "Square TopRight 1 1 Side 1"
        shape = get_shape_by_description(text)
        self.assertEqual(shape.get_name(), "Square")
        self.assertEqual(shape.side1, 1 )
        self.assertEqual(shape.side2, 1 )
        self.assertAlmostEqual(shape.get_perimetr(), 4.0 )
        self.assertAlmostEqual(shape.get_area(),1.0 )


def main():
    print("Please enter the shape description:")
    input_text = sys.stdin.readline().strip() #сист.бібл..станд.інпут..читаєрядок..видаляєпробіли
    print(get_result_text(input_text))


if __name__ == "__main__":
    #main()
    unittest.main()