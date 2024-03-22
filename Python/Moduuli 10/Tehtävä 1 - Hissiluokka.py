class Hissi:
    
    def __init__(self, kerros, alin_kerros=0, ylin_kerros=10):
        self.kerros = kerros
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros

    def kerros_alas(self, kerros):
        kerros = kerros - 1

    def kerros_ylos(self, kerros):
        kerros = kerros + 1


    def siirry_kerrokseen(self, kerros):
        self.kerros = kerros
        if self.kerros < self.alin_kerros:
            self.kerros = self.alin_kerros
        elif self.kerros > self.ylin_kerros:
            self.kerros = self.ylin_kerros
        else:
            return f"Olet kerroksella {self.kerros}."
        alaspain = Hissi.kerros_alas()
        ylospain = Hissi.kerros_ylos()

hissi = Hissi.siirry_kerrokseen(0, 5)