#two classes i.e cats and dogs each with a make_sound that produces different sounds
#takes an object and accepts a call to make a sound
class Pets:
    def make_sound(self):
        return "All pets make a sound"

#child class dogs will directly use the make_sound function just as the base class but with a different return
class Dog(Pets):
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return f"{self.name} barks"

# same thing happens with the cats class
class Cat(Pets):
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        return f"{self.name} meows"

dog1 = Dog("Tiger")
print(dog1.make_sound())
cat1 = Cat("Cutty")
print(cat1.make_sound())