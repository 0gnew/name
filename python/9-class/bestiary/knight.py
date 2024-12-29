from dataclasses import dataclass
from weaponry.sword import Sword
from weaponry.shield import Shield
from weaponry.crossbow import Crossbow
from world.health import Health


class Knight:
    NOBLE_SWORD_NAME = "Эскалибур"

    def __init__(self, name: str):
        self.name = name
        self.equipment = Equipment()
        self.health = Health.give_birth_a_knight()

    def check_shield(self):
        return bool(equipment.shield.health)

    def loads_crossbow(self, bolts: int):
        for bolt in range(bolts):
            if self.equipment.bolts_bag.use_bolt():
                self.equipment.crossbow.load()

    def __repr__(self):
        return f"Вот я — {self.name}, мой меч — {self.equipment.sword.name}!"

    @staticmethod
    def pronoun_an_elder(elder: str):
        return f"Мой славный предок, рыцарь {elder}"

@dataclass
class Equipment:
    sword: Sword | None = None
    shield: Shield | None = None
    crossbow: Crossbow | None = None
    bolts_bag: BoltsBag = BoltsBag()
