import random
from buttonpress import text_and_wait_for_enter, auswahl_loop
from gamestate import GameState
from monsters import get_monsterlist
from attack import do_attack



def menu():
    text_and_wait_for_enter(
        "======================\n"
        "\tMONSTERBATTLER\n\n"
        "   Adventure Awaits\n"
        "======================")


def auswahl_monster(monsterlist: list, player_name: str):
    print(f"\n {player_name}, wähle dein Monster:")
    for i, m in enumerate(monsterlist, start = 1):
        print(f"[{i}]. {m.name} (Typ: {m.type.capitalize()})")

    return auswahl_loop(monsterlist)


def auswahl_attack(monster, is_cpu: bool = False):
    if is_cpu:
        attack = random.choice(monster.attacks)
        print(f"\nCPU wählt: {attack.name}")
        return attack

    print(f"\n {monster.name}, - wähle eine Attacke:")
    for i, atk in enumerate(monster.attacks, start=1):
        print(f"[{i}]. {atk.name} (Typ: {atk.type.capitalize()}, Power:{atk.power})")

    return auswahl_loop(monster.attacks)


def battle_loop(game: GameState):
    """Main battle loop"""
    while game.player_monster.is_alive() and game.cpu_monster.is_alive():
        print(game)

        active = game.get_active_monster()

        if game.active_player == "Player":
            attack = auswahl_attack(active)
        else:
            attack = auswahl_attack(active, is_cpu=True)

        do_attack(attack, game)

    print("\n===========ENDE===========")
    if game.player_monster.is_alive():
        print(f"{game.player_monster.name} WINS")
    else:
        print(f"{game.cpu_monster.name} war stärker.\nGood luck next time!")


def main():
    # Startet Menü
    menu()
    # lädt Monsterkiste
    monsterlist = get_monsterlist()
    # Monsterauswahl
    players_monster = auswahl_monster(monsterlist, "Player")
    # Auswahl zufälliges CPU
    cpus_monster = random.choice([m for m in monsterlist])
    print(f"\nCPU wählt: {cpus_monster.name}!\n")

    game = GameState(players_monster, cpus_monster)
    battle_loop(game)


if __name__ == "__main__":
    main()