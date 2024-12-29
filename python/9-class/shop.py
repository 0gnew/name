class Shop:
    def __init__(self):
        self.swords = [
            Sword(name="Ледяной трон", ranged=False, damage=8, price=10),
            Sword(name="Экскалибур", ranged=False, damage=10, price=20),
            Sword(name="Масамунэ", ranged=False, damage=12, price=30)
        ]
        self.bolts_price = 2

    def buy_sword(self, purse):
        for sword in self.swords:
            if purse.get_balance() >= sword.price:
                purse.spend_balance(sword.price)
            return sword

    def buy_bolts(self, purse, amount: int):
        if purse.get_balance() >= self.bolts_price * amount:
            purse.spend_balance(self.bolts_price * amount)
            purse.equipment.bolts_bag.add_bolts(amount)
            return amount
