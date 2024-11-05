#a class Vector that represents a vector in 2D space with x and y components.
#Overload the + operator to allow vector addition.
#Test this functionality by creating two Vector objects and adding them.
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y) #accepts the additin of a vector to another(overloading)

    def __str__(self):
        return f"{self.x}, {self.y}" #provides a readable string for the new vector object

vector1 = Vector(1, 3)
vector2 = Vector(6, 8)
vector3 = vector1 + vector2
print(f"Our vector sum is: ({vector3})")