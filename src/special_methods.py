class Temperature:
    def __init__(self, celsius) -> None:
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

    @property
    def kelvin(self):
        return self._celsius + 273.15

    @staticmethod
    def is_freezing(celsius_temp):
        return celsius_temp <= 0

    @classmethod
    def from_fahrenheit(cls, fahrenheit_temp):
        celsius_temp = (fahrenheit_temp - 32) * 5/9
        return cls(celsius_temp)


temp1 = Temperature(25)
print(f"Celsius: {temp1.celsius}°C")
print(f"Fahrenheit: {temp1.fahrenheit}°F")
print(f"Kelvin: {temp1.kelvin}K")
print(f"Is it freezing? {Temperature.is_freezing(temp1.celsius)}")

temp2 = Temperature.from_fahrenheit(32)
print(f"Celsius: {temp2.celsius}°C")
print(f"Fahrenheit: {temp2.fahrenheit}°F")
print(f"Is it freezing? {Temperature.is_freezing(temp2.celsius)}")
