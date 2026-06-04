from attack import Attack

#gehört nirgendwo richtig hin auser gamestate,ausgelagert für weitere Kampfmechaniken
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