class BankAccount:
    def __init__(self) -> None:
        self.__balance = 0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        if self.__balance < amount:
            raise ValueError("Недостаточно средств")
        self.__balance -= amount

    def get_balance(self):
        return self.__balance


account = BankAccount()
print(f"Initial balance: {account.get_balance()}")
account.deposit(1000)
print(f"Balance after deposit: {account.get_balance()}")
account.withdraw(500)
print(f"Balance after withdrawal: {account.get_balance()}")
print(f"Final balance: {account.get_balance()}")

try:
    account.withdraw(600)
except ValueError as e:
    print(f"Error when trying to withdraw 600: {e}")

try:
    account.deposit(-100)
except ValueError as e:
    print(f"Error when trying to deposit -100: {e}")
