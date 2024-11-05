#base class employee with a method to calculate salary that prints a generic message.
# Then create a subclass Manager that overrides calculate_salary() to provide a specific calculation for a manager’s salary.
# Demonstrate the overridden behavior.
class Employees:
    def calculate_salary(self):
        print("This is an Employee class for salary calculation")

class Manager(Employees):
    def __init__(self, name, normal_salary, bonus):
        self.name = name
        self.normal_salary = int(normal_salary)
        self.bonus = int(bonus)

    def calculate_salary(self):
        manager_salary = self.normal_salary + self.bonus
        print(f"A manager earns {manager_salary}")


employee = Employees()
employee.calculate_salary()

manager = Manager("Boss", "100000", "20000")
manager.calculate_salary()

