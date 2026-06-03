from monster import Monster
from moves import *


def get_monsterlist():
    return[
        Monster("Bisasam", 45, 49, 49, "Pflanze",[tackle, vinewhip]),
        Monster("Glumanda", 39, 52, 43, "Feuer", [tackle, ember]),
        Monster("Schiggy", 44, 65, 49, "Wasser", [tackle, watergun])
        ]