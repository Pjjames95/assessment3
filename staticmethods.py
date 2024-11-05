# Calculator class with a static method add() that takes two numbers and returns their sum.
# Also, add a static attribute count to track the number of times the add() method has been called.
# Show how to use this static method and update count.
class Calculator:
    count = 0 #set as the initializer
    @staticmethod
    def add(a, b):
        Calculator.count += 1 #with every calculation there is an addition of 1
        return a + b


test1 = Calculator.add(5, 7) #output to expect is 12 after I call the function and run it
print(f"My answer is: {test1}")
test5 = Calculator.add(45, 67)
print(f"My answer is: {test5}")