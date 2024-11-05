# class is cars
# should have a function displaying information for the cars given
# finally it should be callable to print our output
class Cars:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    #     defining a function for displaying information
    def display_info(self):
        return f"The car is a {self.make} {self.model} {self.year}"

car1 = Cars("Honda", "Hybrid", "2021")
car2 = Cars("Toyota", "RAV4", "2024")

# calling the function to print our outputs
print(car1.display_info())
print(car2.display_info())