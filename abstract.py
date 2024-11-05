#abc module to create an abstract base class Shape with an abstract method area().
# Then, implement subclasses Circle and Square that provide their own implementations of area().
# Write code to create instances of Circle and Square, and call area() on each.
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius, pi):
        self.radius = int(radius)
        self.pi = int(pi)

    def area(self):
        return self.pi * self.radius**2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def area(self):
        return self.width * self.height



circle = Circle(7,3.14)
print(circle.area())
rectangle = Rectangle(9,5)
print(rectangle.area())

