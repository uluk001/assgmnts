import abc


class PaymentProcessor(abc.ABC):
    @abc.abstractmethod
    def pay(self) -> str:
        pass


class PayPal(PaymentProcessor):
    def pay(self):
        return "Paying via PayPal"


class CreditCard(PaymentProcessor):
    def pay(self):
        return "Paying via CreditCard"


class Crypto(PaymentProcessor):
    def pay(self):
        return "Paying via Crypto"
