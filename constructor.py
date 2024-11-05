#our class is rectangle with a constructor to initialize the rectangle with either one (for a square) or two parameters (for a general rectangle).
# with a method to calculate the area, and test it by creating squares and rectangles.
class Rectangle:
    # the width is initialized to none to make sure that the compiler recognises the object as a square assuming both sides are equal
    def __init__(self, length, width=None):
        self.length = length
        self.width = width
        if width is None:
            self.width = length
            #area of a rectangle is found by multiplying width by length

    def area_tester(self):
        return self.length * self.width

square = Rectangle(10)
print(square.area_tester())
rectangle = Rectangle(20,8)
print(rectangle.area_tester())