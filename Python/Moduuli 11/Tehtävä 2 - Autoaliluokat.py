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

class Sahkoauto(Auto):
    def __init__(self, rekisteri, huippunopeus, akkukapasiteetti, nopeus=0, matka=0):
        super().__init__(rekisteri, huippunopeus, nopeus, matka)
        self.akkukapasiteetti = akkukapasiteetti

    def lataa(self, lataus):
        self.akkukapasiteetti += lataus

    def tulosta_tiedot(self):
        super().ominaisuudet()
        print(f"Akku: {self.akkukapasiteetti} kWh")


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteri, huippunopeus, bensatankki, nopeus=0, matka=0):
        super().__init__(rekisteri, huippunopeus, nopeus, matka)
        self.bensatankki = bensatankki

    def tankkaa(self, litrat):
        self.bensatankki += litrat

    def tulosta_tiedot(self):
        super().ominaisuudet()
        print(f"Bensatankki: {self.bensatankki} l")


Auto1 = Sahkoauto("ABC-15", 160, 52.5)
Auto2 = Polttomoottoriauto("ACD-123", 130, 32.3)

Auto1.kiihdytys(120)
Auto2.kiihdytys(110)

for _ in range(3):
    Auto1.kulje(1)
    Auto2.kulje(1)

print("\n")
print(f"Sähköautolla kuljettu matka: ({Auto1.matka}) km. Akun kapasiteetti: {Auto1.akkukapasiteetti} kWh.")
print(f"Polttomoottoriautolla kuljettu matka: ({Auto2.matka}) km. Bensatankki: {Auto2.bensatankki} l.")
print("\n")