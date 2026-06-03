from monster import Monster
from buttonpress import text_and_wait_for_enter

class GameState:
    def __init__(self, player_monster: Monster, cpu_monster: Monster):
        self.player_monster = player_monster
        self.cpu_monster = cpu_monster
        self.active_player = "Player"

    def get_active_monster(self)-> Monster:
        if self.active_player == "Player":
            return self.player_monster
        return self.cpu_monster

    def get_attacked_monster(self)-> Monster:
        if self.active_player == "Player":
            return self.cpu_monster
        return self.player_monster

    def switch_turn(self):
        """turnover und anzeige aktueller Spieler"""
        self.active_player = "Cpu" if self.active_player == "Player" else "Player"
        print(f"{self.get_active_monster()} ist am Zug!\n")
        text_and_wait_for_enter()

    def __str__(self):
        return (f"-----------------------------------\n"
                f"Spieler: {self.player_monster} "
                f"CPU: {self.cpu_monster} "
                f"> > > {self.active_player.upper()}'s turn\n")