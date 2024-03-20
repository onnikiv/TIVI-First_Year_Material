import random

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

    # Metodi, jolla lasketaan kuljettumatka
    def kulje(self, aika):
        self.kuljettu_matka += self.alkunopeus * aika

Autot = []

for i in range(10): # For looppi joka luo 10 autoa, rekisteritunnus on ABC-1, ABC-2, ABC-3, jne. ja huippunopeus on random välillä 100-200
    huippunopeus = random.randint(100, 200)
    rekisteritunnus = f"ABC-{i+1}"
    auto = Auto(rekisteritunnus, huippunopeus) 
    Autot.append(auto)

kilpailu = True

while kilpailu: # Kun kilpailu päällä, niin jokaiselle autolle annetaan random nopeus väliltä -10 ja 15 ja kuljetaan 1 tunti
    for auto in Autot:
        auto.kiihdytys(random.randint(-10, 15))
        auto.kulje(1)

        if auto.kuljettu_matka >= 10000: # Jos auton kuljettu matka on yli 10000 km, niin kilpailu loppuu
            kilpailu = False
            break

auton_numero = 1

for auto in Autot:
    print(f"Auto ({auton_numero})")
    auto.ominaisuudet()
    auton_numero += 1
