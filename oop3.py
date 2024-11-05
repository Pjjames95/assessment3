class Employees:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Payroll:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def print_payroll(self):
        for employee in self.employees:
            print(f"Employee: {employee.name}, Salary: {employee.salary}")

    def total_payroll(self):
        total = 0
        for employee in self.employees:
            total += int(employee.salary)
        return total

# Example usage
emp1 = Employees("Bob", "40000")
emp2 = Employees("James", "50000")
payroll = Payroll()
payroll.add_employee(emp1)
payroll.add_employee(emp2)

payroll.print_payroll()
print(f"Total Payroll: {payroll.total_payroll()}")