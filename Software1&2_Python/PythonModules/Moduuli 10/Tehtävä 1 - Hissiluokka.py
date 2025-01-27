class Hissi:
    def __init__(self, alinkerros, ylinkerros):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.kerros = alinkerros

    def kerros_ylos(self):
        if self.kerros < self.ylinkerros:
            self.kerros += 1

    def kerros_alas(self):
        if self.kerros > self.alinkerros:
            self.kerros -= 1

    def siirry_kerrokseen(self, liikutaan):
        print("_"*30)
        print(f"Olet kerroksessa: ({self.kerros})")
        
        if liikutaan < self.kerros:
            while liikutaan < self.kerros:
                self.kerros_alas()
                print(f"Siirrytään kerrokseen: {self.kerros}")
        else:
            while liikutaan > self.kerros:
                self.kerros_ylos()
                print(f"Ylöspäin mennään: {self.kerros}")
        
        print(f"Pysähdytään kerrokseen: {self.kerros}")


hissi = Hissi(0,5)
hissi.siirry_kerrokseen(4)
hissi.siirry_kerrokseen(0)