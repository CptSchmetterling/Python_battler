class Attack:
    def __init__(self, name: str, power: int, type: str, pp: int, accuracy: int=100):
        self.name = name
        self.power = power
        self.type = type.lower()
        self.pp = pp
        self.accuracy = accuracy


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


