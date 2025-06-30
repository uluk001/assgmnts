class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def introduce(self):
        print(f"Hi, I'm {self.name}")


class Flyable:
    def fly(self):
        print("I can fly!")


class Runnable:
    def run(self):
        print("I can run!")


class Swimmable:
    def swim(self):
        print("I can swim!")


class Lion(Animal, Runnable):
    pass


class Fish(Animal, Swimmable):
    pass


class Eagle(Animal, Flyable, Runnable):
    pass


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
