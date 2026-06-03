from attack import *

class Monster:
    def __init__(self, name: str, hp: int,defense: int, attack: int,type:str,attacks:list[Attack]):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.defense = defense
        self.attack = attack
        self.type = type
        self.attacks = attacks

    def is_alive(self)-> bool:
        return self.hp > 0

    def __str__(self):
        return f"{self.name}({self.hp}/{self.max_hp} KP)"