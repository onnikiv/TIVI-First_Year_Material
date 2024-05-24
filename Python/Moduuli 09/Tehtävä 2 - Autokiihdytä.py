class Auto:
    
    def __init__(self, rekisteritunnus, huippunopeus, alkunopeus=0, kuljettu_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.alkunopeus = alkunopeus    
        self.kuljettu_matka = kuljettu_matka    

    def ominaisuudet(self): 
        print(f"Rekisteritunnus: {self.rekisteritunnus}")
        print(f"Huippunopeus: {self.huippunopeus} km/h")
        print(f"Nopeus: {self.alkunopeus} km/h")
        print(f"Kuljettu matka: {self.kuljettu_matka} km\n")
    
    def kiihdytys(self, nopeuden_muutos):
        self.alkunopeus += nopeuden_muutos 
        
        if self.alkunopeus < 0: 
            self.alkunopeus = 0 
        
        if self.alkunopeus > self.huippunopeus: 
            self.alkunopeus = self.huippunopeus


auto1 = Auto("ABC-123", 142)

auto1.kiihdytys(30) 
auto1.kiihdytys(50) 
auto1.kiihdytys(70)

auto1.ominaisuudet()

auto1.kiihdytys(-200)
auto1.ominaisuudet()