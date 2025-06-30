class Animal:
    def speak(self):
        print("...")

    def move(self):
        print("I'm walking")


class Flyable:
    def move(self):
        print("I'm flying")


class Swimmable:
    def move(self):
        print("I'm swimming")


class Dog(Animal):
    def speak(self):
        print("Woof!")


class Bird(Flyable, Animal):
    def speak(self):
        print("Tweet!")


class Fish(Swimmable, Animal):
    pass


animals = [Dog(), Bird(), Fish()]

for animal in animals:
    animal.speak()
    animal.move()
