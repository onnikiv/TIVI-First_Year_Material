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
    def kiihdytys(self,nopeuden_muutos):
        if self.alkunopeus + nopeuden_muutos > self.huippunopeus: # Jos alkunopeus + nopeuden_muutos on suurempaa kuin huippunopeus niin silloin se on yhtä kuin huippunopeus
            self.alkunopeus = self.huippunopeus
        else:
            self.alkunopeus += nopeuden_muutos # Muuten lisätään alkunopeuteen nopeuden_muutos


auto1 = Auto("ABC-123", 142)

# Kiihdytetään autoa, lopussa päästään huippunopeuteen
auto1.kiihdytys(30) 
auto1.kiihdytys(50) 
auto1.kiihdytys(70)

# Tulostetaan auton ominaisuudet
auto1.ominaisuudet()

# Hätäjarrutus eli hidastetaan autoa 200 km/h, ja tulostetaan auton ominaisuudet
auto1.kiihdytys(-200)
auto1.ominaisuudet()