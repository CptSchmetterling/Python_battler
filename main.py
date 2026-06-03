class Monster:
    def __init__(self, name: str, hp: int,defense: int, attack: int,typ:str):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.defense = defense
        self.attack = attack
        self.type = typ

    def __str__(self):
        return (f"{self.name}({self.hp}/{self.max_hp} KP)"
        )


class Attack:
    def __init__(self, name: str, power: int, typ: str):
        self.name = name
        self.power = power
        self.typ = typ.lower()

    def typenvorteil(self,target_monster_type: str)-> float:
        target_type = target_monster_type.lower()
        multiplier = 1.0
        wechselwirkung = {
            "feuer": {"strong": "pflanze", "weak": "wasser" },
            "wasser": {"strong": "feuer", "weak": "pflanze"},
            "pflanze": {"strong": "wasser", "weak": "feuer"},}

        if self.typ in wechselwirkung:
            if wechselwirkung[self.typ]["strong"] == target_type:
                multiplier = 2.0
                print("Es ist sehr effektiv!")
            elif wechselwirkung[self.typ]["weak"] == target_type:
                multiplier = 0.5
                print("Es ist nicht sehr effektiv...")
        return multiplier

#Monster
bisasam = Monster("Bisasam", 45, 49, 49,"Pflanze")
glumanda = Monster("Glumanda", 39, 52, 43,"Feuer")
schiggy = Monster("Schiggy", 44, 65, 49, "Wasser")
#Attacken
tackle = Attack("Tackle", 40, "Normal")
watergun = Attack("Water Gun", 40, "Wasser")
ember = Attack("Ember", 40, "Feuer")
vinewhip = Attack("Vine Whip", 40, "Pflanze")

"""  
class AttackSet:
    pro pokemon
"""""

class GameState:
    def __init__(self,monster_player: Monster, monster_cpu: Monster):
        self.monster_player = monster_player
        self.monster_cpu = monster_cpu
        self.active_player = "Player"

    def switch_turn(self):
        if self.active_player == "Player":
            self.active_player = "Cpu"
        else:
            self.active_player = "Player"
        print(f"{game.get_active_monster()} ist am Zug!\n")

#gibt Aktives Monster zurück
    def get_active_monster(self)-> Monster:
        if self.active_player == "Player":
            return self.monster_player
        return self.monster_cpu

#Monster das angegriffen wird
    def get_attacked_monster(self)-> Monster:
        if self.active_player == "Player":
            return self.monster_cpu
        return self.monster_player

    def do_attack(self, attack: Attack):    #noch direkt Attack
        attacker = self.get_active_monster()
        defender = self.get_attacked_monster()

        print(f"{attacker} setzt {attack.name} ein!\n")

        multiplier = attack.typenvorteil(defender.type)

        damage = int(((2.4 * (attack.power * attacker.attack / defender.defense) / 50 )+2) * multiplier)
        """Schadensformel: 2⋅Level5+2⋅Stärke der Attacke⋅AngriffVerteidigung÷50 * multiplier"""

        defender.hp -= damage
        if defender.hp < 0:
            defender.hp = 0
        print(f"{defender.name} erleidet {damage} Schaden!\n")


    def __str__(self):
        return (f"-----------------------------------\n"
                f"Spieler: {self.monster_player} "
                f"CPU: {self.monster_cpu} "
                f"> > > {self.active_player.upper()}'s turn\n")


if __name__ == "__main__":
    game = GameState(bisasam, schiggy)  ### placeholder hardcoded monster
    print(game)
    game.do_attack(vinewhip)
    game.switch_turn()
    print(game)
    game.do_attack(tackle)
    print(game)