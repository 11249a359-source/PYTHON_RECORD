import math

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2

rect = Rectangle(10, 5)
tri = Triangle(8, 6)
cir = Circle(7)

print("Area of Rectangle:", rect.area())
print("Area of Triangle:", tri.area())
print("Area of Circle:", round(cir.area(), 2))
