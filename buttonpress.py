import copy
from monsters import hidden_monster

def text_and_wait_for_enter(txt:str = ""):
    if txt:
        print(f"{txt}")
    input("Press ENTER...")

def auswahl_loop(option):
    hidden = 0
    while True:
        try:
            auswahl = int(input("Deine Wahl: "))
            if auswahl == 149:
                hidden +=1
                if hidden == 3:
                    return hidden_monster()
            elif 1 <= auswahl <= len(option):
                return copy.copy(option[auswahl - 1])
            print(f"Bitte eine Zahl zwischen 1 und {len(option)} eingeben.")
        except ValueError:
            print("Ungültige Eingabe")