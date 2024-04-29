import random

class Auto:
    
    def __init__(self, rekisteritunnus, huippunopeus, nopeus_nyt = 0, kuljettu_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus_nyt = nopeus_nyt
        self.kuljettu_matka = kuljettu_matka

    def kiihdytä(self,nopeuden_muutos):
        self.nopeus_nyt += nopeuden_muutos
        
        # jos nopeusnyt alle 0 niin nopeus on 0
        if self.nopeus_nyt < 0: 
            self.nopeus_nyt = 0
        
        # jos nopeusnyt ylittää huippunopeuden, muutetaan nopeusnyt huippunopeudeksi
        if self.nopeus_nyt > self.huippunopeus:
            self.nopeus_nyt = self.huippunopeus
    
    def kulje(self,kulutettu_aika):
        # kuljettumatka muokkautuu nopeusnyt kertaa kulutetulla ajalla
        self.kuljettu_matka += self.nopeus_nyt * kulutettu_aika
        
    
    def ominaisuudet(self):
        print(f"Rekisteritunnus: {self.rekisteritunnus}  --- Huippunopeus: {self.huippunopeus} --- Nopeus nyt: {self.nopeus_nyt} --- Kuljettu matka: {self.kuljettu_matka}")
        
Autot = []

for i in range(10):
    huippunopeus = random.randint(100,200)
    rekisteritunnus = f"ABC-{i+1}"
    auto = Auto(rekisteritunnus, huippunopeus)
    Autot.append(auto)

kilpailu = True

while kilpailu: # Kun kilpailu päällä, niin jokaiselle autolle annetaan random nopeus väliltä -10 ja 15 ja kuljetaan 1 tunti
    for auto in Autot:
        auto.kiihdytä(random.randint(-10, 15))
        auto.kulje(1)

        if auto.kuljettu_matka >= 10000: # Jos auton kuljettu matka on yli 10000 km, niin kilpailu loppuu
            kilpailu = False
            break

auton_numero = 1

for auto in Autot:
    # print(f"Auto ({auton_numero})")
    auto.ominaisuudet()
    auton_numero += 1