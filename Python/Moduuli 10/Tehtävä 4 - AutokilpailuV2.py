import random

class Auto:
    
    # Konstruktori, joka alustaa olion attribuutit // rekisteritunnus, huippunopeus, alkunopeus, kuljettu_matka
    def __init__(self, rekisteritunnus, huippunopeus, alkunopeus=0, kuljettu_matka=0):
        self.rekisteri = rekisteritunnus  
        self.huippunopeus = huippunopeus
        self.nopeus = alkunopeus    
        self.matka = kuljettu_matka

    # Metodi, jolla tulostetaan auton tiedot
    def ominaisuudet(self): 
        print(f"Rekisteritunnus: {self.rekisteri}")
        print(f"Huippunopeus: {self.huippunopeus} km/h")
        print(f"Nopeus: {self.nopeus} km/h") 
        print(f"Kuljettu matka: {self.matka} km\n")
    
    # Metodi, jolla kiihdytetään autoa
    def kiihdytys(self, nopeuden_muutos):
        self.nopeus += nopeuden_muutos 
        
        if self.nopeus < 0: 
            self.nopeus = 0 
        
        if self.nopeus > self.huippunopeus: 
            self.nopeus = self.huippunopeus

    # Metodi, jolla lasketaan kuljettumatka
    def kulje(self, aika):
        self.matka += self.nopeus * aika  

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdytys(nopeuden_muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"Auto:          Nopeus (km/h): Matka (km)")
        for auto in self.autot:
            print(f"{auto.rekisteri:<15}{auto.nopeus:<15}{auto.matka:<15}")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.pituus:
                return True
        return False


autot = []
for i in range(10):
    rekisteri = f"ABC-{i+1}"
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekisteri, huippunopeus))

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunti = 1

while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    if tunti % 10 == 0:
        print("-" * 40)
        print(f"Tunti {tunti} tilanne:\n")
        kilpailu.tulosta_tilanne()
    tunti += 1

print("-" * 40)
print(f"Kilpailu '{kilpailu.nimi}' on päättynyt! Lopullinen tilanne on:\n")
kilpailu.tulosta_tilanne() 
