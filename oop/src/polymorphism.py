import math


class Shape:
    def area(self):
        return 0

    def perimeter(self):
        return 0


class Rectangle(Shape):
    def __init__(self, width, height) -> None:
        super().__init__()
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius) -> None:
        super().__init__()
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius


shapes = [
    Rectangle(5, 3),
    Rectangle(10, 4),
    Circle(2),
    Circle(5),
    Rectangle(7, 7),
    Circle(1.5),
]

for i, shape in enumerate(shapes, 1):
    print(f"Shape #{i} ({type(shape).__name__}):")
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
