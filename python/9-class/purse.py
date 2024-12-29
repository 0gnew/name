class Purse:
    def __init__(self):
        self.balance = 50

    def get_balance(self) -> int:
        return self.balance

    def add_balance(self, amount: int):
        self.balance += amount

    def spend_balance(self, amount: int):
        self.balance -= amount

