from abc import ABC, abstractmethod


class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def introduce(self):
        print(f"Hi, I'm {self.name}")


class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass


class Runnable(ABC):
    @abstractmethod
    def run(self):
        pass


class Swimmable(ABC):
    @abstractmethod
    def swim(self):
        pass


class Lion(Animal, Runnable):
    def run(self):
        print("I can run!")


class Fish(Animal, Swimmable, Runnable):
    def run(self):
        print("I can run!")

    def swim(self):
        print("I can swim!")


class Eagle(Animal, Flyable, Runnable, Swimmable):
    def run(self):
        print("I can run!")

    def swim(self):
        print("I can swim!")


    def fly(self):
        print("I can fly!")


simba = Lion(name="Simba")
simba.introduce()
simba.run()

print("-" * 10)

nemo = Fish(name="Nemo")
nemo.introduce()
nemo.swim()

print("-" * 10)

baldeagle = Eagle(name="Baldy")
baldeagle.introduce()
baldeagle.run()
baldeagle.fly()
