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
    def speak(self):
        pass


animals = [Dog(), Bird(), Fish()]
for animal in animals:
    print(f"{type(animal).__name__} speaks:")
    animal.speak()
    print(f"{type(animal).__name__} moves:")
    animal.move()
