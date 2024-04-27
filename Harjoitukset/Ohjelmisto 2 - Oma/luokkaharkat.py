class Auto:
    
    def __init__(self, rekisteri_nro, max_nopeus, kulutettu_matka):
        self.rekisteri_nro = rekisteri_nro
        self.max_nopeus = max_nopeus
        self.kulutettu_matka = kulutettu_matka

    def aja_matka(self, matka):
        super().__init__(self)
        self.matka = matka