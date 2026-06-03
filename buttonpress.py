def text_and_wait_for_enter(txt:str = ""):
    if txt:
        print(f"{txt}")
    input("Press ENTER...")

def auswahl_loop(option):
    while True:
        try:
            auswahl = int(input("Deine Wahl: "))
            if 1 <= auswahl <= len(option):
                return option[auswahl - 1]
            print(f"Bitte eine Zahl zwischen 1 und {len(option)} eingeben.")
        except ValueError:
            print("Ungültige Eingabe")