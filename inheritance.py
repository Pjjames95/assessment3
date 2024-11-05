#base class is animals with attributes eat and sleep.
# a sub class that inherits animals with an inclusion of bark
class Animals:
    def __init__(self, eat, sleep):
        self.eat = eat
        self.sleep = sleep
        pass

class Dog(Animals):
    def __init__(self, eat, sleep, bark):
        super().__init__(eat, sleep)
        self.bark = bark

    def display_info(self):
        print(f"{self.eat} {self.sleep} {self.bark}")

dog1 = Dog("hungrily", "soundly", "loudly")
(dog1.display_info())


