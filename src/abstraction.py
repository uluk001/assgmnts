import abc


class Transport(abc.ABC):
    @abc.abstractmethod
    def start_engine(self) -> str:
        pass

    @abc.abstractmethod
    def stop_engine(self) -> str:
        pass

    @abc.abstractmethod
    def move(self) -> str:
        pass


class Car(Transport):
    def start_engine(self) -> str:
        return "Car engine starting..."

    def stop_engine(self) -> str:
        return "Car engine stopping..."

    def move(self) -> str:
        return "Car is moving on the road."


class Boat(Transport):
    def start_engine(self) -> str:
        return "Boat engine starting..."

    def stop_engine(self) -> str:
        return "Boat engine stopping..."

    def move(self) -> str:
        return "Boat is sailing on the water."


car = Car()
boat = Boat()

print(f"Start: {car.start_engine()}")
print(f"Move: {car.move()}")
print(f"Stop: {car.stop_engine()}")

print(f"Start: {boat.start_engine()}")
print(f"Move: {boat.move()}")
print(f"Stop: {boat.stop_engine()}")
