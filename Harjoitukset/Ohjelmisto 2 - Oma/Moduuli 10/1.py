class Hissi:
    
    def __init__(self, alin_kerros, ylin_kerros):
        # Konstruktori, jossa alin ja ylinkerros
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros

    def kerros_ylös(self, kohdekerros):
        # Funktio ylöspäin menemiseen
        for _ in range(kohdekerros - self.alin_kerros):
            self.alin_kerros += 1
            print(f"Ylös menty, kerros: {self.alin_kerros}")
   
    def kerros_alas(self, kohdekerros):
        # Funktio alaspäin menemiseen
        for _ in range(self.alin_kerros - kohdekerros):
            self.alin_kerros -= 1
            print(f"Alas menty, kerros: {self.alin_kerros}")

    def siirry_kerrokseen(self, kohdekerros):
        # jos kohdekerros on isompaa kuin alinkerros niin kutsutaan self.kerros_ylös(kohdekerros) <- kohdekerroksena mihin halutaan
        # sama juttu alaspäin menemiseen
        if kohdekerros > self.alin_kerros:
            self.kerros_ylös(kohdekerros)
        elif kohdekerros < self.alin_kerros:
            self.kerros_alas(kohdekerros)

hissi1 = Hissi(0, 5) # alinkerros = 0, ylinkerros = 5

hissi1.siirry_kerrokseen(5)
hissi1.siirry_kerrokseen(0)
