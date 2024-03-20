class Auto:
    
    # Konstruktori, joka alustaa olion attribuutit // rekisteritunnus, huippunopeus, alkunopeus, kuljettu_matka
    def __init__(self, rekisteritunnus, huippunopeus, alkunopeus=0, kuljettu_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.alkunopeus = alkunopeus    # = 0
        self.kuljettu_matka = kuljettu_matka    # = 0

    # Metodi, jolla tulostetaan auton tiedot
    def ominaisuudet(self): 
        print(f"\nRekisteritunnus: {self.rekisteritunnus}")
        print(f"Huippunopeus: {self.huippunopeus}")
        print(f"Nopeus: {self.alkunopeus}")
        print(f"Kuljettu matka: {self.kuljettu_matka}\n")
    

auto1 = Auto("ABC-123", 142)
auto1.ominaisuudet()