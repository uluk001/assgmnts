class Bird:
    def speak(self) -> str:
        return "I'm a Bird!"


class Flyable:
    def fly(self):
        return "I'm flying!"


class Sparrow(Bird):
    def speak(self) -> str:
        return super().speak()


class Penguin(Bird):
    def speak(self) -> str:
        return super().speak()


def test_bird_behavior(bird: Bird):
    print(f"Птица говорит: {bird.speak()}")
    return bird.speak()


def test_liskov_substitution():
    birds = [
        Bird(),
        Sparrow(),
        Penguin(),
    ]

    for bird in birds:
        result = test_bird_behavior(bird)
        print(f"Результат для {type(bird).__name__}: {result}")


test_liskov_substitution()
