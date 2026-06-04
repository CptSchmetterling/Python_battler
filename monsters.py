from monster import Monster
from moves import *


def get_monsterlist():
    monsterlist =[
        Monster("Bisasam", 45, 49, 49, "Pflanze",[tackle, vinewhip,growl, razorleaf]),
        Monster("Glumanda", 39, 52, 43, "Feuer", [tackle, growl, ember, firefang]),
        Monster("Schiggy", 44, 65, 49, "Wasser", [tackle,tailwhip, watergun, bubblebeam])
        ]
    return monsterlist

def hidden_monster():
    return Monster("Dragonite",91, 95, 134, "Dragon",[fireblast, surf, extremespeed, hyperbeam])
