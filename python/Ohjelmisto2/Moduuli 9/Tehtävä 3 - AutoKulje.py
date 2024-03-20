class Auto:
    
    # Konstruktori, joka alustaa olion attribuutit // rekisteritunnus, huippunopeus, alkunopeus, kuljettu_matka
    def __init__(self, rekisteritunnus, huippunopeus, alkunopeus=0, kuljettu_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.alkunopeus = alkunopeus    # = 0
        self.kuljettu_matka = kuljettu_matka    # = 0

    # Metodi, jolla tulostetaan auton tiedot
    def ominaisuudet(self): 
        print(f"Rekisteritunnus: {self.rekisteritunnus}")
        print(f"Huippunopeus: {self.huippunopeus} km/h")
        print(f"Nopeus: {self.alkunopeus} km/h")
        print(f"Kuljettu matka: {self.kuljettu_matka} km\n")
    
    # Metodi, jolla kiihdytetään autoa
    def kiihdytys(self, nopeuden_muutos):
        self.alkunopeus += nopeuden_muutos # Lisätään alkunopeuteen nopeuden_muutos
        
        if self.alkunopeus < 0: # jos alkunopeus on pienempi kuin 0, niin silloin nopeus on yhtä kuin 0
            self.alkunopeus = 0 
        
        if self.alkunopeus > self.huippunopeus: # Jos alkunopeus on suurempi kuin huippunopeus, niin silloin nopeus on yhtä kuin huippunopeus
            self.alkunopeus = self.huippunopeus

    # Metodi, jolla lasketaan aika ja matka
    def kulje(self, aika):
        self.kuljettu_matka += self.alkunopeus * aika # Kuljettu matka on yhtä kuin alkunopeus * kulutettu_aika



auto1 = Auto("ABC-123", 142, 60, 2000) # rekkari = ABC-123, huippunopeus = 142, alkunopeus = 60, kuljettu_matka = 2000

auto1.kulje(1.5)

auto1.ominaisuudet()