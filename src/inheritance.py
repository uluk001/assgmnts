class Employee:
    def __init__(self, name, position, salary) -> None:
        self.name = name
        self.position = position
        self.salary = salary

    def get_info(self):
        return {
            "name": self.name,
            "position": self.position,
            "salary": self.salary,
        }


class Developer(Employee):
    def __init__(self, name, position, salary, programming_language):
        super().__init__(name, position, salary)
        self.programming_language = programming_language

    def get_info(self):
        info = super().get_info()
        info["programming_language"] = self.programming_language
        return info


class Manager(Employee):
    def __init__(self, name, position, salary, employees):
        super().__init__(name, position, salary)
        self.employees = employees

    def get_info(self):
        info = super().get_info()
        info["employees"] = [e.name for e in self.employees]
        return info


dev1 = Developer("John Doe", "Developer", 60000, "Python")
dev2 = Developer("Mike Ross", "Developer", 65000, "JavaScript")
manager = Manager("Jane Smith", "Manager", 90000, [dev1, dev2])

print("Developer Info:", dev1.get_info())
print("Manager Info:", manager.get_info())
