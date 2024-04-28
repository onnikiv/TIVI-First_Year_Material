class Auto:
    
    def __init__(self, rekisteri_nro, max_nopeus, ajettu_matka=0):
        self.rekisteri_nro = rekisteri_nro
        self.max_nopeus = max_nopeus
        self.ajettu_matka = ajettu_matka

    def aja_matka(self, matka):
        self.ajettu_matka += matka
    
    def ominaisuudet(self):
         print(f"Rekisteri: {self.rekisteri_nro} --- Max nopeus: {self.max_nopeus} --- Ajettu matka: {self.ajettu_matka} ")
                
auto1 = Auto("ABC-123", 100)
auto1.ominaisuudet()
auto1.aja_matka(235)
auto1.ominaisuudet()