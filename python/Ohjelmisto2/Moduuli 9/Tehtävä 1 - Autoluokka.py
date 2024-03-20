class Auto:
    
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, kuljettu_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus_atm = nopeus
        self.kuljettu_matka = kuljettu_matka


    def ominaisuudet(self):
        print(f"\nRekisteritunnus: {self.rekisteritunnus}\nHuippunopeus: {self.huippunopeus}\nNopeus: {self.nopeus_atm}\nKuljettu matka: {self.kuljettu_matka}\n")
    

auto1 = Auto("ABC-123", 142)
auto1.ominaisuudet()