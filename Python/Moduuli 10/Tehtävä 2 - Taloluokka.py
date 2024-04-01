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


class Talo:
    def __init__(self, talonalinkerros, talonylinkerros, hissienmaara):
        '''
        self.hissit = lista, missä metodit ja kuinka monta hissiä talossa on
        '''
        self.hissit = [Hissi(talonalinkerros, talonylinkerros) for _ in range(hissienmaara)] 

    def aja_hissia(self, hissinumero, kohdekerros):
        print("_"*30)
        print(f"Hissin numero: ({hissinumero})\nMihin kerrokseen: ({kohdekerros})")
        self.hissit[hissinumero].kerros_ylos() if kohdekerros > self.hissit[hissinumero].kerros else self.hissit[hissinumero].kerros_alas()

talo = Talo(0, 7, 2) # 0-7 kerrosta, 2 hissiä

talo.aja_hissia(1, 5) # hissi 1, kerrokseen 5
talo.aja_hissia(0, 3)
