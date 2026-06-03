class Attack:
    def __init__(self, name: str, power: int, type: str):
        self.name = name
        self.power = power
        self.type = type.lower()

    def typenvorteil(self,target_type: str)-> float:
        """Gibt den Typenmultiplier zurück
         mit Text ausgabe über effektivität"""
        target = target_type.lower()
        multiplier = 1.0

        wechselwirkung = {
            "feuer": {"strong": "pflanze", "weak": "wasser" },
            "wasser": {"strong": "feuer", "weak": "pflanze"},
            "pflanze": {"strong": "wasser", "weak": "feuer"},}

        if self.type in wechselwirkung:
            if wechselwirkung[self.type]["strong"] == target:
                multiplier = 2.0
                print("Es ist sehr effektiv!")
            elif wechselwirkung[self.type]["weak"] == target:
                multiplier = 0.5
                print("Es ist nicht sehr effektiv...")

        return multiplier

def do_attack(attack: Attack,game)->None:
    """attack und turnover"""
    attacker = game.get_active_monster()
    defender = game.get_attacked_monster()

    print(f"{attacker} setzt {attack.name} ein!\n")

    multiplier = attack.typenvorteil(defender.type)

    #Schadensformel angelehnt an Pokémon Gen 1
    # ((2.4 * Power * Angriff / Verteidigung) / 50 + 2) * Typenmultiplikator
    damage = int(((2.4 * attack.power * attacker.attack / defender.defense) / 50 + 2) * multiplier)

    defender.hp = max(0,defender.hp - damage)
    print(f"{defender.name} erleidet {damage} Schaden!\n")

    game.switch_turn()
