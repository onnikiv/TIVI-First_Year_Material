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
    
    # Metodi, jolla kiihdytetään autoa
    def kiihdytys(self, nopeuden_muutos):
        if self.alkunopeus + nopeuden_muutos > self.huippunopeus: # Jos alkunopeus + nopeuden_muutos on suurempaa kuin huippunopeus niin silloin se on yhtä kuin huippunopeus
            self.alkunopeus = self.huippunopeus
        else:
            self.alkunopeus += nopeuden_muutos # Muuten lisätään alkunopeuteen nopeuden_muutos

    # Metodi, jolla lasketaan aika ja matka
    def kulje(self, aika):
        self.kuljettu_matka += self.alkunopeus * aika # Kuljettu matka on yhtä kuin alkunopeus * kulutettu_aika



auto1 = Auto("ABC-123", 142, 60, 2000) # rekkari = ABC-123, huippunopeus = 142, alkunopeus = 60, kuljettu_matka = 2000

auto1.kulje(1.5)

auto1.ominaisuudet()