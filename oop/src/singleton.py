class Logger:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        self.__logs = []

    def log(self, message):
        self.__logs.append(message)
        print(message)

    def get_logs(self):
        return self.__logs


logger1 = Logger()
logger2 = Logger()

logger1.log("First message")
logger2.log("Second message")

assert logger1 is logger2, "Logger is not a singleton!"
assert logger1.get_logs() == ["First message", "Second message"]
