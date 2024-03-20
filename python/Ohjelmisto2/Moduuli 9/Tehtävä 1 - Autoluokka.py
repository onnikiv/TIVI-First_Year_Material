class Auto:
    
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, kuljettu_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus_atm = nopeus
        self.kuljettu_matka = kuljettu_matka


    def ominaisuudet(self):
        print(f"\nRekisteritunnus: {self.rekisteritunnus}")
        print(f"Huippunopeus: {self.huippunopeus}")
        print(f"Nopeus: {self.nopeus_atm}")
        print(f"Kuljettu matka: {self.kuljettu_matka}\n")
    

auto1 = Auto("ABC-123", 142)
auto1.ominaisuudet()