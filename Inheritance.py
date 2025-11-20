AIM:
To write a python program to find the area of triangle, circle and rectangle by using the
concept of inheritance.

ALGORITHM:
1. Start
2. Define a base class Shape with a method area() (can be an empty or general method).
3. Define a derived class Triangle that inherits from Shape:
a) Take base and height as input
b) Implement the area() method as: (0.5 * base * height)
4. Define a derived class Rectangle that inherits from Shape:
a) Take length and width as input
b) Implement the area() method as: length * width
5. Define a derived class Circle that inherits from Shape:
a) Take radius as input
b) Implement the area() method as: π * radius^2
6. Create instances of each derived class and call the area() method
7. Display the results
8. End

PROGRAM:
import math

# Base Class
class Shape:
def area(self):
return 0

# Derived Class for Triangle
class Triangle(Shape):
def init (self, base, height):

39 | P a g e

self.base = base
self.height = height

def area(self):
return 0.5 * self.base * self.height

# Derived Class for Rectangle
class Rectangle(Shape):
def init (self, length, width):
self.length = length
self.width = width

def area(self):
return self.length * self.width

# Derived Class for Circle
class Circle(Shape):
def init (self, radius):
self.radius = radius

def area(self):
return math.pi * self.radius ** 2

# Main Program
print(&quot;Area Calculations:&quot;)

# Triangle
b = float(input(&quot;Enter base of triangle: &quot;))
h = float(input(&quot;Enter height of triangle: &quot;))
triangle = Triangle(b, h)
print(f&quot;Area of Triangle: {triangle.area():.2f}&quot;)

# Rectangle
l = float(input(&quot;\nEnter length of rectangle: &quot;))

39 | P a g e

w = float(input(&quot;Enter width of rectangle: &quot;))
rectangle = Rectangle(l, w)
print(f&quot;Area of Rectangle: {rectangle.area():.2f}&quot;)

# Circle
r = float(input(&quot;\nEnter radius of circle: &quot;))
circle = Circle(r)
print(f&quot;Area of Circle: {circle.area():.2f}&quot;)

OUTPUT:

Area Calculations:
Enter base of triangle: 10
Enter height of triangle: 5
Area of Triangle: 25.00

Enter length of rectangle: 8
Enter width of rectangle: 4
Area of Rectangle: 32.00

Enter radius of circle: 7
Area of Circle: 153.94
